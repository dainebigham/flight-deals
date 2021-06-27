import requests
from flight_data import FlightData
from keys.keys import SHEETY_BEARER_KEY

SHEETY_URL = 'https://api.sheety.co/d8532f7b374806aaec629327e09e1945/flightData/flights'
SHEETY_HEADER = {
    'Authorization': SHEETY_BEARER_KEY
}

class DataManager:
    def __init__(self):
        self.flight_data = FlightData()

    def get_flight_data(self): 
        response = requests.get(SHEETY_URL, headers=SHEETY_HEADER)
        data = response.json()
        self.destination_data = data['flights']

        return self.destination_data

    def update_iata_code(self):

        for city in self.destination_data:
            new_data = {
                'flight': {
                    'iataCode': city['iataCode']
                }
            }

            response = requests.put(
                url=f"{SHEETY_URL}/{city['id']}", 
                json=new_data, 
                headers=SHEETY_HEADER
            )