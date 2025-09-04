from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY", "demo_key")

@app.route("/")
def home():
    return "Weather App CI/CD is live!"

@app.route("/weather")
def get_weather():
    city = request.args.get("city", "London")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        return jsonify({"error": data.get("message", "Unable to fetch weather")}), 400
    return jsonify({
        "city": city,
        "temperature": data["main"]["temp"],
        "weather": data["weather"][0]["description"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
