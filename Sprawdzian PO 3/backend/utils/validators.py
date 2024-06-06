def validate_temperature(temperature):
    if temperature < -50 or temperature > 50:
        raise ValueError("Temperature must be between -50 and 50 degrees Celsius")

def validate_humidity(humidity):
    if humidity < 0 or humidity > 100:
        raise ValueError("Humidity must be between 0 and 100%")

def validate_pressure(pressure):
    if pressure < 800 or pressure > 1200:
        raise ValueError("Pressure must be between 800 and 1200 hPa")
