import requests
from unidecode import unidecode

API_KEY="59fb1bba7ba542eb96f81336250612"
city = input("Podaj miasto, dla którego chcesz sprawdzić pogodę ")
city_uni = unidecode(city)
print("Jakie dane chcesz zobaczyć?")
print("1 - Temperatura")
print("2 - Ciśnienie")
print("3 - Wilgotność")
print("4 - Wszystko (temperatura, ciśnienie, wilgotność, opis)")
while True:
    choice = input("Wybierz (1/2/3/4): ")
    if choice in ["1", "2", "3", "4"]:
        break
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city_uni}&aqi=yes"

response= requests.get(url)
response = response.json()

try:
    if choice == "1":
        temp_c = response['current']['temp_c']
        if temp_c < 5:
            emoji = "❄️"
        elif temp_c < 20:
            emoji = "🌫️"
        else:
            emoji = "🌞"
        print(f"Temperatura dla miasta {city} wynosi {temp_c} C {emoji}")

    elif choice == "2":
        print(f"Ciśnienie w {city}: {current['pressure_mb']} hPa")

    elif choice == "3":
        print(f"Wilgotność w {city}: {current['humidity']}%")

    elif choice == "4":
        print(f"Temperatura w {city}: {response['current']['temp_c']} °C {emoji}")    
        print(f"Ciśnienie w {city}: {response['current']['pressure_mb']} hPa")
        print(f"Wilgotność w {city}: {response['current']['humidity']}%")
        print(f"Stężenie pyłów w {city}: {response['current']['air_quality']['pm10']}")
        if response['current']['condition']['text'] == 'Sunny':
            print(f"Warunki pogodowe dla {city}: Słonecznie")
        else:
            print(f"Warunki pogodowe dla {city}: Nie jest słonecznie")
    else:
        print("Nieprawidłowy wybór.")

