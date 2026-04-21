# 🌡️ live-humidity-tracker

A Raspberry Pi project that reads live temperature and humidity data from a DHT22 sensor and displays it as real-time line charts in a browser dashboard powered by Flask and CanvasJS.

---

## 📁 Project Structure

```
live-humidity-tracker/
├── sensor.py                   # Reads DHT22 sensor and writes JSON data files
├── requirements.txt
└── webapp/
    ├── flask_server.py         # Flask web server
    ├── data/                   # JSON data files (auto-generated at runtime)
    │   ├── humidity.json
    │   └── temperature.json
    ├── templates/
    │   └── index.html          # Live chart dashboard (Humidity + Temperature)
    └── static/
        └── js/
            └── canvasjs.min.js # Chart library (download separately — see Setup)
```

---

## 🛠️ Hardware Requirements

- Raspberry Pi (any model with GPIO support)
- DHT22 temperature & humidity sensor
- Sensor data pin connected to **GPIO pin 4 (D4)**

---

## ⚙️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/live-humidity-tracker.git
cd live-humidity-tracker
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

> CanvasJS is not included in this repo due to its license. A free non-commercial license is available on their website.

---

## 🚀 Running the Project

Both scripts need to run **simultaneously** (in separate terminals).

### Terminal 1 — Start the sensor script

```bash
python sensor.py
```

This reads temperature and humidity from the DHT22 every **3 seconds** and writes the data to `webapp/data/humidity.json` and `webapp/data/temperature.json`.

### Terminal 2 — Start the web server

```bash
cd webapp
python flask_server.py
```

Then open your browser at:

```
http://<your-raspberry-pi-ip>:5000
```

---

## 📊 Dashboard

The dashboard displays two live line charts:

| Chart | Data |
|-------|------|
| **Humidity** | Relative humidity (%) over time |
| **Temperature** | Temperature in Celsius (°C) over time |

Charts update on page refresh. For auto-refresh, consider adding a `setInterval` call in `index.html`.

---

## 📦 Dependencies

| Package | Purpose |
|--------|---------|
| `flask` | Web server |
| `adafruit-circuitpython-dht` | DHT22 sensor interface |
| `board` | GPIO pin mapping (part of Blinka) |
| `canvasjs` | Chart rendering (client-side, manual install) |

---

## 📝 Notes

- Temperature is stored and displayed in **Celsius**. To display Fahrenheit, the conversion (`temperature_f`) is already computed in `sensor.py` — just swap the value pushed to `temperature_hist`.
- `webapp/data/*.json` should be added to `.gitignore` as these files are generated at runtime.
- The sensor script keeps the full history in memory and rewrites the JSON files on every reading. A restart clears the history.

---

## 📄 License

MIT
