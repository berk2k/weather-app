from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import pytz


load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def weather():
    tr_tz = pytz.timezone("Europe/Istanbul")
    tr_time = datetime.now(tr_tz).strftime("%Y-%m-%d %H:%M:%S")  

    if request.method == "POST":
        city = request.form['city']
        api_key = os.getenv("WEATHER_API_KEY") 
        api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(api_url)
        weather_data = response.json()

        if 'coord' in weather_data:
            return render_template("weather.html", data=weather_data, tr_time=tr_time)

    return render_template("weather.html", tr_time=tr_time)


if __name__ == "__main__":
    app.run(debug=True)
