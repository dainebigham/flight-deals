import requests

class FlightData:
    def __init__(self):
        self.sheety_url = 'https://api.sheety.co/31a86792fd95429388193024970a7b21/flightList/flights'

        self.sheety_header = {
            'Authorization': 'Bearer o7Ms7fMJJ@QKca%C'
        }

        response = requests.get(self.sheety_url, headers=self.sheety_header)
        self.flight_data = response.json()
        
        self.prices = []

        for flight in self.flight_data['flights']:
            self.prices.append(flight['lowestPrice'])