import requests

endpoint = "https://httpbin.org/anything"

response = requests.get(endpoint, json={"query":"Hello World!"})
source = response.text
json_response = response.json()
status = response.status_code

print(json_response)
