"""Flask application for the Smart Home Weather Dashboard Author: S275931."""
from sys import api_version

from flask import Flask, render_template, jsonify
import os
import hashlib, requests, time, hmac

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():  # put application's code here
    api_key = 'e9acjapvjih3rpbcnjnj8c8kfsnyivkb'
    api_secret = 'p9ltsbyvv137bkskvuerqfs7s8qbe8gy'
    station_id = 142820

    # current time
    local_time = int(time.time())

    # api signature
    data_to_sign = f"api-key{api_key}station-id{station_id}t{local_time}"
    signature = hmac.new(
        api_secret.encode('utf-8'),
        data_to_sign.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

    url = f"https://api.weatherlink.com/v2/current/{station_id}"
    params = {
        "api-key": api_key,
        "t": local_time,
        "api-signature": signature
    }

    response = requests.get(url, params=params)
    current_weather = response.json()
    sensors = current_weather['sensors']
    sensors = sensors[2]
    sensorData = sensors['data']
    sensorData = sensorData[0]
    temperatureFarenheit = sensorData['temp']
    print("Temperature Farenheit", temperatureFarenheit)
    temperatureCelsius = (temperatureFarenheit - 32) * 5.0 / 9.0
    temperatureCelsius1 = round(temperatureCelsius, 1)  # round to 1 decimal place
    print("Temperature Celsius", temperatureCelsius1)
    strTemperatureCelsius1 = str(temperatureCelsius1) + "°C"
    print("Temperature Celsius String", strTemperatureCelsius1)
    strTemperatureFarenheit = str(temperatureFarenheit) + "°F"
    print("Temperature Farenheit String", strTemperatureFarenheit)
    current_weather = response.json()
    sensors = current_weather['sensors']
    sensors = sensors[4]
    sensorData = sensors['data']
    sensorData = sensorData[0]
    temperatureFarenheit = sensorData['temp']
    print("Temperature Farenheit", temperatureFarenheit)
    temperatureCelsius = (temperatureFarenheit - 32) * 5.0 / 9.0
    temperatureCelsius2 = round(temperatureCelsius, 1)  # round to 1 decimal place
    print("Temperature Celsius", temperatureCelsius2)
    strTemperatureCelsius2 = str(temperatureCelsius2) + "°C"
    print("Temperature Celsius String", strTemperatureCelsius2)
    strTemperatureFarenheit = str(temperatureFarenheit) + "°F"
    print("Temperature Farenheit String", strTemperatureFarenheit)

    averageTemperature = (temperatureCelsius1 + temperatureCelsius2) / 2
    averageTemperature = round(averageTemperature, 1)
    strAverageTemperature = str(averageTemperature) + "°C"

    response = requests.get(url, params=params)
    current_weather = response.json()
    sensors = current_weather['sensors']
    sensors = sensors[2]
    sensorData = sensors['data']
    sensorData = sensorData[0]
    humidity1 = sensorData['hum']
    print("Temperature Farenheit", humidity1)
    strHumidity1 = str(humidity1) + "%"
    print("Humidity String", strHumidity1)
    current_weather = response.json()
    sensors = current_weather['sensors']
    sensors = sensors[4]
    sensorData = sensors['data']
    sensorData = sensorData[0]
    humidity2 = sensorData['hum']
    print("Humidity", humidity2)
    strHumidity2 = str(humidity2) + "%"
    print("Humidity String", strHumidity2)

    averageHumidity = (humidity1 + humidity2) / 2
    averageHumidity = round(averageHumidity, 1)
    strAverageHumidity = str(averageHumidity) + "%"

    data = strAverageTemperature, strAverageHumidity
    print("Data", data)
    return render_template('index.html', data=data)

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    api_key = 'e9acjapvjih3rpbcnjnj8c8kfsnyivkb'
    api_secret = 'p9ltsbyvv137bkskvuerqfs7s8qbe8gy'
    station_id = 142820

    # current time
    local_time = int(time.time())

    # api signature
    data_to_sign = f"api-key{api_key}station-id{station_id}t{local_time}"
    signature = hmac.new(
        api_secret.encode('utf-8'),
        data_to_sign.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

    url = f"https://api.weatherlink.com/v2/current/{station_id}"
    params = {
        "api-key": api_key,
        "t": local_time,
        "api-signature": signature
    }

    response = requests.get(url, params=params)
    current_weather = response.json()
    sensors = current_weather['sensors']
    sensors = sensors[2]
    sensorData = sensors['data']
    sensorData = sensorData[0]
    temperatureFarenheit = sensorData['temp']
    print("Temperature Farenheit", temperatureFarenheit)
    temperatureCelsius = (temperatureFarenheit - 32) * 5.0/9.0
    temperatureCelsius1 = round(temperatureCelsius, 1) # round to 1 decimal place
    print("Temperature Celsius", temperatureCelsius1)
    strTemperatureCelsius1 = str(temperatureCelsius1) + "°C"
    print("Temperature Celsius String", strTemperatureCelsius1)
    strTemperatureFarenheit = str(temperatureFarenheit) + "°F"
    print("Temperature Farenheit String", strTemperatureFarenheit)
    current_weather = response.json()
    sensors = current_weather['sensors']
    sensors = sensors[4]
    sensorData = sensors['data']
    sensorData = sensorData[0]
    temperatureFarenheit = sensorData['temp']
    print("Temperature Farenheit", temperatureFarenheit)
    temperatureCelsius = (temperatureFarenheit - 32) * 5.0 / 9.0
    temperatureCelsius2 = round(temperatureCelsius, 1)  # round to 1 decimal place
    print("Temperature Celsius", temperatureCelsius2)
    strTemperatureCelsius2 = str(temperatureCelsius2) + "°C"
    print("Temperature Celsius String", strTemperatureCelsius2)
    strTemperatureFarenheit = str(temperatureFarenheit) + "°F"
    print("Temperature Farenheit String", strTemperatureFarenheit)

    averageTemperature = (temperatureCelsius1 + temperatureCelsius2) / 2
    averageTemperature = round(averageTemperature, 1)
    strAverageTemperature = str(averageTemperature) + "°C"

    data=strTemperatureCelsius1, strTemperatureCelsius2, strAverageTemperature
    print("Data", data)

    return render_template('temperature.html', data=data)

@app.route('/humidity', methods=['GET', 'POST'])
def humidity():
    api_key = 'e9acjapvjih3rpbcnjnj8c8kfsnyivkb'
    api_secret = 'p9ltsbyvv137bkskvuerqfs7s8qbe8gy'
    station_id = 142820

    # current time
    local_time = int(time.time())

    # api signature
    data_to_sign = f"api-key{api_key}station-id{station_id}t{local_time}"
    signature = hmac.new(
        api_secret.encode('utf-8'),
        data_to_sign.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

    url = f"https://api.weatherlink.com/v2/current/{station_id}"
    params = {
        "api-key": api_key,
        "t": local_time,
        "api-signature": signature
    }

    response = requests.get(url, params=params)
    current_weather = response.json()
    sensors = current_weather['sensors']
    sensors = sensors[2]
    sensorData = sensors['data']
    sensorData = sensorData[0]
    humidity1 = sensorData['hum']
    print("Temperature Farenheit", humidity1)
    strHumidity1 = str(humidity1) + "%"
    print("Humidity String", strHumidity1)
    current_weather = response.json()
    sensors = current_weather['sensors']
    sensors = sensors[4]
    sensorData = sensors['data']
    sensorData = sensorData[0]
    humidity2 = sensorData['hum']
    print("Humidity", humidity2)
    strHumidity2 = str(humidity2) + "%"
    print("Humidity String", strHumidity2)


    averageHumidity = (humidity1 + humidity2) / 2
    averageHumidity = round(averageHumidity, 1)
    strAverageHumidity = str(averageHumidity) + "%"

    data = strHumidity1, strHumidity2, strAverageHumidity
    print("Data", data)

    return render_template('humidity.html', data=data)

@app.route('/weathermaps')
def weathermaps():
    return render_template('weathermaps.html')

@app.route('/clocktest')
def clocktest():
    return render_template('clocktest.html')

@app.route('/calendartest')
def calendartest():
    return render_template('calendartest.html')

@app.route('/tabletest1')
def tabletest():
    return render_template('tabletest1.html')

@app.route('/graphtest1')
def graphtest():
    return render_template('graphtest1.html')

@app.route('/weatherdatatest')
def weatherdatatest():
    api_key = 'e9acjapvjih3rpbcnjnj8c8kfsnyivkb'
    api_secret = 'p9ltsbyvv137bkskvuerqfs7s8qbe8gy'
    station_id = 142820

    # current time
    local_time = int(time.time())

    # api signature
    data_to_sign = f"api-key{api_key}station-id{station_id}t{local_time}"
    signature = hmac.new(
        api_secret.encode('utf-8'),
        data_to_sign.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

    url = f"https://api.weatherlink.com/v2/current/{station_id}"
    params = {
        "api-key": api_key,
        "t": local_time,
        "api-signature": signature
    }

    response = requests.get(url, params=params)
    current_weather = response.json()
    print(current_weather)

    return render_template('weatherdatatest.html', data=current_weather)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # port number
    app.run(debug=True, host='0.0.0.0', port=port)  # run the application
