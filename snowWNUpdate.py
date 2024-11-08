import requests
from requests.auth import HTTPBasicAuth

# ServiceNow instance details
instance = "your_instance"  # e.g., dev12345
username = "your_username"
password = "your_password"

# Incident sys_id
sys_id = "incident_sys_id_here"  # replace with the actual sys_id of the incident

# API URL for the incident
url = f"https://{instance}.service-now.com/api/now/table/incident/{sys_id}"

# Headers and data
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
data = {
    "work_notes": "Adding work notes through the API. Example note."
}

# Make the API request
response = requests.patch(url, auth=HTTPBasicAuth(username, password), headers=headers, json=data)

# Check if the update was successful
if response.status_code == 200:
    print("Work notes updated successfully.")
    print("Response:", response.json())
else:
    print(f"Failed to update work notes. Status code: {response.status_code}")
    print("Response:", response.text)
