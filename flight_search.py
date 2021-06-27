import requests
from keys.keys import TEQUILA_API_KEY

TEQUILA_URL = 'https://tequila-api.kiwi.com/locations/query'
TEQUILA_SEARCH_URL = 'https://tequila-api.kiwi.com/v2/search'
TEQUILA_HEADER = {
    'apikey': TEQUILA_API_KEY
}

class FlightSearch:
    def get_iata_code(self, city):

        response = requests.get(f'{TEQUILA_URL}?term={city}', headers=TEQUILA_HEADER)
        data = response.json()
        iata_code = data['locations'][0]['code']

        return iata_code

    def search_flights(self): 
        query = {
            'fly_from': 'AKL',
            'fly_to': 'MEL',
            'date_from': '27/06/2021',
            'date_to': '27/12/2021',
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "NZD"
        }

        response = requests.get(
            TEQUILA_SEARCH_URL, 
            params=query, 
            headers=TEQUILA_HEADER
        )

        data = response.json()['data'][0]
        print(data['price'])