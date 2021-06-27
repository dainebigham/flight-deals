import requests
from pprint import pprint
from keys.keys import TEQUILA_API_KEY

TEQUILA_URL = 'https://tequila-api.kiwi.com/locations/query'
TEQUILA_HEADER = {
    'apikey': TEQUILA_API_KEY
}

class FlightSearch:
    def __init__(self):
        pass

    def get_iata_code(self, city):

        response = requests.get(f'{TEQUILA_URL}?term={city}', headers=TEQUILA_HEADER)
        data = response.json()
        iata_code = data['locations'][0]['code']

        return iata_code