import os
import requests


class AirQualityClient:
    def __init__(self, city, station, api_key):
        self.base_url = "https://api.openaq.org/v1/latest"
        self.city = city
        self.station = station
        self.api_key = api_key

    def get_air_quality_data(self):
        params = {'city': self.city, 'location': self.station}
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()


def main():
    CITY = os.getenv('CITY', 'Warsaw')
    STATION = os.getenv('STATION', 'Warsaw-Ursynow')
    API_KEY = os.getenv('API_KEY', '439c0252-16cb-45cb-b61c-75a71e174f98')

    client = AirQualityClient(CITY, STATION, API_KEY)
    air_quality_data = client.get_air_quality_data()
    print(air_quality_data)


if __name__ == "__main__":
    main()
