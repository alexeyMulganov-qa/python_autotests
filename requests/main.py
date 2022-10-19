import requests

url = "https://petstore.swagger.io/v2/pet"

response = requests.post(url, json = {
  "id": 9595,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "bulldozer",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)

response = requests.put(url, json = {
  "id": 9595,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "excavator",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)

response = requests.get("https://petstore.swagger.io/v2/pet/9595")
print(response.text)