from backend.models.air_quality_model import AirQualityData
from backend.utils.validators import validate_temperature, validate_humidity, validate_pressure
from datetime import datetime

class AirQualityService:
    def __init__(self):
        self.data_store = []

    def add_air_quality_data(self, data):
        timestamp = datetime.fromisoformat(data['timestamp'])
        temperature = data['temperature']
        humidity = data['humidity']
        pressure = data['pressure']
        pollution_level = data['pollution_level']

        validate_temperature(temperature)
        validate_humidity(humidity)
        validate_pressure(pressure)

        air_quality_data = AirQualityData(timestamp, temperature, humidity, pressure, pollution_level)
        self.data_store.append(air_quality_data)

    def get_nearest_air_quality_data(self, timestamp_str):
        if not self.data_store:
            return None
        timestamp = datetime.fromisoformat(timestamp_str)
        nearest_data = min(self.data_store, key=lambda x: abs(x.timestamp - timestamp))
        return {
            'timestamp': nearest_data.timestamp.isoformat(),
            'temperature': nearest_data.temperature,
            'humidity': nearest_data.humidity,
            'pressure': nearest_data.pressure,
            'pollution_level': nearest_data.pollution_level
        }
