import os
from dotenv import load_dotenv
import requests
import json

# .env dosyasını yükle
load_dotenv()

# API anahtarını oku
api_key = os.getenv("WEATHER_API_KEY")

base_url = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city_name):
    # URL'i oluştur
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"

    # API isteği yap
    response = requests.get(complete_url)

    # JSON formatındaki veriyi al
    data = response.json()

    # Hava durumu bilgilerini işleme
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temp = main["temp"]
        humidity = main["humidity"]
        description = weather["description"]

        # Sonuçları yazdır
        print(f"Şehir: {city_name}")
        print(f"Sıcaklık: {temp}°C")
        print(f"Nem: {humidity}%")
        print(f"Hava durumu: {description}")
    else:
        print("Şehir bulunamadı!")

# Şehir ismini kullanıcıdan al
city_name = input("Hava durumu için şehir ismi gir: ")
get_weather(city_name)

