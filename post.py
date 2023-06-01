import csv
import json
import requests

# Read CSV file and convert to list of dictionaries
with open("file.csv", 'r') as f:
    reader = csv.DictReader(f)
    data = [dict(row) for row in reader]

# Create JSON payload
payload = {
    "name": "api_test",
    "values": data
}

# Convert payload to JSON string
json_payload = json.dumps(payload, ensure_ascii=False)
print(json_payload)

headers = {
    "Authorization": "Bearer api-key",
    "Content-Type": "application/json"
}

# Send POST request with JSON payload and headers
response = requests.post("https://api.planadoapp.com/v2/dictionaries", headers=headers, data=json_payload)

# Print response
print(response.status_code)
