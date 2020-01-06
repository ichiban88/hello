import json
import base64
import requests
# Required package requests: `pip install requests`

client_id = "ichiban@posteo.net_api_client_1577871127"
client_secret = "3f919e51427848b7a6ed68fe20b6111f"

identity_url = "https://sandbox.livevol.com/id/connect/token"

encoded = base64.b64encode((client_id + ':' + client_secret).encode())
headers = {"Authorization": "Basic " + encoded.decode('ascii')}
payload = {"grant_type": "client_credentials"}

# Requesting access token
token_data = requests.post(identity_url, data=payload, headers=headers)
if token_data.status_code == 200:
        token = token_data.json()['access_token']
        if len(token) > 0:
            print("Authenticated successfully")
        # Requesting data from API
            #result = requests.get("https://sandbox.livevol.com/api//v1/delayed/market/symbols/MSFT", headers={"Authorization": "Bearer " + token}, verify=False)
        #print(result.json())
else:
    print("Authentications failed")
