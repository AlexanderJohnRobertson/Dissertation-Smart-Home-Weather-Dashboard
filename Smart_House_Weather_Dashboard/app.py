"""Flask application for the Smart Home Weather Dashboard Author: S275931."""
import json
from sys import api_version

from flask import Flask, render_template, jsonify
import os
import hashlib, requests, time, hmac
from datetime import date
import calendar

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

    openWeather_API_Key = 'cdb2f81a0c0053ff42b1db37fdb0b39b'
    openWeatherID = 2646057
    local_time = int(time.time())
    params = {
        "t": local_time
    }
    openWeatherURL = 'https://api.openweathermap.org/data/2.5/forecast?id=' + str(
        openWeatherID) + '&appid=' + openWeather_API_Key
    response = requests.get(openWeatherURL, params=params)
    openWeatherData = response.json()
    print("openWeatherData", openWeatherData)
    print(type(openWeatherData))
    openWeatherData = openWeatherData['list']
    openWeatherDataToday = openWeatherData[0]
    print(openWeatherDataToday)
    OpenWeatherDataTodayWeather = openWeatherDataToday['weather']
    OpenWeatherDataTodayWeather = OpenWeatherDataTodayWeather[0]
    print(OpenWeatherDataTodayWeather)
    weatherConditionsToday = OpenWeatherDataTodayWeather['main']
    print(weatherConditionsToday)

    if weatherConditionsToday == "Rain":
        weatherConditionsTodayIcon = "/static/images/rain.svg"
    elif weatherConditionsToday == "Clouds":
        weatherConditionsTodayIcon = "/static/images/cloudy.svg"
    elif weatherConditionsToday == "Clear":
        weatherConditionsTodayIcon = "/static/images/sunny.svg"
    elif weatherConditionsToday == "Snow":
        weatherConditionsTodayIcon = "/static/images/snow.svg"
    elif weatherConditionsToday == "Thunderstorm":
        weatherConditionsTodayIcon = "/static/images/thunderstorms.svg"
    elif weatherConditionsToday == "Wind":
        weatherConditionsTodayIcon = "/static/images/wind.svg"
    elif weatherConditionsToday == "Hail":
        weatherConditionsTodayIcon = "/static/images/hailstones.svg"

    temperatureforecastToday = round(temperatureCelsius1, 0)
    temperatureforecastToday = int(temperatureforecastToday)
    temperatureforecastToday = str(temperatureforecastToday) + "°C"

    openWeatherDataTomorrow = openWeatherData[8]
    print(openWeatherDataTomorrow)
    OpenWeatherDataTomorrowWeather = openWeatherDataTomorrow['weather']
    OpenWeatherDataTomorrowWeather = OpenWeatherDataTomorrowWeather[0]
    print(OpenWeatherDataTomorrowWeather)
    weatherConditionsTomorrow = OpenWeatherDataTomorrowWeather['main']
    print(weatherConditionsTomorrow)

    if weatherConditionsTomorrow == "Rain":
        weatherConditionsTomorrowIcon = "/static/images/rain.svg"
    elif weatherConditionsTomorrow == "Clouds":
        weatherConditionsTomorrowIcon = "/static/images/cloudy.svg"
    elif weatherConditionsTomorrow == "Clear":
        weatherConditionsTomorrowIcon = "/static/images/sunny.svg"
    elif weatherConditionsTomorrow == "Snow":
        weatherConditionsTomorrowIcon = "/static/images/snow.svg"
    elif weatherConditionsTomorrow == "Thunderstorm":
        weatherConditionsTomorrowIcon = "/static/images/thunderstorms.svg"
    elif weatherConditionsTomorrow == "Wind":
        weatherConditionsTomorrowIcon = "/static/images/wind.svg"
    elif weatherConditionsTomorrow == "Hail":
        weatherConditionsTomorrowIcon = "/static/images/hailstones.svg"

    temperatureforecastTomorrow = openWeatherDataTomorrow['main']
    temperatureforecastTomorrow = temperatureforecastTomorrow['temp']
    temperatureforecastTomorrow = (temperatureforecastTomorrow - 273.15)
    temperatureforecastTomorrow = round(temperatureforecastTomorrow, 0)
    temperatureforecastTomorrow = int(temperatureforecastTomorrow)
    temperatureforecastTomorrow = str(temperatureforecastTomorrow) + "°C"

    tomorrowDate = openWeatherDataTomorrow['dt_txt']
    tomorrowDate = tomorrowDate.split(" ")
    tomorrowDate = tomorrowDate[0]
    tomorrowDate = date.fromisoformat(tomorrowDate)
    tomorrowDate = calendar.day_name[tomorrowDate.weekday()]
    tomorrowDate = str(tomorrowDate)
    tomorrowDate = tomorrowDate[0:3]
    print(tomorrowDate)

    tomorrowWindSpeed = openWeatherDataTomorrow['wind']
    tomorrowWindSpeed = tomorrowWindSpeed['speed']
    tomorrowWindSpeed = tomorrowWindSpeed / 0.447
    tomorrowWindSpeed = round(tomorrowWindSpeed, 0)
    tomorrowWindSpeed = int(tomorrowWindSpeed)
    tomorrowWindSpeed = str(tomorrowWindSpeed) + "mph"
    print("Tomorrow Wind Speed", tomorrowWindSpeed)

    tomorrowWindDirection = openWeatherDataTomorrow['wind']
    tomorrowWindDirection = tomorrowWindDirection['deg']
    print("Tomorrow Wind Direction", tomorrowWindDirection)
    if tomorrowWindDirection >= 0 and tomorrowWindDirection < 22.5 or tomorrowWindDirection >= 337.5 and tomorrowWindDirection <= 360:
        tomorrowWindDirectionDescription = "North"
    elif tomorrowWindDirection >= 22.5 and tomorrowWindDirection < 67.5:
        tomorrowWindDirectionDescription = "North East"
    elif tomorrowWindDirection >= 67.5 and tomorrowWindDirection < 112.5:
        tomorrowWindDirectionDescription = "East"
    elif tomorrowWindDirection >= 112.5 and tomorrowWindDirection < 157.5:
        tomorrowWindDirectionDescription = "South East"
    elif tomorrowWindDirection >= 157.5 and tomorrowWindDirection < 202.5:
        tomorrowWindDirectionDescription = "South"
    elif tomorrowWindDirection >= 202.5 and tomorrowWindDirection < 247.5:
        tomorrowWindDirectionDescription = "South West"
    elif tomorrowWindDirection >= 247.5 and tomorrowWindDirection < 292.5:
        tomorrowWindDirectionDescription = "West"
    elif tomorrowWindDirection >= 292.5 and tomorrowWindDirection < 337.5:
        tomorrowWindDirectionDescription = "North West"

    tomorrowHumidity = openWeatherDataTomorrow['main']
    tomorrowHumidity = tomorrowHumidity['humidity']
    tomorrowHumidity = str(tomorrowHumidity) + "%"
    print("Tomorrow Humidity", tomorrowHumidity)

    #3Day
    openWeatherDataThreeDay = openWeatherData[16]
    print(openWeatherDataThreeDay)
    OpenWeatherDataThreeDayWeather = openWeatherDataThreeDay['weather']
    OpenWeatherDataThreeDayWeather = OpenWeatherDataThreeDayWeather[0]
    print(OpenWeatherDataThreeDayWeather)
    weatherConditionsThreeDay = OpenWeatherDataThreeDayWeather['main']
    print(weatherConditionsThreeDay)

    if weatherConditionsThreeDay == "Rain":
        weatherConditionsThreeDayIcon = "/static/images/rain.svg"
    elif weatherConditionsThreeDay == "Clouds":
        weatherConditionsThreeDayIcon = "/static/images/cloudy.svg"
    elif weatherConditionsThreeDay == "Clear":
        weatherConditionsThreeDayIcon = "/static/images/sunny.svg"
    elif weatherConditionsThreeDay == "Snow":
        weatherConditionsThreeDayIcon = "/static/images/snow.svg"
    elif weatherConditionsThreeDay == "Thunderstorm":
        weatherConditionsThreeDayIcon = "/static/images/thunderstorms.svg"
    elif weatherConditionsThreeDay == "Wind":
        weatherConditionsThreeDayIcon = "/static/images/wind.svg"
    elif weatherConditionsThreeDay == "Hail":
        weatherConditionsThreeDayIcon = "/static/images/hailstones.svg"

    temperatureforecastThreeDay = openWeatherDataThreeDay['main']
    temperatureforecastThreeDay = temperatureforecastThreeDay['temp']
    temperatureforecastThreeDay = (temperatureforecastThreeDay - 273.15)
    temperatureforecastThreeDay = round(temperatureforecastThreeDay, 0)
    temperatureforecastThreeDay = int(temperatureforecastThreeDay)
    temperatureforecastThreeDay = str(temperatureforecastThreeDay) + "°C"

    ThreeDayDate = openWeatherDataThreeDay['dt_txt']
    ThreeDayDate = ThreeDayDate.split(" ")
    ThreeDayDate = ThreeDayDate[0]
    ThreeDayDate = date.fromisoformat(ThreeDayDate)
    ThreeDayDate = calendar.day_name[ThreeDayDate.weekday()]
    ThreeDayDate = str(ThreeDayDate)
    ThreeDayDate = ThreeDayDate[0:3]
    print(ThreeDayDate)

    ThreeDayWindSpeed = openWeatherDataThreeDay['wind']
    ThreeDayWindSpeed = ThreeDayWindSpeed['speed']
    ThreeDayWindSpeed = ThreeDayWindSpeed / 0.447
    ThreeDayWindSpeed = round(ThreeDayWindSpeed, 0)
    ThreeDayWindSpeed = int(ThreeDayWindSpeed)
    ThreeDayWindSpeed = str(ThreeDayWindSpeed) + "mph"
    print("ThreeDay Wind Speed", ThreeDayWindSpeed)

    ThreeDayWindDirection = openWeatherDataThreeDay['wind']
    ThreeDayWindDirection = ThreeDayWindDirection['deg']
    print("ThreeDay Wind Direction", ThreeDayWindDirection)
    if ThreeDayWindDirection >= 0 and ThreeDayWindDirection < 22.5 or ThreeDayWindDirection >= 337.5 and ThreeDayWindDirection <= 360:
        ThreeDayWindDirectionDescription = "North"
    elif ThreeDayWindDirection >= 22.5 and ThreeDayWindDirection < 67.5:
        ThreeDayWindDirectionDescription = "North East"
    elif ThreeDayWindDirection >= 67.5 and ThreeDayWindDirection < 112.5:
        ThreeDayWindDirectionDescription = "East"
    elif ThreeDayWindDirection >= 112.5 and ThreeDayWindDirection < 157.5:
        ThreeDayWindDirectionDescription = "South East"
    elif ThreeDayWindDirection >= 157.5 and ThreeDayWindDirection < 202.5:
        ThreeDayWindDirectionDescription = "South"
    elif ThreeDayWindDirection >= 202.5 and ThreeDayWindDirection < 247.5:
        tomorrowWindDirectionDescription = "South West"
    elif ThreeDayWindDirection >= 247.5 and ThreeDayWindDirection < 292.5:
        ThreeDayWindDirectionDescription = "West"
    elif ThreeDayWindDirection >= 292.5 and ThreeDayWindDirection < 337.5:
        ThreeDayWindDirectionDescription = "North West"

    ThreeDayHumidity = openWeatherDataThreeDay['main']
    ThreeDayHumidity = ThreeDayHumidity['humidity']
    ThreeDayHumidity = str(ThreeDayHumidity) + "%"
    print("ThreeDay Humidity", ThreeDayHumidity)

    #4 Day
    openWeatherDataFourDay = openWeatherData[24]
    print(openWeatherDataFourDay)
    OpenWeatherDataFourDayWeather = openWeatherDataFourDay['weather']
    OpenWeatherDataFourDayWeather = OpenWeatherDataFourDayWeather[0]
    print(OpenWeatherDataFourDayWeather)
    weatherConditionsFourDay = OpenWeatherDataFourDayWeather['main']
    print(weatherConditionsFourDay)

    if weatherConditionsFourDay == "Rain":
        weatherConditionsFourDayIcon = "/static/images/rain.svg"
    elif weatherConditionsFourDay == "Clouds":
        weatherConditionsFourDayIcon = "/static/images/cloudy.svg"
    elif weatherConditionsFourDay == "Clear":
        weatherConditionsFourDayIcon = "/static/images/sunny.svg"
    elif weatherConditionsFourDay == "Snow":
        weatherConditionsFourDayIcon = "/static/images/snow.svg"
    elif weatherConditionsFourDay == "Thunderstorm":
        weatherConditionsFourDayIcon = "/static/images/thunderstorms.svg"
    elif weatherConditionsFourDay == "Wind":
        weatherConditionsFourDayIcon = "/static/images/wind.svg"
    elif weatherConditionsFourDay == "Hail":
        weatherConditionsFourDayIcon = "/static/images/hailstones.svg"

    temperatureforecastFourDay = openWeatherDataFourDay['main']
    temperatureforecastFourDay = temperatureforecastFourDay['temp']
    temperatureforecastFourDay = (temperatureforecastFourDay - 273.15)
    temperatureforecastFourDay = round(temperatureforecastFourDay, 0)
    temperatureforecastFourDay = int(temperatureforecastFourDay)
    temperatureforecastFourDay = str(temperatureforecastFourDay) + "°C"

    FourDayDate = openWeatherDataFourDay['dt_txt']
    FourDayDate = FourDayDate.split(" ")
    FourDayDate = FourDayDate[0]
    FourDayDate = date.fromisoformat(FourDayDate)
    FourDayDate = calendar.day_name[FourDayDate.weekday()]
    FourDayDate = str(FourDayDate)
    FourDayDate = FourDayDate[0:3]
    print(FourDayDate)

    FourDayWindSpeed = openWeatherDataFourDay['wind']
    FourDayWindSpeed = FourDayWindSpeed['speed']
    FourDayWindSpeed = FourDayWindSpeed / 0.447
    FourDayWindSpeed = round(FourDayWindSpeed, 0)
    FourDayWindSpeed = int(FourDayWindSpeed)
    FourDayWindSpeed = str(FourDayWindSpeed) + "mph"
    print("FourDay Wind Speed", FourDayWindSpeed)

    FourDayWindDirection = openWeatherDataFourDay['wind']
    FourDayWindDirection = FourDayWindDirection['deg']
    print("FourDay Wind Direction", FourDayWindDirection)
    if FourDayWindDirection >= 0 and FourDayWindDirection < 22.5 or FourDayWindDirection >= 337.5 and FourDayWindDirection <= 360:
        FourDayWindDirectionDescription = "North"
    elif FourDayWindDirection >= 22.5 and FourDayWindDirection < 67.5:
        FourDayWindDirectionDescription = "North East"
    elif FourDayWindDirection >= 67.5 and FourDayWindDirection < 112.5:
        FourDayWindDirectionDescription = "East"
    elif FourDayWindDirection >= 112.5 and FourDayWindDirection < 157.5:
        FourDayWindDirectionDescription = "South East"
    elif FourDayWindDirection >= 157.5 and FourDayWindDirection < 202.5:
        FourDayWindDirectionDescription = "South"
    elif FourDayWindDirection >= 202.5 and FourDayWindDirection < 247.5:
        FourDayWindDirectionDescription = "South West"
    elif FourDayWindDirection >= 247.5 and FourDayWindDirection < 292.5:
        FourDayWindDirectionDescription = "West"
    elif FourDayWindDirection >= 292.5 and FourDayWindDirection < 337.5:
        FourDayWindDirectionDescription = "North West"

    FourDayHumidity = openWeatherDataFourDay['main']
    FourDayHumidity = FourDayHumidity['humidity']
    FourDayHumidity = str(FourDayHumidity) + "%"
    print("FourDay Humidity", FourDayHumidity)

    #5 Day
    openWeatherDataFiveDay = openWeatherData[32]
    print(openWeatherDataFiveDay)
    OpenWeatherDataFiveDayWeather = openWeatherDataFiveDay['weather']
    OpenWeatherDataFiveDayWeather = OpenWeatherDataFiveDayWeather[0]
    print(OpenWeatherDataFiveDayWeather)
    weatherConditionsFiveDay = OpenWeatherDataFiveDayWeather['main']
    print(weatherConditionsFiveDay)

    if weatherConditionsFiveDay == "Rain":
        weatherConditionsFiveDayIcon = "/static/images/rain.svg"
    elif weatherConditionsFiveDay == "Clouds":
        weatherConditionsFiveDayIcon = "/static/images/cloudy.svg"
    elif weatherConditionsFiveDay == "Clear":
        weatherConditionsFiveDayIcon = "/static/images/sunny.svg"
    elif weatherConditionsFiveDay == "Snow":
        weatherConditionsFiveDayIcon = "/static/images/snow.svg"
    elif weatherConditionsFiveDay == "Thunderstorm":
        weatherConditionsFiveDayIcon = "/static/images/thunderstorms.svg"
    elif weatherConditionsFiveDay == "Wind":
        weatherConditionsFiveDayIcon = "/static/images/wind.svg"
    elif weatherConditionsFiveDay == "Hail":
        weatherConditionsFiveDayIcon = "/static/images/hailstones.svg"

    temperatureforecastFiveDay = openWeatherDataFiveDay['main']
    temperatureforecastFiveDay = temperatureforecastFiveDay['temp']
    temperatureforecastFiveDay = (temperatureforecastFiveDay - 273.15)
    temperatureforecastFiveDay = round(temperatureforecastFiveDay, 0)
    temperatureforecastFiveDay = int(temperatureforecastFiveDay)
    temperatureforecastFiveDay = str(temperatureforecastFiveDay) + "°C"

    FiveDayDate = openWeatherDataFiveDay['dt_txt']
    FiveDayDate = FiveDayDate.split(" ")
    FiveDayDate = FiveDayDate[0]
    FiveDayDate = date.fromisoformat(FiveDayDate)
    FiveDayDate = calendar.day_name[FiveDayDate.weekday()]
    FiveDayDate = str(FiveDayDate)
    FiveDayDate = FiveDayDate[0:3]
    print(FiveDayDate)

    FiveDayWindSpeed = openWeatherDataFiveDay['wind']
    FiveDayWindSpeed = FiveDayWindSpeed['speed']
    FiveDayWindSpeed = FiveDayWindSpeed / 0.447
    FiveDayWindSpeed = round(FiveDayWindSpeed, 0)
    FiveDayWindSpeed = int(FiveDayWindSpeed)
    FiveDayWindSpeed = str(FiveDayWindSpeed) + "mph"
    print("FiveDay Wind Speed", FiveDayWindSpeed)

    FiveDayWindDirection = openWeatherDataFiveDay['wind']
    FiveDayWindDirection = FiveDayWindDirection['deg']
    print("FiveDay Wind Direction", FiveDayWindDirection)
    if FiveDayWindDirection >= 0 and FiveDayWindDirection < 22.5 or FiveDayWindDirection >= 337.5 and FiveDayWindDirection <= 360:
        FiveDayWindDirectionDescription = "North"
    elif FiveDayWindDirection >= 22.5 and FiveDayWindDirection < 67.5:
        FiveDayWindDirectionDescription = "North East"
    elif FiveDayWindDirection >= 67.5 and FiveDayWindDirection < 112.5:
        FiveDayWindDirectionDescription = "East"
    elif FiveDayWindDirection >= 112.5 and FiveDayWindDirection < 157.5:
        FiveDayWindDirectionDescription = "South East"
    elif FiveDayWindDirection >= 157.5 and FiveDayWindDirection < 202.5:
        FiveDayWindDirectionDescription = "South"
    elif FiveDayWindDirection >= 202.5 and FiveDayWindDirection < 247.5:
        FiveDayWindDirectionDescription = "South West"
    elif FiveDayWindDirection >= 247.5 and FiveDayWindDirection < 292.5:
        FiveDayWindDirectionDescription = "West"
    elif FiveDayWindDirection >= 292.5 and FiveDayWindDirection < 337.5:
        FiveDayWindDirectionDescription = "North West"

    FiveDayHumidity = openWeatherDataFiveDay['main']
    FiveDayHumidity = FiveDayHumidity['humidity']
    FiveDayHumidity = str(FiveDayHumidity) + "%"
    print("FiveDay Humidity", FiveDayHumidity)

    #6 Day
    openWeatherDataSixDay = openWeatherData[39]
    print(openWeatherDataSixDay)
    OpenWeatherDataSixDayWeather = openWeatherDataSixDay['weather']
    OpenWeatherDataSixDayWeather = OpenWeatherDataSixDayWeather[0]
    print(OpenWeatherDataSixDayWeather)
    weatherConditionsSixDay = OpenWeatherDataSixDayWeather['main']
    print(weatherConditionsSixDay)

    if weatherConditionsSixDay == "Rain":
        weatherConditionsSixDayIcon = "/static/images/rain.svg"
    elif weatherConditionsSixDay == "Clouds":
        weatherConditionsSixDayIcon = "/static/images/cloudy.svg"
    elif weatherConditionsSixDay == "Clear":
        weatherConditionsSixDayIcon = "/static/images/sunny.svg"
    elif weatherConditionsSixDay == "Snow":
        weatherConditionsSixDayIcon = "/static/images/snow.svg"
    elif weatherConditionsSixDay == "Thunderstorm":
        weatherConditionsSixDayIcon = "/static/images/thunderstorms.svg"
    elif weatherConditionsSixDay == "Wind":
        weatherConditionsSixDayIcon = "/static/images/wind.svg"
    elif weatherConditionsSixDay == "Hail":
        weatherConditionsSixDayIcon = "/static/images/hailstones.svg"

    temperatureforecastSixDay = openWeatherDataSixDay['main']
    temperatureforecastSixDay = temperatureforecastSixDay['temp']
    temperatureforecastSixDay = (temperatureforecastSixDay - 273.15)
    temperatureforecastSixDay = round(temperatureforecastSixDay, 0)
    temperatureforecastSixDay = int(temperatureforecastSixDay)
    temperatureforecastSixDay = str(temperatureforecastSixDay) + "°C"

    SixDayDate = openWeatherDataSixDay['dt_txt']
    SixDayDate = SixDayDate.split(" ")
    SixDayDate = SixDayDate[0]
    SixDayDate = date.fromisoformat(SixDayDate)
    SixDayDate = calendar.day_name[SixDayDate.weekday()]
    SixDayDate = str(SixDayDate)
    SixDayDate = SixDayDate[0:3]
    print(SixDayDate)

    SixDayWindSpeed = openWeatherDataSixDay['wind']
    SixDayWindSpeed = SixDayWindSpeed['speed']
    SixDayWindSpeed = SixDayWindSpeed / 0.447
    SixDayWindSpeed = round(SixDayWindSpeed, 0)
    SixDayWindSpeed = int(SixDayWindSpeed)
    SixDayWindSpeed = str(SixDayWindSpeed) + "mph"
    print("SixDay Wind Speed", SixDayWindSpeed)

    SixDayWindDirection = openWeatherDataSixDay['wind']
    SixDayWindDirection = SixDayWindDirection['deg']
    print("SixDay Wind Direction", SixDayWindDirection)
    if SixDayWindDirection >= 0 and SixDayWindDirection < 22.5 or SixDayWindDirection >= 337.5 and SixDayWindDirection <= 360:
        SixDayWindDirectionDescription = "North"
    elif SixDayWindDirection >= 22.5 and SixDayWindDirection < 67.5:
        SixDayWindDirectionDescription = "North East"
    elif SixDayWindDirection >= 67.5 and SixDayWindDirection < 112.5:
        SixDayWindDirectionDescription = "East"
    elif SixDayWindDirection >= 112.5 and SixDayWindDirection < 157.5:
        SixDayWindDirectionDescription = "South East"
    elif SixDayWindDirection >= 157.5 and SixDayWindDirection < 202.5:
        SixDayWindDirectionDescription = "South"
    elif SixDayWindDirection >= 202.5 and SixDayWindDirection < 247.5:
        SixDayWindDirectionDescription = "South West"
    elif SixDayWindDirection >= 247.5 and SixDayWindDirection < 292.5:
        SixDayWindDirectionDescription = "West"
    elif SixDayWindDirection >= 292.5 and SixDayWindDirection < 337.5:
        SixDayWindDirectionDescription = "North West"

    SixDayHumidity = openWeatherDataSixDay['main']
    SixDayHumidity = SixDayHumidity['humidity']
    SixDayHumidity = str(SixDayHumidity) + "%"
    print("SixDay Humidity", SixDayHumidity)




    data = strTemperatureCelsius1, strHumidity, aqi, aqi_description, strWindSpeed, windDirectionDescription, UV_index, UV_index_description, UV_index_percentage, UV_index_colour, aqi_percentage, aqi_colour, compass, strTemperatureFarenheit, strWindSpeedKMH, openWeatherDataToday, temperatureforecastToday, weatherConditionsTodayIcon, tomorrowDate, weatherConditionsTomorrowIcon, temperatureforecastTomorrow, tomorrowWindSpeed, tomorrowWindDirectionDescription, tomorrowHumidity, ThreeDayDate, weatherConditionsThreeDayIcon, temperatureforecastThreeDay, ThreeDayWindSpeed, ThreeDayWindDirectionDescription, ThreeDayHumidity, FourDayDate, weatherConditionsFourDayIcon, temperatureforecastFourDay, FourDayWindSpeed, FourDayWindDirectionDescription, FourDayHumidity, FiveDayDate, weatherConditionsFiveDayIcon, temperatureforecastFiveDay, FiveDayWindSpeed, FiveDayWindDirectionDescription, FiveDayHumidity, SixDayDate, weatherConditionsSixDayIcon, temperatureforecastSixDay, SixDayWindSpeed, SixDayWindDirectionDescription, SixDayHumidity
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

@app.route('/openweathertest', methods=['GET', 'POST'])
def openweathertest():
    openWeather_API_Key = 'cdb2f81a0c0053ff42b1db37fdb0b39b'
    openWeatherID = 2646057
    local_time = int(time.time())
    params = {
        "t": local_time
    }
    openWeatherURL = 'https://api.openweathermap.org/data/2.5/forecast?id=' + str(openWeatherID) + '&appid=' + openWeather_API_Key
    response = requests.get(openWeatherURL, params=params)
    openWeatherData = response.json()
    print("openWeatherData", openWeatherData)
    print(type(openWeatherData))
    openWeatherData = openWeatherData['list']
    openWeatherDataToday = openWeatherData[16]
    print(openWeatherDataToday)
    OpenWeatherDataTodayWeather = openWeatherDataToday['weather']
    OpenWeatherDataTodayWeather = OpenWeatherDataTodayWeather[0]
    print(OpenWeatherDataTodayWeather)
    weatherConditions = OpenWeatherDataTodayWeather['main']
    print(weatherConditions)
    tomorrowDate = openWeatherDataToday['dt_txt']
    tomorrowDate = tomorrowDate.split(" ")
    tomorrowDate = tomorrowDate[0]
    print(tomorrowDate)

    return jsonify(openWeatherData)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # port number
    app.run(debug=True, host='0.0.0.0', port=port)  # run the application
