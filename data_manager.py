import requests
from flight_data import FlightData

class DataManager:
    def __init__(self):
        self.flight_data = FlightData()

    def UpdateIataCode(self, data):

        response = requests.put(url=f"{self.flight_data.sheety_url}/2", json=data, headers=self.flight_data.sheety_header)
        print(response.text)
        # for item in data['flight']:
        #     print(item)
        #     response = requests.put(url=f"{self.flight_data.sheety_url}/{item['id']}", json=data, headers=self.flight_data.sheety_header)
        #     print(response.text)