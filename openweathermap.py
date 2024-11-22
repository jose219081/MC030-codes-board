import http as req

API_KEY = "56b0fa0dffacca8c03a3f17abc12de2c"  # Substitua pela sua chave de API do OpenWeatherMap
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
POLLUTION_URL = "https://api.openweathermap.org/data/2.5/air_pollution?"

def get_location():
    """Obtém latitude e longitude (simulação para MicroPython)."""
    # Em um dispositivo real, você usaria um módulo GPS ou serviço de localização.
    latitude = -22.9083  # Latitude de Campinas
    longitude = -47.0608 # Longitude de Campinas
    return latitude, longitude

def get_weather_data():
    """Obtém dados climáticos do OpenWeatherMap."""
    lat, lon = get_location()
    complete_url = BASE_URL + "lat={}&lon={}&appid={}".format(lat, lon, API_KEY)
    data = req.http_request(complete_url)
    complete_url = POLLUTION_URL + "lat={}&lon={}&appid={}".format(lat, lon, API_KEY)
    data += req.http_request(complete_url)
    return data