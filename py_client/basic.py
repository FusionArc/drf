import requests

endpoint = "https://httpbin.org/anything"
backend = "http://localhost:8000"

# response = requests.get(backend, json={"query":"Hello World!"})
response = requests.get(backend)
source = response.text
status = response.status_code
# json_response = response.json()

print(source)
