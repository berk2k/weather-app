import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# API anahtarını oku
api_key = os.getenv("WEATHER_API_KEY")

