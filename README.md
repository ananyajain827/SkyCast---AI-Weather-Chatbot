# 🌤️ SkyCast - AI Weather Chatbot

SkyCast is an AI-powered weather chatbot that provides real-time weather updates for any city worldwide. Just type in a city name, and SkyCast will fetch the latest weather details instantly! 🌍☀️🌧️
Whether you're planning a trip or just curious about the weather, SkyCast has you covered! ☀️🌧️🌪️

## 🚀 Features
- 🌡️ Get real-time temperature updates
- 🌤️ Weather conditions & descriptions
- 💧 Humidity levels
- 🌬️ Wind speed information
- 📍 Supports city-based queries
- 🖥️ Interactive chat-based UI

## 🛠️ Tech Stack
- 🔥 **Flask** (Backend)
- 🎨 **HTML, CSS, JavaScript** (Frontend)
- 🌍 **OpenWeather API** (Weather Data)
- ⚡ **Fetch API** (Handling requests)
- 🔍 re (Regex Library) (Extracting city names from user input)

## 📂 Project Structure
```
📦 SkyCast
├── 📄 app.py           # Flask backend
├── 📄 requirements.txt # Dependencies
├── 📂 templates
│   └── 📄 index.html   # Frontend UI
└── 📂 static           # (Optional) for styles or scripts
```

## 🛠️ Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/skycast-weather-chatbot.git
   cd skycast-weather-chatbot
   ```
2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**
   ```bash
   python app.py
   ```
5. **Open in your browser**
   - Go to `http://127.0.0.1:5000/`

## 🔑 API Key Setup
SkyCast uses the **OpenWeather API**. Get your API key from [OpenWeather](https://openweathermap.org/api) and replace the `API_KEY` in `app.py`:
```python
API_KEY = "your_api_key_here"
```

## 🎥 Demo
![Screenshot 2025-03-29 231639](https://github.com/user-attachments/assets/0874bba8-2942-4dc5-8906-7789effc08bd)

## 💡 Future Improvements
- 🌍 Add multi-language support
- 📅 3-day weather forecast feature
- 🌌 Dark mode UI
- 📌 Location-based automatic weather detection

## 🤝 Contributing
Pull requests are welcome! Feel free to fork the repo, create a new branch, and submit a PR. 😊

## 📜 License
This project is licensed under the MIT License.

---
Made with ❤️ by [ananya](https://github.com/ananyajain827) 🚀

