import requests

API_KEY="59fb1bba7ba542eb96f81336250612"
city = input("Wybierz miasto: ")

url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=yes"

response= requests.get(url)
response = response.json()

print(f"Temperatura dla miasta {city} wynosi {response['current']['temp_c']} C")
print(f"Ciśnienie dla miasta {city} wynosi {response['current']['pressure_mb']} hPa")
print(f"Wilgotność dla miasta {city} wynosi {response['current']['humidity']} %")

if response['current']['condition']['text'] == 'Sunny':
    print(f"Warunki pogodowe dla {city}: Słonecznie")
else:
    print(f"Warunki pogodowe dla {city}: Nie jest słonecznie")