from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
import datetime as dt

data_manager = DataManager()
flight_search = FlightSearch()

LOCATION = 'AKL'

sheety_data = data_manager.get_flight_data()

if sheety_data[0]['iataCode'] == '':
    flight_search = FlightSearch()
    for row in sheety_data:
        row['iataCode'] = flight_search.get_iata_code(row['city'])

    data_manager.destination_data = sheety_data
    data_manager.update_iata_code()

date_from = dt.datetime.now()
date_to = date_from + dt.timedelta(days=180)
date_from = date_from.strftime('%d/%m/%Y')
date_to = date_to.strftime('%d/%m/%Y')

for destination in sheety_data:
    flight_search.search_flights(
        location = LOCATION,
        destination = destination['iataCode'],
        date_from = date_from, 
        date_to = date_to)

