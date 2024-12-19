import smtplib
from email.mime.text import MIMEText
import requests

def detect_environment():
    """
    Determines whether the script is running on SAT or DFW
    by checking the accessibility of environment-specific URLs.
    """
    sat_test_url = "https://prodbat11lsat.usaa.com:8443/ControlM"
    dfw_test_url = "https://prodbat11ldfw.usaa.com:8443/ControlM"

    try:
        # Check SAT URL
        response = requests.get(sat_test_url, timeout=5)
        if response.status_code == 200:
            return "SAT"
    except requests.RequestException:
        pass

    try:
        # Check DFW URL
        response = requests.get(dfw_test_url, timeout=5)
        if response.status_code == 200:
            return "DFW"
    except requests.RequestException:
        pass

    return None

def check_web_status(environment):
    """
    Checks the status of web services based on the detected environment.
    Sends an email if necessary.
    """
    if environment == "DFW":
        webservices = [
            "emprod1.usaa.com:8443",
            "prodbat11ldfw.usaa.com:8443",
            "prodbat12ldfw.usaa.com:8443",
        ]
        up_exceptions = ["emprod1.usaa.com:8443"]
    elif environment == "SAT":
        webservices = [
            "emprod1.usaa.com:8443",
            "prodbat11lsat.usaa.com:8443",
            "prodbat12lsat.usaa.com:8443",
        ]
        up_exceptions = ["emprod1.usaa.com:8443"]
    else:
        print("Unknown environment. Exiting.")
        return

    # Check the status of each web service
    down_services = []
    for service in webservices:
        url = f"https://{service}/ControlM"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code != 200:
                down_services.append(service)
        except requests.RequestException:
            down_services.append(service)

    # Determine if an email needs to be sent
    if down_services != up_exceptions:
        send_email(environment, down_services)
    else:
        print(f"All services in {environment} are up.")

def send_email(environment, down_services):
    """
    Sends an email notification about down services.
    """
    # Construct the email content
    subject = f"Control-M WEB Down on {environment}"
    body = f"The following Control-M web services are down on {environment}:\n\n" + "\n".join(down_services)

    # Replace with your email settings if SMTP is not automatically configured
    from_email = "your_email@example.com"
    to_emails = ["use_production_control_tech@internal.usaa.com", "another_email@example.com"]

    # Create MIMEText email object
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)

    # Use system's SMTP settings or override manually
    try:
        smtp = smtplib.SMTP('localhost')  # Assumes SMTP is set up on localhost
        smtp.sendmail(from_email, to_emails, msg.as_string())
        print("Email sent successfully.")
        smtp.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    environment = detect_environment()
    if environment:
        print(f"Detected environment: {environment}")
        check_web_status(environment)
    else:
        print("Unable to determine environment.")

######
Explanation:
Detect Environment:

The script tries to access a specific URL from SAT (prodbat11lsat) and DFW (prodbat11ldfw).
If SAT URL is reachable, it concludes that the script is running in the SAT environment.
Similarly, if DFW URL is reachable, it concludes DFW.
If neither URL is accessible, it exits without proceeding further.
Check Web Service Status:

The script checks the health of all web services in the detected environment.
Services are flagged as "down" if they:
Do not respond successfully.
Have a non-200 HTTP status code.
Send Email:

The email subject includes the detected environment (e.g., SAT or DFW).
The body lists the services that are down.
Email is sent using the system's SMTP (localhost), assuming the system has a configured SMTP service like Postfix or Sendmail.
Email Example Output:

Subject: Control-M WEB Down on SAT
Body:
makefile
Copy code
The following Control-M web services are down on SAT:

prodbat11lsat.usaa.com:8443
prodbat12lsat.usaa.com:8443
SMTP Details:
If the system's SMTP (localhost) does not work, you can replace 'localhost' with your actual SMTP server details:

python
Copy code
smtp = smtplib.SMTP('smtp.usaa.com', 587)  # Example SMTP server
smtp.starttls()
smtp.login('your_username', 'your_password')  # Provide credentials if needed
Let me know if you need further clarification!

############################