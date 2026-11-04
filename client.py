import requests

BASE_URL = "http://127.0.0.1:8000"

# GET
response = requests.get(f"{BASE_URL}/products")
print("GET:", response.status_code)
print(response.json())

# POST
new_product = {
    "id": 5,
    "name": "Mouse",
    "price": 800,
    "category": "Accessories"
}

response = requests.post(
    f"{BASE_URL}/products",
    json=new_product
)

print("POST:", response.status_code)
print(response.json())

# GET by ID
response = requests.get(f"{BASE_URL}/products/5")
print("GET BY ID:", response.json())

# PUT
updated_product = {
    "id": 5,
    "name": "Wireless Mouse",
    "price": 1200,
    "category": "Accessories"
}

response = requests.put(
    f"{BASE_URL}/products/5",
    json=updated_product
)

print("PUT:", response.json())

# DELETE
#response = requests.delete(f"{BASE_URL}/products/5")
#print("DELETE:", response.json())