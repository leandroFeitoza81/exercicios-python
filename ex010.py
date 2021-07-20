"""
    Programa consulta uma API e printa na tela a cotação do dólar  para Real
"""
import requests
import json
from decouple import config

SECRET = config('SECRET_KEY')
URL = 'https://currencyapi.net/api/v1/rates?'
BASE = 'USD'
response = requests.request('GET', URL + 'Key=' + SECRET + '&base=' + BASE)
json = json.loads(response.content)
value = (json['rates']['BRL'])
formatted_str = str('{:.3f}'.format(value)).replace('.', ',')
print(f'R${formatted_str}')
