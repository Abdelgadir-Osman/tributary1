import requests

# Test the /record endpoint
response = requests.post("http://localhost:8000/record", json={"engine_temperature": 0.3})
print(f"Record Status Code: {response.status_code}")
print(response.json())

# Test the /collect endpoint
response = requests.post("http://localhost:8000/collect")
print(f"Collect Status Code: {response.status_code}")
print(response.json())