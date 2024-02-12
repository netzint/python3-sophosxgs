import requests
import json

# Setzen Sie Ihre Client-ID und das Client-Geheimnis hier ein
client_id = '41d77df9-c190-4b7d-80db-401b22970f9f'
client_secret = 'e70f95080bc2d2cc9df4b729676ba404824b96306b6cadefe5c66f253052a3e1be0aec48c7e7cea7a91058d56f19892d33d9'

# URL für die Token-Anforderung
url = 'https://id.sophos.com/api/v2/oauth2/token'

# Daten für die Anforderung
data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': 'token'
}

# Header für die Anforderung
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Senden der Anforderung
response = requests.post(url, data=data, headers=headers)

# Überprüfen des Antwortstatus
if response.status_code != 200:
    # Fehler - Fehlermeldung anzeigen
    print(f'Fehler: {response.status_code}')
    print(response.text)
    exit()

# Erfolgreich - Das Token aus der Antwort extrahieren
token = response.json().get('access_token')
#print(f'Token: {token}')

API_URL = "https://api.central.sophos.com"

headers = {
    "Authorization": "Bearer " + token,
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.get(API_URL + "/whoami/v1", headers=headers)
partnerid = response.json().get('id')
#print(f'Partner ID: {partnerid}')

headers["X-Partner-ID"] = partnerid

### SHOW TENANTS
response = requests.get(API_URL + "/partner/v1/tenants?pageTotal=true", headers=headers)
tenants = response.json()

### CREATE TENANT
# data = {
#     "name": "Robert-Bosch-Schule Ulm",
#     "dataGeography": "DE",
#     "contact": {
#         "firstName": "Joachim",
#         "lastName": "Pfister",
#         "email": "administrator@rbs-ulm.de",
#         "phone": "+497311613755",
#         "address": {
#             "address1": "Egginger Weg 30",
#             "city": "Ulm",
#             "countryCode": "DE",
#             "postalCode": "89077"
#         }
#     },
#     "billingType": "usage"
# }

# data = json.dumps(data)

# response = requests.post("https://api.central.sophos.com/partner/v1/tenants", headers=headers, data=data)
# print(response.json())

### GET TENANT BY NAME
tenantid = ""
for tenant in tenants["items"]:
    if tenant["name"] == "Robert-Bosch-Schule Ulm":
        tenantid = tenant["id"]
        API_URL = tenant["apiHost"]

headers["X-Tenant-ID"] = partnerid