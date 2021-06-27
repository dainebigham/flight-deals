import requests
from pprint import pprint

TEQUILA_URL = 'https://tequila-api.kiwi.com/locations/query'
TEGUILA_HEADER = {
    'apikey': ''
}

class FlightSearch:
    def __init__(self):
        pass

    def get_iata_code(self, city):

        response = requests.get(f'{TEQUILA_URL}?term={city}', headers=TEGUILA_HEADER)
        data = response.json()
        iata_code = data['locations'][0]['code']

        return iata_code