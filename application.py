from flask import Flask
from flask import request
import json
import logging
import time
import base64
import requests
from verify import token

application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def index():
    if len(token) > 0:
        # print("Authenticated successfully")
        # Requesting data from API
            result = requests.get("https://sandbox.livevol.com/api/v1/delayed/market/scans/options/put-vertical-spread", headers={"Authorization": "Bearer " + token}, verify=False)
            #result = requests.get("https://sandbox.livevol.com/api//v1/delayed/market/symbols/TSLA", headers={"Authorization": "Bearer " + token}, verify=False)
        #print(result.json())
    else:
        print("Authentications failed")
    return str(result.json())


if __name__ == '__main__':
  application.run()
