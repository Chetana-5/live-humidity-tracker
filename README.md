# 🌡️ Live Humidity & Temperature Tracker

> Real-time temperature and humidity monitoring using DHT22 sensor and Raspberry Pi, visualized in a web dashboard.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-GPIO-red?logo=raspberrypi)
---

## ✨ Features
- 📡 Reads live data from DHT22 sensor every 3 seconds
- 📊 Displays real-time temperature & humidity charts
- 🌐 Accessible from any device on the local network
- 🔄 Auto-refreshes every 5 seconds

---

## 🔧 Hardware Required
- Raspberry Pi (any model)
- DHT22 Sensor
- 10kΩ resistor
- Jumper wires

---

## 🚀 Installation
```
git clone https://github.com/Chetana-5/live-humidity-tracker.git
cd live-humidity-tracker
pip install -r requirements.txt
```

## ▶️ Usage
```
# Terminal 1 — Start sensor
python sensor.py

# Terminal 2 — Start web server
cd webapp
python flask_server.py
```

Then open `http://<raspberry-pi-ip>:5000` in your browser.

---

## 📁 Project Structure
```
live-humidity-tracker/
├── sensor.py
├── requirements.txt
└── webapp/
    ├── flask_server.py
    ├── templates/index.html
    ├── static/js/
    └── data/
```

---

## 👩‍💻 Author
**Chetana Srinivas** — [GitHub](https://github.com/Chetana-5)