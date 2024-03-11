import os
import requests
import json

TOKEN = os.getenv('SELLIX_TOKEN')

def get_products():
    url = "https://dev.sellix.io/v1/products"
    
    headers = {"Authorization": f"Bearer {TOKEN}"}

    response = requests.request("GET", url, headers=headers)

    return json.loads(response.text)['data']['products']

