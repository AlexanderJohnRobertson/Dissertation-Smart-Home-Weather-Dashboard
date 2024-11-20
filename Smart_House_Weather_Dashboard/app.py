"""Flask application for the Smart Home Weather Dashboard Author: S275931."""
import json
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
    temperatureCelsius = round(temperatureCelsius, 1)  # round to 1 decimal place
    print("Temperature Celsius", temperatureCelsius)
    strTemperatureCelsius = str(temperatureCelsius) + "°C"
    print("Temperature Celsius String", strTemperatureCelsius)
    strTemperatureFarenheit = str(temperatureFarenheit) + "°F"
    print("Temperature Farenheit String", strTemperatureFarenheit)



    response = requests.get(url, params=params)
    current_weather = response.json()
    sensors = current_weather['sensors']
    sensors = sensors[2]
    sensorData = sensors['data']
    sensorData = sensorData[0]
    humidity = sensorData['hum']
    print("Temperature Farenheit", humidity)
    strHumidity = str(humidity) + "%"
    print("Humidity String", strHumidity)


    data = strTemperatureCelsius, strHumidity, strTemperatureFarenheit
    print("Data", data)
    return render_template('index.html', data=data)

@app.route('/weather', methods=['GET', 'POST'])
def weather():
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

    sensors = current_weather['sensors']
    sensors = sensors[2]
    sensorData = sensors['data']
    sensorData = sensorData[0]
    humidity = sensorData['hum']
    humidity = int(humidity)
    print("Humidity ", humidity)
    strHumidity = str(humidity) + "%"
    print("Humidity String", strHumidity)

    sensors = current_weather['sensors']
    sensors = sensors[4]
    sensorData = sensors['data']
    sensorData = sensorData[0]
    aqi = sensorData['aqi_val']
    print("AQI ", aqi)
    aqi_description = sensorData['aqi_desc']
    print("AQI Description", aqi_description)
    aqi = int(aqi)

    if aqi == 0:
        aqi_percentage ="0%"
        aqi_colour = "#00FF00"
    elif aqi== 1:
        aqi_percentage = "10%"
        aqi_colour = "#7aff00"
    elif aqi == 2:
        aqi_percentage = "20%"
        aqi_colour = "#a1ff00"
    elif aqi == 3:
        aqi_percentage = "30%"
        aqi_colour = "#c7ff00"
    elif aqi == 4:
        aqi_percentage = "40%"
        aqi_colour = "#faff00"
    elif aqi == 5:
        aqi_percentage = "50%"
        aqi_colour = "#ffea00"
    elif aqi == 6:
        aqi_percentage = "60%"
        aqi_colour = "#ffc400"
    elif aqi == 7:
        aqi_percentage = "70%"
        aqi_colour = "#ff9100"
    elif aqi == 8:
        aqi_percentage = "80%"
        aqi_colour = "#ff5e00"
    elif aqi == 9:
        aqi_percentage = "90%"
        aqi_colour = "#ff3700"
    elif aqi == 10:
        aqi_percentage = "100%"
        aqi_colour = "#ff0000"


    sensors = current_weather['sensors']
    sensors = sensors[2]
    sensorData = sensors['data']
    sensorData = sensorData[0]
    windSpeed = sensorData['wind_speed_last']
    windSpeedKMH = windSpeed * 1.60934
    windSpeedKMH = round(windSpeedKMH, 1)
    windSpeedKMH = int(windSpeedKMH)
    print("Wind Speed ", windSpeed)
    print("Wind Speed KMH", windSpeedKMH)
    strWindSpeed = str(windSpeed) + " mph"
    strWindSpeedKMH = str(windSpeedKMH) + " km/h"

    sensors = current_weather['sensors']
    sensors = sensors[2]
    sensorData = sensors['data']
    sensorData = sensorData[0]
    windDirection = sensorData['wind_dir_last']
    print("Wind Direction ", windDirection)
    if windDirection >=0 and windDirection < 22.5 or windDirection >= 337.5 and windDirection <= 360:
        windDirectionDescription = "North"
        compass = "/static/images/compassNorth.svg"
    elif windDirection >= 22.5 and windDirection < 67.5:
        windDirectionDescription = "North East"
        compass = "/static/images/compassNorthEast.svg"
    elif windDirection >= 67.5 and windDirection < 112.5:
        windDirectionDescription = "East"
        compass = "/static/images/compassEast.svg"
    elif windDirection >= 112.5 and windDirection < 157.5:
        windDirectionDescription = "South East"
        compass = "/static/images/compassSouthEast.svg"
    elif windDirection >= 157.5 and windDirection < 202.5:
        windDirectionDescription = "South"
        compass = "/static/images/compassSouth.svg"
    elif windDirection >= 202.5 and windDirection < 247.5:
        windDirectionDescription = "South West"
        compass = "/static/images/compassSouthWest.svg"
    elif windDirection >= 247.5 and windDirection < 292.5:
        windDirectionDescription = "West"
        compass = "/static/images/compassWest.svg"
    elif windDirection >= 292.5 and windDirection < 337.5:
        windDirectionDescription = "North West"
        compass = "/static/images/compassNorthWest.svg"

    print("Wind Direction Description", windDirectionDescription)

    sensors = current_weather['sensors']
    sensors = sensors[2]
    sensorData = sensors['data']
    sensorData = sensorData[0]
    UV_index= sensorData['uv_index']
    print("UV Index", UV_index)
    if UV_index <= 2:
        UV_index_description = " Low"
    elif UV_index >= 3 and UV_index <= 5:
        UV_index_description = " Moderate"
    elif UV_index >= 6 and UV_index <= 7:
        UV_index_description = " High"
    elif UV_index >= 8 and UV_index <= 10:
        UV_index_description = " Very High"

    UV_index = int(UV_index)

    if UV_index == 0:
        UV_index_percentage ="0%"
        UV_index_colour = "#00FF00"
    elif UV_index == 1:
        UV_index_percentage = "10%"
        UV_index_colour = "#7aff00"
    elif UV_index == 2:
        UV_index_percentage = "20%"
        UV_index_colour = "#a1ff00"
    elif UV_index == 3:
        UV_index_percentage = "30%"
        UV_index_colour = "#c7ff00"
    elif UV_index == 4:
        UV_index_percentage = "40%"
        UV_index_colour = "#faff00"
    elif UV_index == 5:
        UV_index_percentage = "50%"
        UV_index_colour = "#ffea00"
    elif UV_index == 6:
        UV_index_percentage = "60%"
        UV_index_colour = "#ffc400"
    elif UV_index == 7:
        UV_index_percentage = "70%"
        UV_index_colour = "#ff9100"
    elif UV_index == 8:
        UV_index_percentage = "80%"
        UV_index_colour = "#ff5e00"
    elif UV_index == 9:
        UV_index_percentage = "90%"
        UV_index_colour = "#ff3700"
    elif UV_index == 10:
        UV_index_percentage = "100%"
        UV_index_colour = "#ff0000"


    print("UV Index Description", UV_index_description)
    print("UV Index", UV_index)
    print("UV Index Percentage", UV_index_percentage)
    print("UV Index Colour", UV_index_colour)
    print("AQI Percentage", aqi_percentage)


    data = strTemperatureCelsius1, strHumidity, aqi, aqi_description, strWindSpeed, windDirectionDescription, UV_index, UV_index_description, UV_index_percentage, UV_index_colour, aqi_percentage, aqi_colour, compass, strTemperatureFarenheit, strWindSpeedKMH
    print("Data", data)

    return render_template('weather.html', data=data)

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
    temperatureFarenheit1 = sensorData['temp']
    print("Temperature Farenheit", temperatureFarenheit1)
    temperatureCelsius = (temperatureFarenheit1 - 32) * 5.0/9.0
    temperatureCelsius1 = round(temperatureCelsius, 1) # round to 1 decimal place
    print("Temperature Celsius", temperatureCelsius1)
    strTemperatureCelsius1 = str(temperatureCelsius1) + "°C"
    print("Temperature Celsius String", strTemperatureCelsius1)
    strTemperatureFarenheit1 = str(temperatureFarenheit1) + "°F"
    print("Temperature Farenheit String", strTemperatureFarenheit1)
    current_weather = response.json()
    sensors = current_weather['sensors']
    sensors = sensors[4]
    sensorData = sensors['data']
    sensorData = sensorData[0]
    temperatureFarenheit2 = sensorData['temp']
    print("Temperature Farenheit", temperatureFarenheit2)
    temperatureCelsius = (temperatureFarenheit2 - 32) * 5.0 / 9.0
    temperatureCelsius2 = round(temperatureCelsius, 1)  # round to 1 decimal place
    print("Temperature Celsius", temperatureCelsius2)
    strTemperatureCelsius2 = str(temperatureCelsius2) + "°C"
    print("Temperature Celsius String", strTemperatureCelsius2)
    strTemperatureFarenheit2 = str(temperatureFarenheit2) + "°F"
    print("Temperature Farenheit String", strTemperatureFarenheit2)


    data=strTemperatureCelsius1, strTemperatureCelsius2, strTemperatureFarenheit1, strTemperatureFarenheit2
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
    print("Humidity ", humidity1)
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

    return jsonify(current_weather)

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/weathertest', methods=['GET', 'POST'])
def weathertest():
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

    sensors = current_weather['sensors']
    sensors = sensors[2]
    sensorData = sensors['data']
    sensorData = sensorData[0]
    humidity = sensorData['hum']
    humidity = int(humidity)
    print("Humidity ", humidity)
    strHumidity = str(humidity) + "%"
    print("Humidity String", strHumidity)

    sensors = current_weather['sensors']
    sensors = sensors[4]
    sensorData = sensors['data']
    sensorData = sensorData[0]
    aqi = sensorData['aqi_val']
    print("AQI ", aqi)
    aqi_description = sensorData['aqi_desc']
    print("AQI Description", aqi_description)
    aqi = int(aqi)

    if aqi == 0:
        aqi_percentage = "0%"
        aqi_colour = "#00FF00"
    elif aqi == 1:
        aqi_percentage = "10%"
        aqi_colour = "#7aff00"
    elif aqi == 2:
        aqi_percentage = "20%"
        aqi_colour = "#a1ff00"
    elif aqi == 3:
        aqi_percentage = "30%"
        aqi_colour = "#c7ff00"
    elif aqi == 4:
        aqi_percentage = "40%"
        aqi_colour = "#faff00"
    elif aqi == 5:
        aqi_percentage = "50%"
        aqi_colour = "#ffea00"
    elif aqi == 6:
        aqi_percentage = "60%"
        aqi_colour = "#ffc400"
    elif aqi == 7:
        aqi_percentage = "70%"
        aqi_colour = "#ff9100"
    elif aqi == 8:
        aqi_percentage = "80%"
        aqi_colour = "#ff5e00"
    elif aqi == 9:
        aqi_percentage = "90%"
        aqi_colour = "#ff3700"
    elif aqi == 10:
        aqi_percentage = "100%"
        aqi_colour = "#ff0000"

    sensors = current_weather['sensors']
    sensors = sensors[2]
    sensorData = sensors['data']
    sensorData = sensorData[0]
    windSpeed = sensorData['wind_speed_last']
    print("Wind Speed ", windSpeed)
    strWindSpeed = str(windSpeed) + " mph"

    sensors = current_weather['sensors']
    sensors = sensors[2]
    sensorData = sensors['data']
    sensorData = sensorData[0]
    windDirection = sensorData['wind_dir_last']
    print("Wind Direction ", windDirection)
    if windDirection >= 0 and windDirection < 22.5 or windDirection >= 337.5 and windDirection <= 360:
        windDirectionDescription = "North"
        compass = "/static/images/compassNorth.svg"
    elif windDirection >= 22.5 and windDirection < 67.5:
        windDirectionDescription = "North East"
        compass = "/static/images/compassNorthEast.svg"
    elif windDirection >= 67.5 and windDirection < 112.5:
        windDirectionDescription = "East"
        compass = "/static/images/compassEast.svg"
    elif windDirection >= 112.5 and windDirection < 157.5:
        windDirectionDescription = "South East"
        compass = "/static/images/compassSouthEast.svg"
    elif windDirection >= 157.5 and windDirection < 202.5:
        windDirectionDescription = "South"
        compass = "/static/images/compassSouth.svg"
    elif windDirection >= 202.5 and windDirection < 247.5:
        windDirectionDescription = "South West"
        compass = "/static/images/compassSouthWest.svg"
    elif windDirection >= 247.5 and windDirection < 292.5:
        windDirectionDescription = "West"
        compass = "/static/images/compassWest.svg"
    elif windDirection >= 292.5 and windDirection < 337.5:
        windDirectionDescription = "North West"
        compass = "/static/images/compassNorthWest.svg"

    print("Wind Direction Description", windDirectionDescription)

    sensors = current_weather['sensors']
    sensors = sensors[2]
    sensorData = sensors['data']
    sensorData = sensorData[0]
    UV_index = sensorData['uv_index']
    print("UV Index", UV_index)
    if UV_index <= 2:
        UV_index_description = " Low"
    elif UV_index >= 3 and UV_index <= 5:
        UV_index_description = " Moderate"
    elif UV_index >= 6 and UV_index <= 7:
        UV_index_description = " High"
    elif UV_index >= 8 and UV_index <= 10:
        UV_index_description = " Very High"

    UV_index = int(UV_index)

    if UV_index == 0:
        UV_index_percentage = "0%"
        UV_index_colour = "#00FF00"
    elif UV_index == 1:
        UV_index_percentage = "10%"
        UV_index_colour = "#7aff00"
    elif UV_index == 2:
        UV_index_percentage = "20%"
        UV_index_colour = "#a1ff00"
    elif UV_index == 3:
        UV_index_percentage = "30%"
        UV_index_colour = "#c7ff00"
    elif UV_index == 4:
        UV_index_percentage = "40%"
        UV_index_colour = "#faff00"
    elif UV_index == 5:
        UV_index_percentage = "50%"
        UV_index_colour = "#ffea00"
    elif UV_index == 6:
        UV_index_percentage = "60%"
        UV_index_colour = "#ffc400"
    elif UV_index == 7:
        UV_index_percentage = "70%"
        UV_index_colour = "#ff9100"
    elif UV_index == 8:
        UV_index_percentage = "80%"
        UV_index_colour = "#ff5e00"
    elif UV_index == 9:
        UV_index_percentage = "90%"
        UV_index_colour = "#ff3700"
    elif UV_index == 10:
        UV_index_percentage = "100%"
        UV_index_colour = "#ff0000"

    print("UV Index Description", UV_index_description)
    print("UV Index", UV_index)
    print("UV Index Percentage", UV_index_percentage)
    print("UV Index Colour", UV_index_colour)
    print("AQI Percentage", aqi_percentage)

    data = strTemperatureCelsius1, strHumidity, aqi, aqi_description, strWindSpeed, windDirectionDescription, UV_index, UV_index_description, UV_index_percentage, UV_index_colour, aqi_percentage, aqi_colour, compass
    print("Data", data)

    return render_template('weathertest.html', data=data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # port number
    app.run(debug=True, host='0.0.0.0', port=port)  # run the application
