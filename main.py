from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
import datetime as dt

data_manager = DataManager()

LOCATION = 'AKL'

# sheety_data = data_manager.get_flight_data()

# if sheety_data[0]['iataCode'] == '':
#     flight_search = FlightSearch()
#     for row in sheety_data:
#         row['iataCode'] = flight_search.get_iata_code(row['city'])

# data_manager.destination_data = sheety_data
# data_manager.update_iata_code()

from_date = dt.datetime.now()
to_date = from_date + dt.timedelta(days=180)

from_date = from_date.strftime('%d/%m/%Y')
to_date = to_date.strftime('%d/%m/%Y')

flight_search = FlightSearch()
flight_search.search_flights(from_date, to_date)

