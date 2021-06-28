import requests
from flight_data import FlightData
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

    def search_flights(self, location, destination, date_from, date_to): 
        query = {
            'fly_from': location,
            'fly_to': destination,
            'date_from': date_from,
            'date_to': date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 2,
            "curr": "NZD"
        }

        response = requests.get(
            TEQUILA_SEARCH_URL, 
            params=query, 
            headers=TEQUILA_HEADER
        )

        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"There are no flights to {destination} in the next 6 months")
            return None
        else:
            flight_data = FlightData(
                price=data["price"],
                location=data["route"][0]["cityFrom"],
                location_code=data["route"][0]["flyFrom"],
                destination=data["route"][0]["cityTo"],
                destination_code=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            print(f"{flight_data.destination}: ${flight_data.price}")

            return flight_data