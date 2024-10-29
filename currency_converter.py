import requests
import os 
from dotenv import load_dotenv
import math 

load_dotenv()

api_key = os.getenv('API_KEY')

# Function to convert currencies
def convert_currency(amount, from_currency, to_currency):
  url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}'
  response = requests.get(url)
  data = response.json()
  rate = data['conversion_rates'][to_currency]
  conversion = amount * rate 
  rounded_number = math.floor(conversion)
  rounded_rate = math.floor(rate)
  return f'You just converted {amount} {from_currency} to {rounded_number} {to_currency} at  rate of {rounded_rate}'

print(convert_currency(40, 'EUR', 'NGN'))
