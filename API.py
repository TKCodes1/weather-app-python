import requests

city = input("What city do you want to see the weather for?: ")




long_lat_url = "https://geocoding-api.open-meteo.com/v1/search?name="+ city +"&count=10&language=en&format=json"

response = requests.get(long_lat_url)
long_lat_data = response.json()

if 'results' not in long_lat_data:
    print("City not found")
    quit()

longitude = str(long_lat_data['results'][0]['longitude'])
latitude = str(long_lat_data['results'][0]['latitude'])


api_url = 'https://api.open-meteo.com/v1/forecast?latitude='+ latitude + '&longitude='+ longitude +'&current=temperature_2m,wind_speed_10m,precipitation&wind_speed_unit=mph&temperature_unit=fahrenheit'
response_api = requests.get(api_url)
api_data = response_api.json()

temperature = api_data['current']['temperature_2m']
wind_speed = api_data['current']['wind_speed_10m']
precipitation = api_data['current']['precipitation']

print(f"Weather in {city}: ")
print(f"Temperature: {temperature}°F")
print(f"wind_speed: {wind_speed} MPH")
print(f"precipitation: {precipitation} mm")