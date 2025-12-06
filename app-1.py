import requests # Biblioteka do odpytywania API i pobierania kodu ze stron internetowych
from unidecode import unidecode

API_KEY = "59fb1bba7ba542eb96f81336250612" # string z kluczem
city = input("Podaj miasto, dla którego chcesz sprawdzić pogodę") # Pobieramy od użytkownika miasto
city_uni = unidecode(city)
user_choice = 0
# Dopóki użytkownik nie podał 1,2,3 lub 4, pytamy jeszcze raz
while user_choice not in [1,2,3,4]:
    user_choice = int(input(f'Wybierz co chcesz wyświetlić dla {city}'
                    f'\n1) Temperatura'
                    f'\n2) Ciśnienie'
                    f'\n3) Wilgotność'
                    f'\n4) Wszystkie informacje pogodowe'))

url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city_uni}&aqi=yes"

# Obsługa błędów
try:
    response = requests.get(url) # Pobierz dane
    response = response.json() # Pobierz format json

    if user_choice == 1:
        temp_c = response['current']['temp_c']
        if temp_c < 5:
            emoji = "❄️"
        elif temp_c < 20:
            emoji = "🌫️"
        else:
            emoji = "🌞"
        print(f"Temperatura dla miasta {city} wynosi {temp_c} C {emoji}")
    elif user_choice == 2:
        print(f"Ciśnienie dla miasta {city} wynosi {response['current']['pressure_mb']} hPa")
    elif user_choice == 3:
        print(f"Wilgotność dla miasta {city} wynosi {response['current']['humidity']} %")
    elif user_choice == 4:
        temp_c = response['current']['temp_c']
        if temp_c < 5:
            emoji = "❄️"
        elif temp_c < 20:
            emoji = "🌫️"
        else:
            emoji = "🌞"
        print(f"Temperatura dla miasta {city} wynosi {temp_c} C {emoji}")
        print(f"Ciśnienie dla miasta {city} wynosi {response['current']['pressure_mb']} hPa")
        print(f"Wilgotność dla miasta {city} wynosi {response['current']['humidity']} %")
        if response['current']['condition']['text'] == 'Sunny':
            print(f"Warunki pogodowe dla {city}: Słonecznie")
        else:
            print(f"Warunki pogodowe dla {city}: Nie jest słonecznie")
        print(f"Stężenie pyłów PM10: {response['current']['air_quality']['pm10']}")
    else:
        print("Podaj prawidłową liczbę")
# Na wypadek błędów
except:
    print("Nie znaleziono lokalizacji")

# Chcemy dodać zmianę emotek w zależności od temperatury
# np temp <5 -> śnieżynka
# 5-20 -> chmurka
# powyżej 20 -> słońce