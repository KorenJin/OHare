import requests

# Script to connect microservices apps with the Kong broker

# Define the URL of the Kong API gateway
kong_url = "http://34.31.241.179:8000"  # Replace <ip_address_of_kong> with the actual IP address

# Example GET request to retrieve data from a microservice through Kong
response = requests.get(f"{kong_url}/<microservice_endpoint>")
print(response.json())  # Assuming the response is in JSON format

# Example POST request to send data to a microservice through Kong
data = {
    "key1": "value1",
    "key2": "value2"
}
response = requests.post(f"{kong_url}/<microservice_endpoint>", json=data)
print(response.json())  # Assuming the response is in JSON format