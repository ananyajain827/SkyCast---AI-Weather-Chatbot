from flask import Flask, request, jsonify, render_template
import requests
import re  

app = Flask(__name__)

API_KEY = "your_API"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()
    
    city = extract_city(user_input)
    if city:
        weather_data = get_weather(city)
        return jsonify({"reply": weather_data})
    
    return jsonify({"reply": "Please specify a city name to get the weather report."})

def extract_city(user_input):
    """Extracts the city name using regex from user input."""
    match = re.search(r"in\s+([A-Za-z\s]+)", user_input)
    if match:
        return match.group(1).strip()
    return None

def get_weather(city):
    """Fetches weather data for a given city."""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        return (f"🌡 Temperature: <b>{temp}°C</b><br>"
                f"🌤 Condition: <b>{description.capitalize()}</b><br>"
                f"💧 Humidity: <b>{humidity}%</b><br>"
                f"🌬 Wind Speed: <b>{wind_speed} m/s</b><br>"
                f"📍 Location: <b>{city.title()}</b>")
    else:
        return "❌ Sorry, I couldn't find the weather for that city. Please check the spelling or try another location."

if __name__ == "__main__":
    app.run(debug=True)

