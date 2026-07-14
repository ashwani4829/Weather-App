# 🌦️ Weather App (CLI)

A simple and beginner-friendly **Python Command Line Interface (CLI)** application that fetches **real-time weather information** for any city using the **OpenWeatherMap API**. The application provides current weather conditions, temperature, humidity, and wind speed in an easy-to-read format.

---

## 🚀 Features

- 🌍 Get real-time weather information
- 🔎 Search weather by city name
- 🌡️ Display temperature in Celsius
- 💧 View humidity percentage
- 🌬️ Check wind speed
- ☁️ Display current weather conditions
- ⚠️ Handles invalid city names gracefully
- 🐍 Beginner-friendly Python project

---

## 🛠️ Technologies Used

- **Python 3**
- **Requests Library**
- **OpenWeatherMap API**
- **JSON Data Handling**

---

## 📁 Project Structure

```text
Weather_App_CLI/
│
├── weather_app.py
├── README.md
└── screenshots/
    └── output.png
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/weather-app-cli.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd weather-app-cli
```

### 3️⃣ Install Dependencies

```bash
pip install requests
```

---

## 🔑 Get Your OpenWeatherMap API Key

1. Create a free account at **OpenWeatherMap**.
2. Generate a new API key.
3. Open the `weather_app.py` file.
4. Replace:

```python
API_KEY = "YOUR_API_KEY_HERE"
```

with your own API key:

```python
API_KEY = "YOUR_ACTUAL_API_KEY"
```

---

## ▶️ Run the Application

```bash
python weather_app.py
```

---

## 💻 Example Usage

### Input

```text
Enter city name: Delhi
```

### Output

```text
===== WEATHER REPORT =====

City: Delhi, IN
Temperature: 35.4 °C
Feels Like: 39.1 °C
Humidity: 62%
Weather: Haze
Wind Speed: 3.5 m/s
```

---

## 📸 Screenshots

Add your program screenshots inside the `screenshots` folder.

Example:

```
screenshots/
│
└── output.png
```

---

## 🔍 How It Works

1. The user enters a city name.
2. The application sends an HTTP request to the OpenWeatherMap API.
3. The API returns weather information in JSON format.
4. The program extracts the required weather details.
5. The weather report is displayed in the terminal.

---

## 📊 Sample JSON Response

```json
{
  "name": "Delhi",
  "main": {
    "temp": 35.4,
    "humidity": 62
  },
  "weather": [
    {
      "description": "haze"
    }
  ]
}
```

---

## 🧠 Concepts Used

- Variables
- User Input
- Functions
- API Integration
- HTTP Requests
- JSON Parsing
- Conditional Statements
- Exception Handling

---

## 🎯 Learning Outcomes

By completing this project, you will learn:

- How REST APIs work
- Making HTTP requests using Python
- Working with JSON data
- Handling user input
- Implementing exception handling
- Building real-world command-line applications

---

## 🧪 Sample Output

```text
Enter city name: Mumbai

===== WEATHER REPORT =====

City: Mumbai, IN
Temperature: 30.2 °C
Feels Like: 34.1 °C
Humidity: 78%
Weather: Scattered Clouds
Wind Speed: 4.2 m/s
```

---

## 🚀 Future Enhancements

- 🌤️ 5-Day Weather Forecast
- 🖼️ Weather Icons
- 📝 Search History
- 🌍 Multiple City Comparison
- 🖥️ GUI Version using Tkinter
- 🎙️ Voice-Based Weather Assistant
- 📍 Detect Current Location Automatically

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Open a Pull Request.

---

## 📜 License

This project is created for educational and learning purposes. Feel free to use and modify it for personal or academic projects.

---

## ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub. It encourages me to build more Python automation and API-based projects.
