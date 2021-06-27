from flight_search import TEQUILA_URL
import requests
from keys.keys import TEQUILA_API_KEY

class FlightData:
    def __init__(self):
        self.departure_code = 'AKL'
        self.departure_city = 'Auckland'
        self.price = 0