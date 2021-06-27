from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()

# sheety_data = data_manager.get_flight_data()

# if sheety_data[0]['iataCode'] == '':
#     flight_search = FlightSearch()
#     for row in sheety_data:
#         row['iataCode'] = flight_search.get_iata_code(row['city'])

# data_manager.destination_data = sheety_data
# data_manager.update_iata_code()

flight_search = FlightSearch()
flight_search.search_flights()

