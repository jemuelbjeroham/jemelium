import requests
from requests.auth import HTTPBasicAuth

# Replace these with your ServiceNow instance details
instance = "your_instance"  # e.g., dev12345
username = "your_username"
password = "your_password"

# Define the incident sys_id or query parameter
sys_id = "incident_sys_id_here"  # replace with the actual sys_id

# API URL
url = f"https://{instance}.service-now.com/api/now/table/incident/{sys_id}"

# Headers for JSON response
headers = {
    "Accept": "application/json"
}

# Make the API call
response = requests.get(url, auth=HTTPBasicAuth(username, password), headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    short_description = data['result']['short_description']
    print(f"Short Description: {short_description}")
else:
    print(f"Failed to retrieve incident. Status code: {response.status_code}")
    print("Response:", response.text)
