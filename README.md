# DHT22 Live Sensor Dashboard

A Raspberry Pi project that reads temperature and humidity from a **DHT22 sensor** and displays live charts in a web browser using Flask and CanvasJS.

---

## 📁 Project Structure

```
dht22-dashboard/
├── sensor.py                  # Reads DHT22 sensor, writes JSON data files
├── requirements.txt           # Python dependencies
├── .gitignore
└── webapp/
    ├── flask_server.py        # Flask web server
    ├── templates/
    │   └── index.html         # Live chart dashboard
    ├── static/
    │   └── js/
    │       └── canvasjs.min.js  # ← You must add this (see setup below)
    └── data/
        ├── humidity.json      # Auto-generated at runtime
        └── temperature.json   # Auto-generated at runtime
```

---

## 🔧 Hardware Requirements

- Raspberry Pi (any model with GPIO)
- DHT22 temperature & humidity sensor
- 10kΩ pull-up resistor between VCC and DATA
- Wiring: DATA pin → GPIO 4 (board.D4)

---

## 🚀 Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/dht22-dashboard.git
cd dht22-dashboard
```

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3. Add CanvasJS
Download `canvasjs.min.js` from [canvasjs.com](https://canvasjs.com) and place it at:
```
webapp/static/js/canvasjs.min.js
```

### 4. Run the sensor script (Terminal 1)
```bash
python sensor.py
```

### 5. Run the Flask web server (Terminal 2)
```bash
cd webapp
python flask_server.py
```

### 6. Open the dashboard
Visit `http://<raspberry-pi-ip>:5000` in your browser.  
The charts auto-refresh every **5 seconds**.

---

## 📊 How It Works

| Component | Role |
|---|---|
| `sensor.py` | Polls DHT22 every 3s, appends readings to JSON files |
| `flask_server.py` | Serves the web app and exposes JSON data via `/data/` |
| `index.html` | Fetches JSON and renders live line charts with CanvasJS |

---

## 📝 Notes

- `humidity.json` and `temperature.json` are generated at runtime and excluded from git.
- The sensor occasionally produces read errors — these are normal for DHT sensors and are safely retried.
- For production use, consider running both scripts as `systemd` services.
