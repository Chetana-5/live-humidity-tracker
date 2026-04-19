import time
import adafruit_dht
import board
import json

dht_device = adafruit_dht.DHT22(board.D4)

humidity_hist = []
temperature_hist = []
i = 0

while True:
    try:
        temperature_c = dht_device.temperature
        temperature_f = temperature_c * (9 / 5) + 32

        humidity = dht_device.humidity

        temperature_hist.append({'x': i, 'y': temperature_c})
        humidity_hist.append({'x': i, 'y': humidity})

        i += 1

        print("Temp:{:.1f} C / {:.1f} F    Humidity: {}%".format(
            temperature_c, temperature_f, humidity))

        with open('webapp/data/humidity.json', 'w') as f:
            json.dump(humidity_hist, f)

        with open('webapp/data/temperature.json', 'w') as f:
            json.dump(temperature_hist, f)

    except RuntimeError as err:
        print(err.args[0])

    except KeyboardInterrupt:
        break

    time.sleep(3)
