from data_manager import DataManager
import requests
from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager

flight_data = FlightData()
sheety_data = flight_data.flight_data
prices = flight_data.prices

new_sheety_data = {}
new_sheety_data['flight'] = sheety_data.pop('flights')

for flight in new_sheety_data['flight']:
    if flight['iataCode'] == '':
        flight['iataCode'] = FlightSearch(flight['city']).testing() 

test_data = {
    'flight': [
            {
            'city': 'London',
            'iataCode': 'TESTING',
            'lowestPrice': 800,
            'id': '2'
        }
    ]
}

print(test_data['flight'])

data_manager = DataManager()
data_manager.UpdateIataCode(test_data)

