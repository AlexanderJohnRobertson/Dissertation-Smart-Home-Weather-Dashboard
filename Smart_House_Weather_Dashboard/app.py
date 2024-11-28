"""Flask application for the Smart Home Weather Dashboard Author: S275931."""
import json
from sys import api_version

from flask import Flask, render_template, jsonify
import os
import hashlib, requests, time, hmac
from datetime import date
import calendar
import re

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

    pressure = openWeatherDataToday['main']
    pressure = pressure['pressure']
    pressure = round(pressure, 0)
    pressure = int(pressure)
    strPressure = str(pressure) + " hPa/mbar"
    if pressure >= 700 and pressure <= 710:
        angle= 4.5
    elif pressure >= 711 and pressure <= 720:
        angle = 9
    elif pressure >= 721 and pressure <= 730:
        angle = 13.5
    elif pressure >= 731 and pressure <= 740:
        angle = 18
    elif pressure >= 741 and pressure <= 750:
        angle = 22.5
    elif pressure >= 751 and pressure <= 760:
        angle = 27
    elif pressure >= 761 and pressure <= 770:
        angle = 31.5
    elif pressure >= 771 and pressure <= 780:
        angle = 36
    elif pressure >= 781 and pressure <= 790:
        angle = 40.5
    elif pressure >= 791 and pressure <= 800:
        angle = 45
    elif pressure >= 801 and pressure <= 810:
        angle = 49.5
    elif pressure >= 811 and pressure <= 820:
        angle = 54
    elif pressure >= 821 and pressure <= 830:
        angle = 58.5
    elif pressure >= 831 and pressure <= 840:
        angle = 63
    elif pressure >= 841 and pressure <= 850:
        angle = 67.5
    elif pressure >= 851 and pressure <= 860:
        angle = 72
    elif pressure >= 861 and pressure <= 870:
        angle = 76.5
    elif pressure >= 871 and pressure <= 880:
        angle = 81
    elif pressure >= 881 and pressure <= 890:
        angle = 85.5
    elif pressure >= 891 and pressure <= 900:
        angle = 90
    elif pressure >= 901 and pressure <= 910:
        angle = 94.5
    elif pressure >= 911 and pressure <= 920:
        angle = 99
    elif pressure >= 921 and pressure <= 930:
        angle = 103.5
    elif pressure >= 931 and pressure <= 940:
        angle = 108
    elif pressure >= 941 and pressure <= 950:
        angle = 112.5
    elif pressure >= 951 and pressure <= 960:
        angle = 117
    elif pressure >= 961 and pressure <= 970:
        angle = 121.5
    elif pressure >= 971 and pressure <= 980:
        angle = 126
    elif pressure >= 981 and pressure <= 990:
        angle = 130.5
    elif pressure >= 991 and pressure <= 1000:
        angle = 135
    elif pressure >= 1001 and pressure <= 1010:
        angle = 139.5
    elif pressure >= 1011 and pressure <= 1020:
        angle = 144
    elif pressure >= 1021 and pressure <= 1030:
        angle = 148.5
    elif pressure >= 1031 and pressure <= 1040:
        angle = 153
    elif pressure >= 1041 and pressure <= 1050:
        angle = 157.5
    elif pressure >= 1051 and pressure <= 1060:
        angle = 162
    elif pressure >= 1061 and pressure <= 1070:
        angle = 166.5
    elif pressure >= 1071 and pressure <= 1080:
        angle = 171
    elif pressure >= 1081 and pressure <= 1090:
        angle = 175.5
    elif pressure >= 1091 and pressure <= 1100:
        angle = 180



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

    #Weather API Hourly Forecast
    # Current Weather
    weatherAPI_key = '33d91967a1b04700807201804242711'
    weatherAPIurl = 'https://api.weatherapi.com/v1/forecast.json?key=' + weatherAPI_key + '&q=IP5 3RE&days=1&aqi=yes&alerts=yes'
    print(weatherAPIurl)
    response = requests.get(weatherAPIurl)
    weatherAPIData = response.json()
    print(weatherAPIData)
    print(type(weatherAPIData))
    weatherAPIDataCurrent = weatherAPIData['current']
    print(weatherAPIDataCurrent)
    weatherAPIDataCurrentTemperature = weatherAPIDataCurrent['temp_c']
    print(weatherAPIDataCurrentTemperature)
    weatherAPIDataCurrentTemperature = round(weatherAPIDataCurrentTemperature, 0)
    weatherAPIDataCurrentTemperature = int(weatherAPIDataCurrentTemperature)
    weatherAPIDataCurrentTemperature = str(weatherAPIDataCurrentTemperature) + "°C"
    print(weatherAPIDataCurrentTemperature)
    weatherAPIDataCurrentCondition = weatherAPIDataCurrent['condition']
    print(weatherAPIDataCurrentCondition)
    weatherAPIDataCurrentCondition = weatherAPIDataCurrentCondition['text']
    print(weatherAPIDataCurrentCondition)

    regexThunderCurrent = re.findall("Thunder|thunder", weatherAPIDataCurrentCondition)
    regexRainCurrent = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPIDataCurrentCondition)
    regexCloudCurrent = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPIDataCurrentCondition)
    regexClearCurrent = re.findall("Clear|clear|Sun|sun", weatherAPIDataCurrentCondition)
    regexSnowCurrent = re.findall("Snow|snow|Sleet|sleet", weatherAPIDataCurrentCondition)
    regexWindCurrent = re.findall("Wind|wind", weatherAPIDataCurrentCondition)
    regexHailCurrent = re.findall("Hail|hail", weatherAPIDataCurrentCondition)
    regexMistCurrent = re.findall("Mist|mist|Fog|fog", weatherAPIDataCurrentCondition)

    if regexThunderCurrent == ['Thunder'] or regexThunderCurrent == ['thunder']:
        weatherAPIDataCurrentConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRainCurrent == ['Rain'] or regexRainCurrent == ['rain'] or regexRainCurrent == ['Shower'] or regexRainCurrent == ['shower'] or regexRainCurrent == ['Drizzle'] or regexRainCurrent == ['drizzle']:
        weatherAPIDataCurrentConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloudCurrent == ['Cloud'] or regexCloudCurrent == ['cloud'] or regexCloudCurrent == ['Overcast'] or regexCloudCurrent == ['overcast'] or regexCloudCurrent == ['Cloudy'] or regexCloudCurrent == ['cloudy']:
        weatherAPIDataCurrentConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClearCurrent == ['Clear'] or regexClearCurrent == ['clear'] or regexClearCurrent == ['Sun'] or regexClearCurrent == ['sun']:
        weatherAPIDataCurrentConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnowCurrent == ['Snow'] or regexSnowCurrent == ['snow'] or regexSnowCurrent == ['Sleet'] or regexSnowCurrent == ['sleet']:
        weatherAPIDataCurrentConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWindCurrent == ['Wind'] or regexWindCurrent == ['wind']:
        weatherAPIDataCurrentConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHailCurrent == ['Hail'] or regexHailCurrent == ['hail']:
        weatherAPIDataCurrentConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMistCurrent == ['Mist'] or regexMistCurrent == ['mist'] or regexMistCurrent == ['Fog'] or regexMistCurrent == ['fog']:
        weatherAPIDataCurrentConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")

    print("Weather API Current Condition Icon", weatherAPIDataCurrentConditionIcon)

    #01 Hour Forecast
    weatherAPI01HourData = weatherAPIData['forecast']
    weatherAPI01HourData = weatherAPI01HourData['forecastday']
    weatherAPI01HourData = weatherAPI01HourData[0]
    weatherAPI01HourData = weatherAPI01HourData['hour']
    weatherAPI01HourData = weatherAPI01HourData[0]
    weatherAPI01HourDataConditionTime = weatherAPI01HourData['time']
    weatherAPI01HourDataConditionTime = weatherAPI01HourDataConditionTime.split(" ")
    print(weatherAPI01HourDataConditionTime)
    weatherAPI01HourDataConditionTime = weatherAPI01HourDataConditionTime[1]
    print(weatherAPI01HourDataConditionTime)
    weatherAPI01HourDataConditionTime = weatherAPI01HourDataConditionTime.split(":")
    print(weatherAPI01HourDataConditionTime)
    weatherAPI01HourDataConditionTime = weatherAPI01HourDataConditionTime[0]
    print(weatherAPI01HourDataConditionTime)
    weatherAPI01HourDataTemperature = weatherAPI01HourData['temp_c']
    print(weatherAPI01HourDataTemperature)
    weatherAPI01HourDataTemperature = round(weatherAPI01HourDataTemperature, 0)
    weatherAPI01HourDataTemperature = int(weatherAPI01HourDataTemperature)
    weatherAPI01HourDataTemperature = str(weatherAPI01HourDataTemperature) + "°C"
    print(weatherAPI01HourDataTemperature)
    weatherAPI01HourDataCondition = weatherAPI01HourData['condition']
    print(weatherAPI01HourDataCondition)
    weatherAPI01HourDataCondition = weatherAPI01HourDataCondition['text']
    print(weatherAPI01HourDataCondition)

    regexThunder01Hour = re.findall("Thunder|thunder", weatherAPI01HourDataCondition)
    regexRain01Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI01HourDataCondition)
    regexCloud01Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI01HourDataCondition)
    regexClear01Hour = re.findall("Clear|clear|Sun|sun", weatherAPI01HourDataCondition)
    regexSnow01Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI01HourDataCondition)
    regexWind01Hour = re.findall("Wind|wind", weatherAPI01HourDataCondition)
    regexHail01Hour = re.findall("Hail|hail", weatherAPI01HourDataCondition)
    regexMist01Hour = re.findall("Mist|mist|Fog|fog", weatherAPI01HourDataCondition)

    if regexThunder01Hour == ['Thunder'] or regexThunder01Hour == ['thunder']:
        weatherAPI01HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain01Hour == ['Rain'] or regexRain01Hour == ['rain'] or regexRain01Hour == [
        'Shower'] or regexRain01Hour == ['shower'] or regexRain01Hour == ['Drizzle'] or regexRain01Hour == [
        'drizzle']:
        weatherAPI01HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud01Hour == ['Cloud'] or regexCloud01Hour == ['cloud'] or regexCloud01Hour == [
        'Overcast'] or regexCloud01Hour == ['overcast'] or regexCloud01Hour == ['Cloudy'] or regexCloud01Hour == [
        'cloudy']:
        weatherAPI01HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear01Hour == ['Clear'] or regexClear01Hour == ['clear'] or regexClear01Hour == [
        'Sun'] or regexClear01Hour == ['sun']:
        weatherAPI01HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow01Hour == ['Snow'] or regexSnow01Hour == ['snow'] or regexSnow01Hour == [
        'Sleet'] or regexSnow01Hour == ['sleet']:
        weatherAPI01HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind01Hour == ['Wind'] or regexWind01Hour == ['wind']:
        weatherAPI01HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail01Hour == ['Hail'] or regexHail01Hour == ['hail']:
        weatherAPI01HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist01Hour == ['Mist'] or regexMist01Hour == ['mist'] or regexMist01Hour == ['Fog'] or regexMist01Hour == ['fog']:
        weatherAPI01HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")

    print("Weather API 01 Hour Condition Icon", weatherAPI01HourDataConditionIcon)

    #02 Hour Forecast
    weatherAPI02HourData = weatherAPIData['forecast']
    weatherAPI02HourData = weatherAPI02HourData['forecastday']
    weatherAPI02HourData = weatherAPI02HourData[0]
    weatherAPI02HourData = weatherAPI02HourData['hour']
    weatherAPI02HourData = weatherAPI02HourData[1]
    weatherAPI02HourDataConditionTime = weatherAPI02HourData['time']
    weatherAPI02HourDataConditionTime = weatherAPI02HourDataConditionTime.split(" ")
    print(weatherAPI02HourDataConditionTime)
    weatherAPI02HourDataConditionTime = weatherAPI02HourDataConditionTime[1]
    print(weatherAPI02HourDataConditionTime)
    weatherAPI02HourDataConditionTime = weatherAPI02HourDataConditionTime.split(":")
    print(weatherAPI02HourDataConditionTime)
    weatherAPI02HourDataConditionTime = weatherAPI02HourDataConditionTime[0]
    print(weatherAPI02HourDataConditionTime)
    weatherAPI02HourDataTemperature = weatherAPI02HourData['temp_c']
    print(weatherAPI02HourDataTemperature)
    weatherAPI02HourDataTemperature = round(weatherAPI02HourDataTemperature, 0)
    weatherAPI02HourDataTemperature = int(weatherAPI02HourDataTemperature)
    weatherAPI02HourDataTemperature = str(weatherAPI02HourDataTemperature) + "°C"
    print(weatherAPI02HourDataTemperature)
    weatherAPI02HourDataCondition = weatherAPI02HourData['condition']
    print(weatherAPI02HourDataCondition)
    weatherAPI02HourDataCondition = weatherAPI02HourDataCondition['text']
    print(weatherAPI02HourDataCondition)

    regexThunder02Hour = re.findall("Thunder|thunder", weatherAPI02HourDataCondition)
    regexRain02Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI02HourDataCondition)
    regexCloud02Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI02HourDataCondition)
    regexClear02Hour = re.findall("Clear|clear|Sun|sun", weatherAPI02HourDataCondition)
    regexSnow02Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI02HourDataCondition)
    regexWind02Hour = re.findall("Wind|wind", weatherAPI02HourDataCondition)
    regexHail02Hour = re.findall("Hail|hail", weatherAPI02HourDataCondition)
    regexMist02Hour = re.findall("Mist|mist|Fog|fog", weatherAPI02HourDataCondition)

    if regexThunder02Hour == ['Thunder'] or regexThunder02Hour == ['thunder']:
        weatherAPI02HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain02Hour == ['Rain'] or regexRain02Hour == ['rain'] or regexRain02Hour == [
        'Shower'] or regexRain02Hour == ['shower'] or regexRain02Hour == ['Drizzle'] or regexRain02Hour == [
        'drizzle']:
        weatherAPI02HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud02Hour == ['Cloud'] or regexCloud02Hour == ['cloud'] or regexCloud02Hour == [
        'Overcast'] or regexCloud02Hour == ['overcast'] or regexCloud02Hour == ['Cloudy'] or regexCloud02Hour == [
        'cloudy']:
        weatherAPI02HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear02Hour == ['Clear'] or regexClear02Hour == ['clear'] or regexClear02Hour == [
        'Sun'] or regexClear02Hour == ['sun']:
        weatherAPI02HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow02Hour == ['Snow'] or regexSnow02Hour == ['snow'] or regexSnow02Hour == [
        'Sleet'] or regexSnow02Hour == ['sleet']:
        weatherAPI02HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind02Hour == ['Wind'] or regexWind02Hour == ['wind']:
        weatherAPI02HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail02Hour == ['Hail'] or regexHail02Hour == ['hail']:
        weatherAPI02HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist02Hour == ['Mist'] or regexMist02Hour == ['mist'] or regexMist02Hour == ['Fog'] or regexMist02Hour == ['fog']:
        weatherAPI02HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")

    print("Weather API 02 Hour Condition Icon", weatherAPI02HourDataConditionIcon)

    #03 Hour Forecast
    weatherAPI03HourData = weatherAPIData['forecast']
    weatherAPI03HourData = weatherAPI03HourData['forecastday']
    weatherAPI03HourData = weatherAPI03HourData[0]
    weatherAPI03HourData = weatherAPI03HourData['hour']
    weatherAPI03HourData = weatherAPI03HourData[2]
    weatherAPI03HourDataConditionTime = weatherAPI03HourData['time']
    weatherAPI03HourDataConditionTime = weatherAPI03HourDataConditionTime.split(" ")
    print(weatherAPI03HourDataConditionTime)
    weatherAPI03HourDataConditionTime = weatherAPI03HourDataConditionTime[1]
    print(weatherAPI03HourDataConditionTime)
    weatherAPI03HourDataConditionTime = weatherAPI03HourDataConditionTime.split(":")
    print(weatherAPI03HourDataConditionTime)
    weatherAPI03HourDataConditionTime = weatherAPI03HourDataConditionTime[0]
    print(weatherAPI03HourDataConditionTime)
    weatherAPI03HourDataTemperature = weatherAPI03HourData['temp_c']
    print(weatherAPI03HourDataTemperature)
    weatherAPI03HourDataTemperature = round(weatherAPI03HourDataTemperature, 0)
    weatherAPI03HourDataTemperature = int(weatherAPI03HourDataTemperature)
    weatherAPI03HourDataTemperature = str(weatherAPI03HourDataTemperature) + "°C"
    print(weatherAPI03HourDataTemperature)
    weatherAPI03HourDataCondition = weatherAPI03HourData['condition']
    print(weatherAPI03HourDataCondition)
    weatherAPI03HourDataCondition = weatherAPI03HourDataCondition['text']
    print(weatherAPI03HourDataCondition)

    regexThunder03Hour = re.findall("Thunder|thunder", weatherAPI03HourDataCondition)
    regexRain03Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI03HourDataCondition)
    regexCloud03Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI03HourDataCondition)
    regexClear03Hour = re.findall("Clear|clear|Sun|sun", weatherAPI03HourDataCondition)
    regexSnow03Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI03HourDataCondition)
    regexWind03Hour = re.findall("Wind|wind", weatherAPI03HourDataCondition)
    regexHail03Hour = re.findall("Hail|hail", weatherAPI03HourDataCondition)
    regexMist03Hour = re.findall("Mist|mist|Fog|fog", weatherAPI03HourDataCondition)

    if regexThunder03Hour == ['Thunder'] or regexThunder03Hour == ['thunder']:
        weatherAPI03HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain03Hour == ['Rain'] or regexRain03Hour == ['rain'] or regexRain03Hour == [
        'Shower'] or regexRain03Hour == ['shower'] or regexRain03Hour == ['Drizzle'] or regexRain03Hour == [
        'drizzle']:
        weatherAPI03HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud03Hour == ['Cloud'] or regexCloud03Hour == ['cloud'] or regexCloud03Hour == [
        'Overcast'] or regexCloud03Hour == ['overcast'] or regexCloud03Hour == ['Cloudy'] or regexCloud03Hour == [
        'cloudy']:
        weatherAPI03HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear03Hour == ['Clear'] or regexClear03Hour == ['clear'] or regexClear03Hour == [
        'Sun'] or regexClear03Hour == ['sun']:
        weatherAPI03HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow03Hour == ['Snow'] or regexSnow03Hour == ['snow'] or regexSnow03Hour == [
        'Sleet'] or regexSnow03Hour == ['sleet']:
        weatherAPI03HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind03Hour == ['Wind'] or regexWind03Hour == ['wind']:
        weatherAPI03HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail03Hour == ['Hail'] or regexHail03Hour == ['hail']:
        weatherAPI03HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist03Hour == ['Mist'] or regexMist03Hour == ['mist'] or regexMist03Hour == ['Fog'] or regexMist03Hour == ['fog']:
        weatherAPI03HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")


    #04 Hour Forecast
    weatherAPI04HourData = weatherAPIData['forecast']
    weatherAPI04HourData = weatherAPI04HourData['forecastday']
    weatherAPI04HourData = weatherAPI04HourData[0]
    weatherAPI04HourData = weatherAPI04HourData['hour']
    weatherAPI04HourData = weatherAPI04HourData[3]
    weatherAPI04HourDataConditionTime = weatherAPI04HourData['time']
    weatherAPI04HourDataConditionTime = weatherAPI04HourDataConditionTime.split(" ")
    print(weatherAPI04HourDataConditionTime)
    weatherAPI04HourDataConditionTime = weatherAPI04HourDataConditionTime[1]
    print(weatherAPI04HourDataConditionTime)
    weatherAPI04HourDataConditionTime = weatherAPI04HourDataConditionTime.split(":")
    print(weatherAPI04HourDataConditionTime)
    weatherAPI04HourDataConditionTime = weatherAPI04HourDataConditionTime[0]
    print(weatherAPI04HourDataConditionTime)
    weatherAPI04HourDataTemperature = weatherAPI04HourData['temp_c']
    print(weatherAPI04HourDataTemperature)
    weatherAPI04HourDataTemperature = round(weatherAPI04HourDataTemperature, 0)
    weatherAPI04HourDataTemperature = int(weatherAPI04HourDataTemperature)
    weatherAPI04HourDataTemperature = str(weatherAPI04HourDataTemperature) + "°C"
    print(weatherAPI04HourDataTemperature)
    weatherAPI04HourDataCondition = weatherAPI04HourData['condition']
    print(weatherAPI04HourDataCondition)
    weatherAPI04HourDataCondition = weatherAPI04HourDataCondition['text']
    print(weatherAPI04HourDataCondition)

    regexThunder04Hour = re.findall("Thunder|thunder", weatherAPI04HourDataCondition)
    regexRain04Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI04HourDataCondition)
    regexCloud04Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI04HourDataCondition)
    regexClear04Hour = re.findall("Clear|clear|Sun|sun", weatherAPI04HourDataCondition)
    regexSnow04Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI04HourDataCondition)
    regexWind04Hour = re.findall("Wind|wind", weatherAPI04HourDataCondition)
    regexHail04Hour = re.findall("Hail|hail", weatherAPI04HourDataCondition)
    regexMist04Hour = re.findall("Mist|mist|Fog|fog", weatherAPI04HourDataCondition)

    if regexThunder04Hour == ['Thunder'] or regexThunder04Hour == ['thunder']:
        weatherAPI04HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain04Hour == ['Rain'] or regexRain04Hour == ['rain'] or regexRain04Hour == [
        'Shower'] or regexRain04Hour == ['shower'] or regexRain04Hour == ['Drizzle'] or regexRain04Hour == [
        'drizzle']:
        weatherAPI04HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud04Hour == ['Cloud'] or regexCloud04Hour == ['cloud'] or regexCloud04Hour == [
        'Overcast'] or regexCloud04Hour == ['overcast'] or regexCloud04Hour == ['Cloudy'] or regexCloud04Hour == [
        'cloudy']:
        weatherAPI04HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear04Hour == ['Clear'] or regexClear04Hour == ['clear'] or regexClear04Hour == [
        'Sun'] or regexClear04Hour == ['sun']:
        weatherAPI04HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow04Hour == ['Snow'] or regexSnow04Hour == ['snow'] or regexSnow04Hour == [
        'Sleet'] or regexSnow04Hour == ['sleet']:
        weatherAPI04HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind04Hour == ['Wind'] or regexWind04Hour == ['wind']:
        weatherAPI04HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail04Hour == ['Hail'] or regexHail04Hour == ['hail']:
        weatherAPI04HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist04Hour == ['Mist'] or regexMist04Hour == ['mist'] or regexMist04Hour == ['Fog'] or regexMist04Hour == ['fog']:
        weatherAPI04HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")


    #05 Hour Forecast
    weatherAPI05HourData = weatherAPIData['forecast']
    weatherAPI05HourData = weatherAPI05HourData['forecastday']
    weatherAPI05HourData = weatherAPI05HourData[0]
    weatherAPI05HourData = weatherAPI05HourData['hour']
    weatherAPI05HourData = weatherAPI05HourData[4]
    weatherAPI05HourDataConditionTime = weatherAPI05HourData['time']
    weatherAPI05HourDataConditionTime = weatherAPI05HourDataConditionTime.split(" ")
    print(weatherAPI05HourDataConditionTime)
    weatherAPI05HourDataConditionTime = weatherAPI05HourDataConditionTime[1]
    print(weatherAPI05HourDataConditionTime)
    weatherAPI05HourDataConditionTime = weatherAPI05HourDataConditionTime.split(":")
    print(weatherAPI05HourDataConditionTime)
    weatherAPI05HourDataConditionTime = weatherAPI05HourDataConditionTime[0]
    print(weatherAPI05HourDataConditionTime)
    weatherAPI05HourDataTemperature = weatherAPI05HourData['temp_c']
    print(weatherAPI05HourDataTemperature)
    weatherAPI05HourDataTemperature = round(weatherAPI05HourDataTemperature, 0)
    weatherAPI05HourDataTemperature = int(weatherAPI05HourDataTemperature)
    weatherAPI05HourDataTemperature = str(weatherAPI05HourDataTemperature) + "°C"
    print(weatherAPI05HourDataTemperature)
    weatherAPI05HourDataCondition = weatherAPI05HourData['condition']
    print(weatherAPI05HourDataCondition)
    weatherAPI05HourDataCondition = weatherAPI05HourDataCondition['text']
    print(weatherAPI05HourDataCondition)

    regexThunder05Hour = re.findall("Thunder|thunder", weatherAPI05HourDataCondition)
    regexRain05Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI05HourDataCondition)
    regexCloud05Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI05HourDataCondition)
    regexClear05Hour = re.findall("Clear|clear|Sun|sun", weatherAPI05HourDataCondition)
    regexSnow05Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI05HourDataCondition)
    regexWind05Hour = re.findall("Wind|wind", weatherAPI05HourDataCondition)
    regexHail05Hour = re.findall("Hail|hail", weatherAPI05HourDataCondition)
    regexMist05Hour = re.findall("Mist|mist|Fog|fog", weatherAPI05HourDataCondition)

    if regexThunder05Hour == ['Thunder'] or regexThunder05Hour == ['thunder']:
        weatherAPI05HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain05Hour == ['Rain'] or regexRain05Hour == ['rain'] or regexRain05Hour == [
        'Shower'] or regexRain05Hour == ['shower'] or regexRain05Hour == ['Drizzle'] or regexRain05Hour == [
        'drizzle']:
        weatherAPI05HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud05Hour == ['Cloud'] or regexCloud05Hour == ['cloud'] or regexCloud05Hour == [
        'Overcast'] or regexCloud05Hour == ['overcast'] or regexCloud05Hour == ['Cloudy'] or regexCloud05Hour == [
        'cloudy']:
        weatherAPI05HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear05Hour == ['Clear'] or regexClear05Hour == ['clear'] or regexClear05Hour == [
        'Sun'] or regexClear05Hour == ['sun']:
        weatherAPI05HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow05Hour == ['Snow'] or regexSnow05Hour == ['snow'] or regexSnow05Hour == [
        'Sleet'] or regexSnow05Hour == ['sleet']:
        weatherAPI05HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind05Hour == ['Wind'] or regexWind05Hour == ['wind']:
        weatherAPI05HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail05Hour == ['Hail'] or regexHail05Hour == ['hail']:
        weatherAPI05HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist05Hour == ['Mist'] or regexMist05Hour == ['mist'] or regexMist05Hour == ['Fog'] or regexMist05Hour == ['fog']:
        weatherAPI05HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")

    #06 Hour Forecast
    weatherAPI06HourData = weatherAPIData['forecast']
    weatherAPI06HourData = weatherAPI06HourData['forecastday']
    weatherAPI06HourData = weatherAPI06HourData[0]
    weatherAPI06HourData = weatherAPI06HourData['hour']
    weatherAPI06HourData = weatherAPI06HourData[5]
    weatherAPI06HourDataConditionTime = weatherAPI06HourData['time']
    weatherAPI06HourDataConditionTime = weatherAPI06HourDataConditionTime.split(" ")
    print(weatherAPI06HourDataConditionTime)
    weatherAPI06HourDataConditionTime = weatherAPI06HourDataConditionTime[1]
    print(weatherAPI06HourDataConditionTime)
    weatherAPI06HourDataConditionTime = weatherAPI06HourDataConditionTime.split(":")
    print(weatherAPI06HourDataConditionTime)
    weatherAPI06HourDataConditionTime = weatherAPI06HourDataConditionTime[0]
    print(weatherAPI06HourDataConditionTime)
    weatherAPI06HourDataTemperature = weatherAPI06HourData['temp_c']
    print(weatherAPI06HourDataTemperature)
    weatherAPI06HourDataTemperature = round(weatherAPI06HourDataTemperature, 0)
    weatherAPI06HourDataTemperature = int(weatherAPI06HourDataTemperature)
    weatherAPI06HourDataTemperature = str(weatherAPI06HourDataTemperature) + "°C"
    print(weatherAPI06HourDataTemperature)
    weatherAPI06HourDataCondition = weatherAPI06HourData['condition']
    print(weatherAPI06HourDataCondition)
    weatherAPI06HourDataCondition = weatherAPI06HourDataCondition['text']
    print(weatherAPI06HourDataCondition)

    regexThunder06Hour = re.findall("Thunder|thunder", weatherAPI06HourDataCondition)
    regexRain06Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI06HourDataCondition)
    regexCloud06Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI06HourDataCondition)
    regexClear06Hour = re.findall("Clear|clear|Sun|sun", weatherAPI06HourDataCondition)
    regexSnow06Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI06HourDataCondition)
    regexWind06Hour = re.findall("Wind|wind", weatherAPI06HourDataCondition)
    regexHail06Hour = re.findall("Hail|hail", weatherAPI06HourDataCondition)
    regexMist06Hour = re.findall("Mist|mist|Fog|fog", weatherAPI06HourDataCondition)

    if regexThunder06Hour == ['Thunder'] or regexThunder06Hour == ['thunder']:
        weatherAPI06HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain06Hour == ['Rain'] or regexRain06Hour == ['rain'] or regexRain06Hour == [
        'Shower'] or regexRain06Hour == ['shower'] or regexRain06Hour == ['Drizzle'] or regexRain06Hour == [
        'drizzle']:
        weatherAPI06HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud06Hour == ['Cloud'] or regexCloud06Hour == ['cloud'] or regexCloud06Hour == [
        'Overcast'] or regexCloud06Hour == ['overcast'] or regexCloud06Hour == ['Cloudy'] or regexCloud06Hour == [
        'cloudy']:
        weatherAPI06HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear06Hour == ['Clear'] or regexClear06Hour == ['clear'] or regexClear06Hour == [
        'Sun'] or regexClear06Hour == ['sun']:
        weatherAPI06HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow06Hour == ['Snow'] or regexSnow06Hour == ['snow'] or regexSnow06Hour == [
        'Sleet'] or regexSnow06Hour == ['sleet']:
        weatherAPI06HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind06Hour == ['Wind'] or regexWind06Hour == ['wind']:
        weatherAPI06HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail06Hour == ['Hail'] or regexHail06Hour == ['hail']:
        weatherAPI06HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist06Hour == ['Mist'] or regexMist06Hour == ['mist'] or regexMist06Hour == ['Fog'] or regexMist06Hour == ['fog']:
        weatherAPI06HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")

    #07 Hour Forecast
    weatherAPI07HourData = weatherAPIData['forecast']
    weatherAPI07HourData = weatherAPI07HourData['forecastday']
    weatherAPI07HourData = weatherAPI07HourData[0]
    weatherAPI07HourData = weatherAPI07HourData['hour']
    weatherAPI07HourData = weatherAPI07HourData[6]
    weatherAPI07HourDataConditionTime = weatherAPI07HourData['time']
    weatherAPI07HourDataConditionTime = weatherAPI07HourDataConditionTime.split(" ")
    print(weatherAPI07HourDataConditionTime)
    weatherAPI07HourDataConditionTime = weatherAPI07HourDataConditionTime[1]
    print(weatherAPI07HourDataConditionTime)
    weatherAPI07HourDataConditionTime = weatherAPI07HourDataConditionTime.split(":")
    print(weatherAPI07HourDataConditionTime)
    weatherAPI07HourDataConditionTime = weatherAPI07HourDataConditionTime[0]
    print(weatherAPI07HourDataConditionTime)
    weatherAPI07HourDataTemperature = weatherAPI07HourData['temp_c']
    print(weatherAPI07HourDataTemperature)
    weatherAPI07HourDataTemperature = round(weatherAPI07HourDataTemperature, 0)
    weatherAPI07HourDataTemperature = int(weatherAPI07HourDataTemperature)
    weatherAPI07HourDataTemperature = str(weatherAPI07HourDataTemperature) + "°C"
    print(weatherAPI07HourDataTemperature)
    weatherAPI07HourDataCondition = weatherAPI07HourData['condition']
    print(weatherAPI07HourDataCondition)
    weatherAPI07HourDataCondition = weatherAPI07HourDataCondition['text']
    print(weatherAPI07HourDataCondition)

    regexThunder07Hour = re.findall("Thunder|thunder", weatherAPI07HourDataCondition)
    regexRain07Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI07HourDataCondition)
    regexCloud07Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI07HourDataCondition)
    regexClear07Hour = re.findall("Clear|clear|Sun|sun", weatherAPI07HourDataCondition)
    regexSnow07Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI07HourDataCondition)
    regexWind07Hour = re.findall("Wind|wind", weatherAPI07HourDataCondition)
    regexHail07Hour = re.findall("Hail|hail", weatherAPI07HourDataCondition)
    regexMist07Hour = re.findall("Mist|mist|Fog|fog", weatherAPI07HourDataCondition)

    if regexThunder07Hour == ['Thunder'] or regexThunder07Hour == ['thunder']:
        weatherAPI07HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain07Hour == ['Rain'] or regexRain07Hour == ['rain'] or regexRain07Hour == [
        'Shower'] or regexRain07Hour == ['shower'] or regexRain07Hour == ['Drizzle'] or regexRain07Hour == [
        'drizzle']:
        weatherAPI07HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud07Hour == ['Cloud'] or regexCloud07Hour == ['cloud'] or regexCloud07Hour == [
        'Overcast'] or regexCloud07Hour == ['overcast'] or regexCloud07Hour == ['Cloudy'] or regexCloud07Hour == [
        'cloudy']:
        weatherAPI07HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear07Hour == ['Clear'] or regexClear07Hour == ['clear'] or regexClear07Hour == [
        'Sun'] or regexClear07Hour == ['sun']:
        weatherAPI07HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow07Hour == ['Snow'] or regexSnow07Hour == ['snow'] or regexSnow07Hour == [
        'Sleet'] or regexSnow07Hour == ['sleet']:
        weatherAPI07HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind07Hour == ['Wind'] or regexWind07Hour == ['wind']:
        weatherAPI07HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail07Hour == ['Hail'] or regexHail07Hour == ['hail']:
        weatherAPI07HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist07Hour == ['Mist'] or regexMist07Hour == ['mist'] or regexMist07Hour == ['Fog'] or regexMist07Hour == ['fog']:
        weatherAPI07HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")


    #08 Hour Forecast
    weatherAPI08HourData = weatherAPIData['forecast']
    weatherAPI08HourData = weatherAPI08HourData['forecastday']
    weatherAPI08HourData = weatherAPI08HourData[0]
    weatherAPI08HourData = weatherAPI08HourData['hour']
    weatherAPI08HourData = weatherAPI08HourData[7]
    weatherAPI08HourDataConditionTime = weatherAPI08HourData['time']
    weatherAPI08HourDataConditionTime = weatherAPI08HourDataConditionTime.split(" ")
    print(weatherAPI08HourDataConditionTime)
    weatherAPI08HourDataConditionTime = weatherAPI08HourDataConditionTime[1]
    print(weatherAPI08HourDataConditionTime)
    weatherAPI08HourDataConditionTime = weatherAPI08HourDataConditionTime.split(":")
    print(weatherAPI08HourDataConditionTime)
    weatherAPI08HourDataConditionTime = weatherAPI08HourDataConditionTime[0]
    print(weatherAPI08HourDataConditionTime)
    weatherAPI08HourDataTemperature = weatherAPI08HourData['temp_c']
    print(weatherAPI08HourDataTemperature)
    weatherAPI08HourDataTemperature = round(weatherAPI08HourDataTemperature, 0)
    weatherAPI08HourDataTemperature = int(weatherAPI08HourDataTemperature)
    weatherAPI08HourDataTemperature = str(weatherAPI08HourDataTemperature) + "°C"
    print(weatherAPI08HourDataTemperature)
    weatherAPI08HourDataCondition = weatherAPI08HourData['condition']
    print(weatherAPI08HourDataCondition)
    weatherAPI08HourDataCondition = weatherAPI08HourDataCondition['text']
    print(weatherAPI08HourDataCondition)

    regexThunder08Hour = re.findall("Thunder|thunder", weatherAPI08HourDataCondition)
    regexRain08Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI08HourDataCondition)
    regexCloud08Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI08HourDataCondition)
    regexClear08Hour = re.findall("Clear|clear|Sun|sun", weatherAPI08HourDataCondition)
    regexSnow08Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI08HourDataCondition)
    regexWind08Hour = re.findall("Wind|wind", weatherAPI08HourDataCondition)
    regexHail08Hour = re.findall("Hail|hail", weatherAPI08HourDataCondition)
    regexMist08Hour = re.findall("Mist|mist|Fog|fog", weatherAPI08HourDataCondition)

    if regexThunder08Hour == ['Thunder'] or regexThunder08Hour == ['thunder']:
        weatherAPI08HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain08Hour == ['Rain'] or regexRain08Hour == ['rain'] or regexRain08Hour == [
        'Shower'] or regexRain08Hour == ['shower'] or regexRain08Hour == ['Drizzle'] or regexRain08Hour == [
        'drizzle']:
        weatherAPI08HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud08Hour == ['Cloud'] or regexCloud08Hour == ['cloud'] or regexCloud08Hour == [
        'Overcast'] or regexCloud08Hour == ['overcast'] or regexCloud08Hour == ['Cloudy'] or regexCloud08Hour == [
        'cloudy']:
        weatherAPI08HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear08Hour == ['Clear'] or regexClear08Hour == ['clear'] or regexClear08Hour == [
        'Sun'] or regexClear08Hour == ['sun']:
        weatherAPI08HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow08Hour == ['Snow'] or regexSnow08Hour == ['snow'] or regexSnow08Hour == [
        'Sleet'] or regexSnow08Hour == ['sleet']:
        weatherAPI08HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind08Hour == ['Wind'] or regexWind08Hour == ['wind']:
        weatherAPI08HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail08Hour == ['Hail'] or regexHail08Hour == ['hail']:
        weatherAPI08HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist08Hour == ['Mist'] or regexMist08Hour == ['mist'] or regexMist08Hour == ['Fog'] or regexMist08Hour == ['fog']:
        weatherAPI08HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")

    #09 Hour Forecast
    weatherAPI09HourData = weatherAPIData['forecast']
    weatherAPI09HourData = weatherAPI09HourData['forecastday']
    weatherAPI09HourData = weatherAPI09HourData[0]
    weatherAPI09HourData = weatherAPI09HourData['hour']
    weatherAPI09HourData = weatherAPI09HourData[8]
    weatherAPI09HourDataConditionTime = weatherAPI09HourData['time']
    weatherAPI09HourDataConditionTime = weatherAPI09HourDataConditionTime.split(" ")
    print(weatherAPI09HourDataConditionTime)
    weatherAPI09HourDataConditionTime = weatherAPI09HourDataConditionTime[1]
    print(weatherAPI09HourDataConditionTime)
    weatherAPI09HourDataConditionTime = weatherAPI09HourDataConditionTime.split(":")
    print(weatherAPI09HourDataConditionTime)
    weatherAPI09HourDataConditionTime = weatherAPI09HourDataConditionTime[0]
    print(weatherAPI09HourDataConditionTime)
    weatherAPI09HourDataTemperature = weatherAPI09HourData['temp_c']
    print(weatherAPI09HourDataTemperature)
    weatherAPI09HourDataTemperature = round(weatherAPI09HourDataTemperature, 0)
    weatherAPI09HourDataTemperature = int(weatherAPI09HourDataTemperature)
    weatherAPI09HourDataTemperature = str(weatherAPI09HourDataTemperature) + "°C"
    print(weatherAPI09HourDataTemperature)
    weatherAPI09HourDataCondition = weatherAPI09HourData['condition']
    print(weatherAPI09HourDataCondition)
    weatherAPI09HourDataCondition = weatherAPI09HourDataCondition['text']
    print(weatherAPI09HourDataCondition)

    regexThunder09Hour = re.findall("Thunder|thunder", weatherAPI09HourDataCondition)
    regexRain09Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI09HourDataCondition)
    regexCloud09Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI09HourDataCondition)
    regexClear09Hour = re.findall("Clear|clear|Sun|sun", weatherAPI09HourDataCondition)
    regexSnow09Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI09HourDataCondition)
    regexWind09Hour = re.findall("Wind|wind", weatherAPI09HourDataCondition)
    regexHail09Hour = re.findall("Hail|hail", weatherAPI09HourDataCondition)
    regexMist09Hour = re.findall("Mist|mist|Fog|fog", weatherAPI09HourDataCondition)

    if regexThunder09Hour == ['Thunder'] or regexThunder09Hour == ['thunder']:
        weatherAPI09HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain09Hour == ['Rain'] or regexRain09Hour == ['rain'] or regexRain09Hour == [
        'Shower'] or regexRain09Hour == ['shower'] or regexRain09Hour == ['Drizzle'] or regexRain09Hour == [
        'drizzle']:
        weatherAPI09HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud09Hour == ['Cloud'] or regexCloud09Hour == ['cloud'] or regexCloud09Hour == [
        'Overcast'] or regexCloud09Hour == ['overcast'] or regexCloud09Hour == ['Cloudy'] or regexCloud09Hour == [
        'cloudy']:
        weatherAPI09HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear09Hour == ['Clear'] or regexClear09Hour == ['clear'] or regexClear09Hour == [
        'Sun'] or regexClear09Hour == ['sun']:
        weatherAPI09HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow09Hour == ['Snow'] or regexSnow09Hour == ['snow'] or regexSnow09Hour == [
        'Sleet'] or regexSnow09Hour == ['sleet']:
        weatherAPI09HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind09Hour == ['Wind'] or regexWind09Hour == ['wind']:
        weatherAPI09HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail09Hour == ['Hail'] or regexHail09Hour == ['hail']:
        weatherAPI09HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist09Hour == ['Mist'] or regexMist09Hour == ['mist'] or regexMist09Hour == ['Fog'] or regexMist09Hour == ['fog']:
        weatherAPI09HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")

    #10 Hour Forecast
    weatherAPI10HourData = weatherAPIData['forecast']
    weatherAPI10HourData = weatherAPI10HourData['forecastday']
    weatherAPI10HourData = weatherAPI10HourData[0]
    weatherAPI10HourData = weatherAPI10HourData['hour']
    weatherAPI10HourData = weatherAPI10HourData[9]
    weatherAPI10HourDataConditionTime = weatherAPI10HourData['time']
    weatherAPI10HourDataConditionTime = weatherAPI10HourDataConditionTime.split(" ")
    print(weatherAPI10HourDataConditionTime)
    weatherAPI10HourDataConditionTime = weatherAPI10HourDataConditionTime[1]
    print(weatherAPI10HourDataConditionTime)
    weatherAPI10HourDataConditionTime = weatherAPI10HourDataConditionTime.split(":")
    print(weatherAPI10HourDataConditionTime)
    weatherAPI10HourDataConditionTime = weatherAPI10HourDataConditionTime[0]
    print(weatherAPI10HourDataConditionTime)
    weatherAPI10HourDataTemperature = weatherAPI10HourData['temp_c']
    print(weatherAPI10HourDataTemperature)
    weatherAPI10HourDataTemperature = round(weatherAPI10HourDataTemperature, 0)
    weatherAPI10HourDataTemperature = int(weatherAPI10HourDataTemperature)
    weatherAPI10HourDataTemperature = str(weatherAPI10HourDataTemperature) + "°C"
    print(weatherAPI10HourDataTemperature)
    weatherAPI10HourDataCondition = weatherAPI10HourData['condition']
    print(weatherAPI10HourDataCondition)
    weatherAPI10HourDataCondition = weatherAPI10HourDataCondition['text']
    print(weatherAPI10HourDataCondition)

    regexThunder10Hour = re.findall("Thunder|thunder", weatherAPI10HourDataCondition)
    regexRain10Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI10HourDataCondition)
    regexCloud10Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI10HourDataCondition)
    regexClear10Hour = re.findall("Clear|clear|Sun|sun", weatherAPI10HourDataCondition)
    regexSnow10Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI10HourDataCondition)
    regexWind10Hour = re.findall("Wind|wind", weatherAPI10HourDataCondition)
    regexHail10Hour = re.findall("Hail|hail", weatherAPI10HourDataCondition)
    regexMist10Hour = re.findall("Mist|mist|Fog|fog", weatherAPI10HourDataCondition)

    if regexThunder10Hour == ['Thunder'] or regexThunder10Hour == ['thunder']:
        weatherAPI10HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain10Hour == ['Rain'] or regexRain10Hour == ['rain'] or regexRain10Hour == [
        'Shower'] or regexRain10Hour == ['shower'] or regexRain10Hour == ['Drizzle'] or regexRain10Hour == [
        'drizzle']:
        weatherAPI10HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud10Hour == ['Cloud'] or regexCloud10Hour == ['cloud'] or regexCloud10Hour == [
        'Overcast'] or regexCloud10Hour == ['overcast'] or regexCloud10Hour == ['Cloudy'] or regexCloud10Hour == [
        'cloudy']:
        weatherAPI10HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear10Hour == ['Clear'] or regexClear10Hour == ['clear'] or regexClear10Hour == [
        'Sun'] or regexClear10Hour == ['sun']:
        weatherAPI10HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow10Hour == ['Snow'] or regexSnow10Hour == ['snow'] or regexSnow10Hour == [
        'Sleet'] or regexSnow10Hour == ['sleet']:
        weatherAPI10HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind10Hour == ['Wind'] or regexWind10Hour == ['wind']:
        weatherAPI10HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail10Hour == ['Hail'] or regexHail10Hour == ['hail']:
        weatherAPI10HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist10Hour == ['Mist'] or regexMist10Hour == ['mist'] or regexMist10Hour == ['Fog'] or regexMist10Hour == ['fog']:
        weatherAPI10HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")


    #11 Hour Forecast
    weatherAPI11HourData = weatherAPIData['forecast']
    weatherAPI11HourData = weatherAPI11HourData['forecastday']
    weatherAPI11HourData = weatherAPI11HourData[0]
    weatherAPI11HourData = weatherAPI11HourData['hour']
    weatherAPI11HourData = weatherAPI11HourData[10]
    weatherAPI11HourDataConditionTime = weatherAPI11HourData['time']
    weatherAPI11HourDataConditionTime = weatherAPI11HourDataConditionTime.split(" ")
    print(weatherAPI11HourDataConditionTime)
    weatherAPI11HourDataConditionTime = weatherAPI11HourDataConditionTime[1]
    print(weatherAPI11HourDataConditionTime)
    weatherAPI11HourDataConditionTime = weatherAPI11HourDataConditionTime.split(":")
    print(weatherAPI11HourDataConditionTime)
    weatherAPI11HourDataConditionTime = weatherAPI11HourDataConditionTime[0]
    print(weatherAPI11HourDataConditionTime)
    weatherAPI11HourDataTemperature = weatherAPI11HourData['temp_c']
    print(weatherAPI11HourDataTemperature)
    weatherAPI11HourDataTemperature = round(weatherAPI11HourDataTemperature, 0)
    weatherAPI11HourDataTemperature = int(weatherAPI11HourDataTemperature)
    weatherAPI11HourDataTemperature = str(weatherAPI11HourDataTemperature) + "°C"
    print(weatherAPI11HourDataTemperature)
    weatherAPI11HourDataCondition = weatherAPI11HourData['condition']
    print(weatherAPI11HourDataCondition)
    weatherAPI11HourDataCondition = weatherAPI11HourDataCondition['text']
    print(weatherAPI11HourDataCondition)

    regexThunder11Hour = re.findall("Thunder|thunder", weatherAPI11HourDataCondition)
    regexRain11Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI11HourDataCondition)
    regexCloud11Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI11HourDataCondition)
    regexClear11Hour = re.findall("Clear|clear|Sun|sun", weatherAPI11HourDataCondition)
    regexSnow11Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI11HourDataCondition)
    regexWind11Hour = re.findall("Wind|wind", weatherAPI11HourDataCondition)
    regexHail11Hour = re.findall("Hail|hail", weatherAPI11HourDataCondition)
    regexMist11Hour = re.findall("Mist|mist|Fog|fog", weatherAPI11HourDataCondition)

    if regexThunder11Hour == ['Thunder'] or regexThunder11Hour == ['thunder']:
        weatherAPI11HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain11Hour == ['Rain'] or regexRain11Hour == ['rain'] or regexRain11Hour == [
        'Shower'] or regexRain11Hour == ['shower'] or regexRain11Hour == ['Drizzle'] or regexRain11Hour == [
        'drizzle']:
        weatherAPI11HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud11Hour == ['Cloud'] or regexCloud11Hour == ['cloud'] or regexCloud11Hour == [
        'Overcast'] or regexCloud11Hour == ['overcast'] or regexCloud11Hour == ['Cloudy'] or regexCloud11Hour == [
        'cloudy']:
        weatherAPI11HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear11Hour == ['Clear'] or regexClear11Hour == ['clear'] or regexClear11Hour == [
        'Sun'] or regexClear11Hour == ['sun']:
        weatherAPI11HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow11Hour == ['Snow'] or regexSnow11Hour == ['snow'] or regexSnow11Hour == [
        'Sleet'] or regexSnow11Hour == ['sleet']:
        weatherAPI11HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind11Hour == ['Wind'] or regexWind11Hour == ['wind']:
        weatherAPI11HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail11Hour == ['Hail'] or regexHail11Hour == ['hail']:
        weatherAPI11HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist11Hour == ['Mist'] or regexMist11Hour == ['mist'] or regexMist11Hour == ['Fog'] or regexMist11Hour == ['fog']:
        weatherAPI11HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")

    #12 Hour Forecast
    weatherAPI12HourData = weatherAPIData['forecast']
    weatherAPI12HourData = weatherAPI12HourData['forecastday']
    weatherAPI12HourData = weatherAPI12HourData[0]
    weatherAPI12HourData = weatherAPI12HourData['hour']
    weatherAPI12HourData = weatherAPI12HourData[11]
    weatherAPI12HourDataConditionTime = weatherAPI12HourData['time']
    weatherAPI12HourDataConditionTime = weatherAPI12HourDataConditionTime.split(" ")
    print(weatherAPI12HourDataConditionTime)
    weatherAPI12HourDataConditionTime = weatherAPI12HourDataConditionTime[1]
    print(weatherAPI12HourDataConditionTime)
    weatherAPI12HourDataConditionTime = weatherAPI12HourDataConditionTime.split(":")
    print(weatherAPI12HourDataConditionTime)
    weatherAPI12HourDataConditionTime = weatherAPI12HourDataConditionTime[0]
    print(weatherAPI12HourDataConditionTime)
    weatherAPI12HourDataTemperature = weatherAPI12HourData['temp_c']
    print(weatherAPI12HourDataTemperature)
    weatherAPI12HourDataTemperature = round(weatherAPI12HourDataTemperature, 0)
    weatherAPI12HourDataTemperature = int(weatherAPI12HourDataTemperature)
    weatherAPI12HourDataTemperature = str(weatherAPI12HourDataTemperature) + "°C"
    print(weatherAPI12HourDataTemperature)
    weatherAPI12HourDataCondition = weatherAPI12HourData['condition']
    print(weatherAPI12HourDataCondition)
    weatherAPI12HourDataCondition = weatherAPI12HourDataCondition['text']
    print(weatherAPI12HourDataCondition)

    regexThunder12Hour = re.findall("Thunder|thunder", weatherAPI12HourDataCondition)
    regexRain12Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI12HourDataCondition)
    regexCloud12Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI12HourDataCondition)
    regexClear12Hour = re.findall("Clear|clear|Sun|sun", weatherAPI12HourDataCondition)
    regexSnow12Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI12HourDataCondition)
    regexWind12Hour = re.findall("Wind|wind", weatherAPI12HourDataCondition)
    regexHail12Hour = re.findall("Hail|hail", weatherAPI12HourDataCondition)
    regexMist12Hour = re.findall("Mist|mist|Fog|fog", weatherAPI12HourDataCondition)

    if regexThunder12Hour == ['Thunder'] or regexThunder12Hour == ['thunder']:
        weatherAPI12HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain12Hour == ['Rain'] or regexRain12Hour == ['rain'] or regexRain12Hour == [
        'Shower'] or regexRain12Hour == ['shower'] or regexRain12Hour == ['Drizzle'] or regexRain12Hour == [
        'drizzle']:
        weatherAPI12HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud12Hour == ['Cloud'] or regexCloud12Hour == ['cloud'] or regexCloud12Hour == [
        'Overcast'] or regexCloud12Hour == ['overcast'] or regexCloud12Hour == ['Cloudy'] or regexCloud12Hour == [
        'cloudy']:
        weatherAPI12HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear12Hour == ['Clear'] or regexClear12Hour == ['clear'] or regexClear12Hour == [
        'Sun'] or regexClear12Hour == ['sun']:
        weatherAPI12HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow12Hour == ['Snow'] or regexSnow12Hour == ['snow'] or regexSnow12Hour == [
        'Sleet'] or regexSnow12Hour == ['sleet']:
        weatherAPI12HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind12Hour == ['Wind'] or regexWind12Hour == ['wind']:
        weatherAPI12HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail12Hour == ['Hail'] or regexHail12Hour == ['hail']:
        weatherAPI12HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist12Hour == ['Mist'] or regexMist12Hour == ['mist'] or regexMist12Hour == ['Fog'] or regexMist12Hour == ['fog']:
        weatherAPI12HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")

    #13 Hour Forecast
    weatherAPI13HourData = weatherAPIData['forecast']
    weatherAPI13HourData = weatherAPI13HourData['forecastday']
    weatherAPI13HourData = weatherAPI13HourData[0]
    weatherAPI13HourData = weatherAPI13HourData['hour']
    weatherAPI13HourData = weatherAPI13HourData[12]
    weatherAPI13HourDataConditionTime = weatherAPI13HourData['time']
    weatherAPI13HourDataConditionTime = weatherAPI13HourDataConditionTime.split(" ")
    print(weatherAPI13HourDataConditionTime)
    weatherAPI13HourDataConditionTime = weatherAPI13HourDataConditionTime[1]
    print(weatherAPI13HourDataConditionTime)
    weatherAPI13HourDataConditionTime = weatherAPI13HourDataConditionTime.split(":")
    print(weatherAPI13HourDataConditionTime)
    weatherAPI13HourDataConditionTime = weatherAPI13HourDataConditionTime[0]
    print(weatherAPI13HourDataConditionTime)
    weatherAPI13HourDataTemperature = weatherAPI13HourData['temp_c']
    print(weatherAPI13HourDataTemperature)
    weatherAPI13HourDataTemperature = round(weatherAPI13HourDataTemperature, 0)
    weatherAPI13HourDataTemperature = int(weatherAPI13HourDataTemperature)
    weatherAPI13HourDataTemperature = str(weatherAPI13HourDataTemperature) + "°C"
    print(weatherAPI13HourDataTemperature)
    weatherAPI13HourDataCondition = weatherAPI13HourData['condition']
    print(weatherAPI13HourDataCondition)
    weatherAPI13HourDataCondition = weatherAPI13HourDataCondition['text']
    print(weatherAPI13HourDataCondition)

    regexThunder13Hour = re.findall("Thunder|thunder", weatherAPI13HourDataCondition)
    regexRain13Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI13HourDataCondition)
    regexCloud13Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI13HourDataCondition)
    regexClear13Hour = re.findall("Clear|clear|Sun|sun", weatherAPI13HourDataCondition)
    regexSnow13Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI13HourDataCondition)
    regexWind13Hour = re.findall("Wind|wind", weatherAPI13HourDataCondition)
    regexHail13Hour = re.findall("Hail|hail", weatherAPI13HourDataCondition)
    regexMist13Hour = re.findall("Mist|mist|Fog|fog", weatherAPI13HourDataCondition)

    if regexThunder13Hour == ['Thunder'] or regexThunder13Hour == ['thunder']:
        weatherAPI13HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain13Hour == ['Rain'] or regexRain13Hour == ['rain'] or regexRain13Hour == [
        'Shower'] or regexRain13Hour == ['shower'] or regexRain13Hour == ['Drizzle'] or regexRain13Hour == [
        'drizzle']:
        weatherAPI13HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud13Hour == ['Cloud'] or regexCloud13Hour == ['cloud'] or regexCloud13Hour == [
        'Overcast'] or regexCloud13Hour == ['overcast'] or regexCloud13Hour == ['Cloudy'] or regexCloud13Hour == [
        'cloudy']:
        weatherAPI13HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear13Hour == ['Clear'] or regexClear13Hour == ['clear'] or regexClear13Hour == [
        'Sun'] or regexClear13Hour == ['sun']:
        weatherAPI13HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow13Hour == ['Snow'] or regexSnow13Hour == ['snow'] or regexSnow13Hour == [
        'Sleet'] or regexSnow13Hour == ['sleet']:
        weatherAPI13HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind13Hour == ['Wind'] or regexWind13Hour == ['wind']:
        weatherAPI13HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail13Hour == ['Hail'] or regexHail13Hour == ['hail']:
        weatherAPI13HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist13Hour == ['Mist'] or regexMist13Hour == ['mist'] or regexMist13Hour == ['Fog'] or regexMist13Hour == ['fog']:
        weatherAPI13HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")

    #14 Hour Forecast
    weatherAPI14HourData = weatherAPIData['forecast']
    weatherAPI14HourData = weatherAPI14HourData['forecastday']
    weatherAPI14HourData = weatherAPI14HourData[0]
    weatherAPI14HourData = weatherAPI14HourData['hour']
    weatherAPI14HourData = weatherAPI14HourData[13]
    weatherAPI14HourDataConditionTime = weatherAPI14HourData['time']
    weatherAPI14HourDataConditionTime = weatherAPI14HourDataConditionTime.split(" ")
    print(weatherAPI14HourDataConditionTime)
    weatherAPI14HourDataConditionTime = weatherAPI14HourDataConditionTime[1]
    print(weatherAPI14HourDataConditionTime)
    weatherAPI14HourDataConditionTime = weatherAPI14HourDataConditionTime.split(":")
    print(weatherAPI14HourDataConditionTime)
    weatherAPI14HourDataConditionTime = weatherAPI14HourDataConditionTime[0]
    print(weatherAPI14HourDataConditionTime)
    weatherAPI14HourDataTemperature = weatherAPI14HourData['temp_c']
    print(weatherAPI14HourDataTemperature)
    weatherAPI14HourDataTemperature = round(weatherAPI14HourDataTemperature, 0)
    weatherAPI14HourDataTemperature = int(weatherAPI14HourDataTemperature)
    weatherAPI14HourDataTemperature = str(weatherAPI14HourDataTemperature) + "°C"
    print(weatherAPI14HourDataTemperature)
    weatherAPI14HourDataCondition = weatherAPI14HourData['condition']
    print(weatherAPI14HourDataCondition)
    weatherAPI14HourDataCondition = weatherAPI14HourDataCondition['text']
    print(weatherAPI14HourDataCondition)

    regexThunder14Hour = re.findall("Thunder|thunder", weatherAPI14HourDataCondition)
    regexRain14Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI14HourDataCondition)
    regexCloud14Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI14HourDataCondition)
    regexClear14Hour = re.findall("Clear|clear|Sun|sun", weatherAPI14HourDataCondition)
    regexSnow14Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI14HourDataCondition)
    regexWind14Hour = re.findall("Wind|wind", weatherAPI14HourDataCondition)
    regexHail14Hour = re.findall("Hail|hail", weatherAPI14HourDataCondition)
    regexMist14Hour = re.findall("Mist|mist|Fog|fog", weatherAPI14HourDataCondition)

    if regexThunder14Hour == ['Thunder'] or regexThunder14Hour == ['thunder']:
        weatherAPI14HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain14Hour == ['Rain'] or regexRain14Hour == ['rain'] or regexRain14Hour == [
        'Shower'] or regexRain14Hour == ['shower'] or regexRain14Hour == ['Drizzle'] or regexRain14Hour == [
        'drizzle']:
        weatherAPI14HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud14Hour == ['Cloud'] or regexCloud14Hour == ['cloud'] or regexCloud14Hour == [
        'Overcast'] or regexCloud14Hour == ['overcast'] or regexCloud14Hour == ['Cloudy'] or regexCloud14Hour == [
        'cloudy']:
        weatherAPI14HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear14Hour == ['Clear'] or regexClear14Hour == ['clear'] or regexClear14Hour == [
        'Sun'] or regexClear14Hour == ['sun']:
        weatherAPI14HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow14Hour == ['Snow'] or regexSnow14Hour == ['snow'] or regexSnow14Hour == [
        'Sleet'] or regexSnow14Hour == ['sleet']:
        weatherAPI14HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind14Hour == ['Wind'] or regexWind14Hour == ['wind']:
        weatherAPI14HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail14Hour == ['Hail'] or regexHail14Hour == ['hail']:
        weatherAPI14HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist14Hour == ['Mist'] or regexMist14Hour == ['mist'] or regexMist14Hour == ['Fog'] or regexMist14Hour == ['fog']:
        weatherAPI14HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")

    #15 Hour Forecast
    weatherAPI15HourData = weatherAPIData['forecast']
    weatherAPI15HourData = weatherAPI15HourData['forecastday']
    weatherAPI15HourData = weatherAPI15HourData[0]
    weatherAPI15HourData = weatherAPI15HourData['hour']
    weatherAPI15HourData = weatherAPI15HourData[14]
    weatherAPI15HourDataConditionTime = weatherAPI15HourData['time']
    weatherAPI15HourDataConditionTime = weatherAPI15HourDataConditionTime.split(" ")
    print(weatherAPI15HourDataConditionTime)
    weatherAPI15HourDataConditionTime = weatherAPI15HourDataConditionTime[1]
    print(weatherAPI15HourDataConditionTime)
    weatherAPI15HourDataConditionTime = weatherAPI15HourDataConditionTime.split(":")
    print(weatherAPI15HourDataConditionTime)
    weatherAPI15HourDataConditionTime = weatherAPI15HourDataConditionTime[0]
    print(weatherAPI15HourDataConditionTime)
    weatherAPI15HourDataTemperature = weatherAPI15HourData['temp_c']
    print(weatherAPI15HourDataTemperature)
    weatherAPI15HourDataTemperature = round(weatherAPI15HourDataTemperature, 0)
    weatherAPI15HourDataTemperature = int(weatherAPI15HourDataTemperature)
    weatherAPI15HourDataTemperature = str(weatherAPI15HourDataTemperature) + "°C"
    print(weatherAPI15HourDataTemperature)
    weatherAPI15HourDataCondition = weatherAPI15HourData['condition']
    print(weatherAPI15HourDataCondition)
    weatherAPI15HourDataCondition = weatherAPI15HourDataCondition['text']
    print(weatherAPI15HourDataCondition)

    regexThunder15Hour = re.findall("Thunder|thunder", weatherAPI15HourDataCondition)
    regexRain15Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI15HourDataCondition)
    regexCloud15Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI15HourDataCondition)
    regexClear15Hour = re.findall("Clear|clear|Sun|sun", weatherAPI15HourDataCondition)
    regexSnow15Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI15HourDataCondition)
    regexWind15Hour = re.findall("Wind|wind", weatherAPI15HourDataCondition)
    regexHail15Hour = re.findall("Hail|hail", weatherAPI15HourDataCondition)
    regexMist15Hour = re.findall("Mist|mist|Fog|fog", weatherAPI15HourDataCondition)

    if regexThunder15Hour == ['Thunder'] or regexThunder15Hour == ['thunder']:
        weatherAPI15HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain15Hour == ['Rain'] or regexRain15Hour == ['rain'] or regexRain15Hour == [
        'Shower'] or regexRain15Hour == ['shower'] or regexRain15Hour == ['Drizzle'] or regexRain15Hour == [
        'drizzle']:
        weatherAPI15HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud15Hour == ['Cloud'] or regexCloud15Hour == ['cloud'] or regexCloud15Hour == [
        'Overcast'] or regexCloud15Hour == ['overcast'] or regexCloud15Hour == ['Cloudy'] or regexCloud15Hour == [
        'cloudy']:
        weatherAPI15HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear15Hour == ['Clear'] or regexClear15Hour == ['clear'] or regexClear15Hour == [
        'Sun'] or regexClear15Hour == ['sun']:
        weatherAPI15HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow15Hour == ['Snow'] or regexSnow15Hour == ['snow'] or regexSnow15Hour == [
        'Sleet'] or regexSnow15Hour == ['sleet']:
        weatherAPI15HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind15Hour == ['Wind'] or regexWind15Hour == ['wind']:
        weatherAPI15HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail15Hour == ['Hail'] or regexHail15Hour == ['hail']:
        weatherAPI15HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist15Hour == ['Mist'] or regexMist15Hour == ['mist'] or regexMist15Hour == ['Fog'] or regexMist15Hour == ['fog']:
        weatherAPI15HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")

    #16 Hour Forecast
    weatherAPI16HourData = weatherAPIData['forecast']
    weatherAPI16HourData = weatherAPI16HourData['forecastday']
    weatherAPI16HourData = weatherAPI16HourData[0]
    weatherAPI16HourData = weatherAPI16HourData['hour']
    weatherAPI16HourData = weatherAPI16HourData[15]
    weatherAPI16HourDataConditionTime = weatherAPI16HourData['time']
    weatherAPI16HourDataConditionTime = weatherAPI16HourDataConditionTime.split(" ")
    print(weatherAPI16HourDataConditionTime)
    weatherAPI16HourDataConditionTime = weatherAPI16HourDataConditionTime[1]
    print(weatherAPI16HourDataConditionTime)
    weatherAPI16HourDataConditionTime = weatherAPI16HourDataConditionTime.split(":")
    print(weatherAPI16HourDataConditionTime)
    weatherAPI16HourDataConditionTime = weatherAPI16HourDataConditionTime[0]
    print(weatherAPI16HourDataConditionTime)
    weatherAPI16HourDataTemperature = weatherAPI16HourData['temp_c']
    print(weatherAPI16HourDataTemperature)
    weatherAPI16HourDataTemperature = round(weatherAPI16HourDataTemperature, 0)
    weatherAPI16HourDataTemperature = int(weatherAPI16HourDataTemperature)
    weatherAPI16HourDataTemperature = str(weatherAPI16HourDataTemperature) + "°C"
    print(weatherAPI16HourDataTemperature)
    weatherAPI16HourDataCondition = weatherAPI16HourData['condition']
    print(weatherAPI16HourDataCondition)
    weatherAPI16HourDataCondition = weatherAPI16HourDataCondition['text']
    print(weatherAPI16HourDataCondition)

    regexThunder16Hour = re.findall("Thunder|thunder", weatherAPI16HourDataCondition)
    regexRain16Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI16HourDataCondition)
    regexCloud16Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI16HourDataCondition)
    regexClear16Hour = re.findall("Clear|clear|Sun|sun", weatherAPI16HourDataCondition)
    regexSnow16Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI16HourDataCondition)
    regexWind16Hour = re.findall("Wind|wind", weatherAPI16HourDataCondition)
    regexHail16Hour = re.findall("Hail|hail", weatherAPI16HourDataCondition)
    regexMist16Hour = re.findall("Mist|mist|Fog|fog", weatherAPI16HourDataCondition)

    if regexThunder16Hour == ['Thunder'] or regexThunder16Hour == ['thunder']:
        weatherAPI16HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain16Hour == ['Rain'] or regexRain16Hour == ['rain'] or regexRain16Hour == [
        'Shower'] or regexRain16Hour == ['shower'] or regexRain16Hour == ['Drizzle'] or regexRain16Hour == [
        'drizzle']:
        weatherAPI16HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud16Hour == ['Cloud'] or regexCloud16Hour == ['cloud'] or regexCloud16Hour == [
        'Overcast'] or regexCloud16Hour == ['overcast'] or regexCloud16Hour == ['Cloudy'] or regexCloud16Hour == [
        'cloudy']:
        weatherAPI16HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear16Hour == ['Clear'] or regexClear16Hour == ['clear'] or regexClear16Hour == [
        'Sun'] or regexClear16Hour == ['sun']:
        weatherAPI16HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow16Hour == ['Snow'] or regexSnow16Hour == ['snow'] or regexSnow16Hour == [
        'Sleet'] or regexSnow16Hour == ['sleet']:
        weatherAPI16HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind16Hour == ['Wind'] or regexWind16Hour == ['wind']:
        weatherAPI16HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail16Hour == ['Hail'] or regexHail16Hour == ['hail']:
        weatherAPI16HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist16Hour == ['Mist'] or regexMist16Hour == ['mist'] or regexMist16Hour == ['Fog'] or regexMist16Hour == ['fog']:
        weatherAPI16HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")


    #17 Hour Forecast
    weatherAPI17HourData = weatherAPIData['forecast']
    weatherAPI17HourData = weatherAPI17HourData['forecastday']
    weatherAPI17HourData = weatherAPI17HourData[0]
    weatherAPI17HourData = weatherAPI17HourData['hour']
    weatherAPI17HourData = weatherAPI17HourData[16]
    weatherAPI17HourDataConditionTime = weatherAPI17HourData['time']
    weatherAPI17HourDataConditionTime = weatherAPI17HourDataConditionTime.split(" ")
    print(weatherAPI17HourDataConditionTime)
    weatherAPI17HourDataConditionTime = weatherAPI17HourDataConditionTime[1]
    print(weatherAPI17HourDataConditionTime)
    weatherAPI17HourDataConditionTime = weatherAPI17HourDataConditionTime.split(":")
    print(weatherAPI17HourDataConditionTime)
    weatherAPI17HourDataConditionTime = weatherAPI17HourDataConditionTime[0]
    print(weatherAPI17HourDataConditionTime)
    weatherAPI17HourDataTemperature = weatherAPI17HourData['temp_c']
    print(weatherAPI17HourDataTemperature)
    weatherAPI17HourDataTemperature = round(weatherAPI17HourDataTemperature, 0)
    weatherAPI17HourDataTemperature = int(weatherAPI17HourDataTemperature)
    weatherAPI17HourDataTemperature = str(weatherAPI17HourDataTemperature) + "°C"
    print(weatherAPI17HourDataTemperature)
    weatherAPI17HourDataCondition = weatherAPI17HourData['condition']
    print(weatherAPI17HourDataCondition)
    weatherAPI17HourDataCondition = weatherAPI17HourDataCondition['text']
    print(weatherAPI17HourDataCondition)

    regexThunder17Hour = re.findall("Thunder|thunder", weatherAPI17HourDataCondition)
    regexRain17Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI17HourDataCondition)
    regexCloud17Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI17HourDataCondition)
    regexClear17Hour = re.findall("Clear|clear|Sun|sun", weatherAPI17HourDataCondition)
    regexSnow17Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI17HourDataCondition)
    regexWind17Hour = re.findall("Wind|wind", weatherAPI17HourDataCondition)
    regexHail17Hour = re.findall("Hail|hail", weatherAPI17HourDataCondition)
    regexMist17Hour = re.findall("Mist|mist|Fog|fog", weatherAPI17HourDataCondition)

    if regexThunder17Hour == ['Thunder'] or regexThunder17Hour == ['thunder']:
        weatherAPI17HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain17Hour == ['Rain'] or regexRain17Hour == ['rain'] or regexRain17Hour == [
        'Shower'] or regexRain17Hour == ['shower'] or regexRain17Hour == ['Drizzle'] or regexRain17Hour == [
        'drizzle']:
        weatherAPI17HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud17Hour == ['Cloud'] or regexCloud17Hour == ['cloud'] or regexCloud17Hour == [
        'Overcast'] or regexCloud17Hour == ['overcast'] or regexCloud17Hour == ['Cloudy'] or regexCloud17Hour == [
        'cloudy']:
        weatherAPI17HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear17Hour == ['Clear'] or regexClear17Hour == ['clear'] or regexClear17Hour == [
        'Sun'] or regexClear17Hour == ['sun']:
        weatherAPI17HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow17Hour == ['Snow'] or regexSnow17Hour == ['snow'] or regexSnow17Hour == [
        'Sleet'] or regexSnow17Hour == ['sleet']:
        weatherAPI17HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind17Hour == ['Wind'] or regexWind17Hour == ['wind']:
        weatherAPI17HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail17Hour == ['Hail'] or regexHail17Hour == ['hail']:
        weatherAPI17HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist17Hour == ['Mist'] or regexMist17Hour == ['mist'] or regexMist17Hour == ['Fog'] or regexMist17Hour == ['fog']:
        weatherAPI17HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")

    #18 Hour Forecast
    weatherAPI18HourData = weatherAPIData['forecast']
    weatherAPI18HourData = weatherAPI18HourData['forecastday']
    weatherAPI18HourData = weatherAPI18HourData[0]
    weatherAPI18HourData = weatherAPI18HourData['hour']
    weatherAPI18HourData = weatherAPI18HourData[17]
    weatherAPI18HourDataConditionTime = weatherAPI18HourData['time']
    weatherAPI18HourDataConditionTime = weatherAPI18HourDataConditionTime.split(" ")
    print(weatherAPI18HourDataConditionTime)
    weatherAPI18HourDataConditionTime = weatherAPI18HourDataConditionTime[1]
    print(weatherAPI18HourDataConditionTime)
    weatherAPI18HourDataConditionTime = weatherAPI18HourDataConditionTime.split(":")
    print(weatherAPI18HourDataConditionTime)
    weatherAPI18HourDataConditionTime = weatherAPI18HourDataConditionTime[0]
    print(weatherAPI18HourDataConditionTime)
    weatherAPI18HourDataTemperature = weatherAPI18HourData['temp_c']
    print(weatherAPI18HourDataTemperature)
    weatherAPI18HourDataTemperature = round(weatherAPI18HourDataTemperature, 0)
    weatherAPI18HourDataTemperature = int(weatherAPI18HourDataTemperature)
    weatherAPI18HourDataTemperature = str(weatherAPI18HourDataTemperature) + "°C"
    print(weatherAPI18HourDataTemperature)
    weatherAPI18HourDataCondition = weatherAPI18HourData['condition']
    print(weatherAPI18HourDataCondition)
    weatherAPI18HourDataCondition = weatherAPI18HourDataCondition['text']
    print(weatherAPI18HourDataCondition)

    regexThunder18Hour = re.findall("Thunder|thunder", weatherAPI18HourDataCondition)
    regexRain18Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI18HourDataCondition)
    regexCloud18Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI18HourDataCondition)
    regexClear18Hour = re.findall("Clear|clear|Sun|sun", weatherAPI18HourDataCondition)
    regexSnow18Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI18HourDataCondition)
    regexWind18Hour = re.findall("Wind|wind", weatherAPI18HourDataCondition)
    regexHail18Hour = re.findall("Hail|hail", weatherAPI18HourDataCondition)
    regexMist18Hour = re.findall("Mist|mist|Fog|fog", weatherAPI18HourDataCondition)

    if regexThunder18Hour == ['Thunder'] or regexThunder18Hour == ['thunder']:
        weatherAPI18HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain18Hour == ['Rain'] or regexRain18Hour == ['rain'] or regexRain18Hour == [
        'Shower'] or regexRain18Hour == ['shower'] or regexRain18Hour == ['Drizzle'] or regexRain18Hour == [
        'drizzle']:
        weatherAPI18HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud18Hour == ['Cloud'] or regexCloud18Hour == ['cloud'] or regexCloud18Hour == [
        'Overcast'] or regexCloud18Hour == ['overcast'] or regexCloud18Hour == ['Cloudy'] or regexCloud18Hour == [
        'cloudy']:
        weatherAPI18HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear18Hour == ['Clear'] or regexClear18Hour == ['clear'] or regexClear18Hour == [
        'Sun'] or regexClear18Hour == ['sun']:
        weatherAPI18HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow18Hour == ['Snow'] or regexSnow18Hour == ['snow'] or regexSnow18Hour == [
        'Sleet'] or regexSnow18Hour == ['sleet']:
        weatherAPI18HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind18Hour == ['Wind'] or regexWind18Hour == ['wind']:
        weatherAPI18HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail18Hour == ['Hail'] or regexHail18Hour == ['hail']:
        weatherAPI18HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist18Hour == ['Mist'] or regexMist18Hour == ['mist'] or regexMist18Hour == ['Fog'] or regexMist18Hour == ['fog']:
        weatherAPI18HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")

    #19 Hour Forecast
    weatherAPI19HourData = weatherAPIData['forecast']
    weatherAPI19HourData = weatherAPI19HourData['forecastday']
    weatherAPI19HourData = weatherAPI19HourData[0]
    weatherAPI19HourData = weatherAPI19HourData['hour']
    weatherAPI19HourData = weatherAPI19HourData[18]
    weatherAPI19HourDataConditionTime = weatherAPI19HourData['time']
    weatherAPI19HourDataConditionTime = weatherAPI19HourDataConditionTime.split(" ")
    print(weatherAPI19HourDataConditionTime)
    weatherAPI19HourDataConditionTime = weatherAPI19HourDataConditionTime[1]
    print(weatherAPI19HourDataConditionTime)
    weatherAPI19HourDataConditionTime = weatherAPI19HourDataConditionTime.split(":")
    print(weatherAPI19HourDataConditionTime)
    weatherAPI19HourDataConditionTime = weatherAPI19HourDataConditionTime[0]
    print(weatherAPI19HourDataConditionTime)
    weatherAPI19HourDataTemperature = weatherAPI19HourData['temp_c']
    print(weatherAPI19HourDataTemperature)
    weatherAPI19HourDataTemperature = round(weatherAPI19HourDataTemperature, 0)
    weatherAPI19HourDataTemperature = int(weatherAPI19HourDataTemperature)
    weatherAPI19HourDataTemperature = str(weatherAPI19HourDataTemperature) + "°C"
    print(weatherAPI19HourDataTemperature)
    weatherAPI19HourDataCondition = weatherAPI19HourData['condition']
    print(weatherAPI19HourDataCondition)
    weatherAPI19HourDataCondition = weatherAPI19HourDataCondition['text']
    print(weatherAPI19HourDataCondition)

    regexThunder19Hour = re.findall("Thunder|thunder", weatherAPI19HourDataCondition)
    regexRain19Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI19HourDataCondition)
    regexCloud19Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI19HourDataCondition)
    regexClear19Hour = re.findall("Clear|clear|Sun|sun", weatherAPI19HourDataCondition)
    regexSnow19Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI19HourDataCondition)
    regexWind19Hour = re.findall("Wind|wind", weatherAPI19HourDataCondition)
    regexHail19Hour = re.findall("Hail|hail", weatherAPI19HourDataCondition)
    regexMist19Hour = re.findall("Mist|mist|Fog|fog", weatherAPI19HourDataCondition)

    if regexThunder19Hour == ['Thunder'] or regexThunder19Hour == ['thunder']:
        weatherAPI19HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain19Hour == ['Rain'] or regexRain19Hour == ['rain'] or regexRain19Hour == [
        'Shower'] or regexRain19Hour == ['shower'] or regexRain19Hour == ['Drizzle'] or regexRain19Hour == [
        'drizzle']:
        weatherAPI19HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud19Hour == ['Cloud'] or regexCloud19Hour == ['cloud'] or regexCloud19Hour == [
        'Overcast'] or regexCloud19Hour == ['overcast'] or regexCloud19Hour == ['Cloudy'] or regexCloud19Hour == [
        'cloudy']:
        weatherAPI19HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear19Hour == ['Clear'] or regexClear19Hour == ['clear'] or regexClear19Hour == [
        'Sun'] or regexClear19Hour == ['sun']:
        weatherAPI19HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow19Hour == ['Snow'] or regexSnow19Hour == ['snow'] or regexSnow19Hour == [
        'Sleet'] or regexSnow19Hour == ['sleet']:
        weatherAPI19HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind19Hour == ['Wind'] or regexWind19Hour == ['wind']:
        weatherAPI19HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail19Hour == ['Hail'] or regexHail19Hour == ['hail']:
        weatherAPI19HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist19Hour == ['Mist'] or regexMist19Hour == ['mist'] or regexMist19Hour == ['Fog'] or regexMist19Hour == ['fog']:
        weatherAPI19HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")

    print("weatherAPI19HourDataConditionIcon", weatherAPI19HourDataConditionIcon)

    # 20 Hour Forecast
    weatherAPI20HourData = weatherAPIData['forecast']
    weatherAPI20HourData = weatherAPI20HourData['forecastday']
    weatherAPI20HourData = weatherAPI20HourData[0]
    weatherAPI20HourData = weatherAPI20HourData['hour']
    weatherAPI20HourData = weatherAPI20HourData[19]
    weatherAPI20HourDataConditionTime = weatherAPI20HourData['time']
    weatherAPI20HourDataConditionTime = weatherAPI20HourDataConditionTime.split(" ")
    print(weatherAPI20HourDataConditionTime)
    weatherAPI20HourDataConditionTime = weatherAPI20HourDataConditionTime[1]
    print(weatherAPI20HourDataConditionTime)
    weatherAPI20HourDataConditionTime = weatherAPI20HourDataConditionTime.split(":")
    print(weatherAPI20HourDataConditionTime)
    weatherAPI20HourDataConditionTime = weatherAPI20HourDataConditionTime[0]
    print(weatherAPI20HourDataConditionTime)
    weatherAPI20HourDataTemperature = weatherAPI20HourData['temp_c']
    print(weatherAPI20HourDataTemperature)
    weatherAPI20HourDataTemperature = round(weatherAPI20HourDataTemperature, 0)
    weatherAPI20HourDataTemperature = int(weatherAPI20HourDataTemperature)
    weatherAPI20HourDataTemperature = str(weatherAPI20HourDataTemperature) + "°C"
    print(weatherAPI20HourDataTemperature)
    weatherAPI20HourDataCondition = weatherAPI20HourData['condition']
    print(weatherAPI20HourDataCondition)
    weatherAPI20HourDataCondition = weatherAPI20HourDataCondition['text']
    print(weatherAPI20HourDataCondition)

    regexThunder20Hour = re.findall("Thunder|thunder", weatherAPI20HourDataCondition)
    regexRain20Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI20HourDataCondition)
    regexCloud20Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI20HourDataCondition)
    regexClear20Hour = re.findall("Clear|clear|Sun|sun", weatherAPI20HourDataCondition)
    regexSnow20Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI20HourDataCondition)
    regexWind20Hour = re.findall("Wind|wind", weatherAPI20HourDataCondition)
    regexHail20Hour = re.findall("Hail|hail", weatherAPI20HourDataCondition)
    regexMist20Hour = re.findall("Mist|mist|Fog|fog", weatherAPI20HourDataCondition)

    if regexThunder20Hour == ['Thunder'] or regexThunder20Hour == ['thunder']:
        weatherAPI20HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain20Hour == ['Rain'] or regexRain20Hour == ['rain'] or regexRain20Hour == [
        'Shower'] or regexRain20Hour == ['shower'] or regexRain20Hour == ['Drizzle'] or regexRain20Hour == [
        'drizzle']:
        weatherAPI20HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud20Hour == ['Cloud'] or regexCloud20Hour == ['cloud'] or regexCloud20Hour == [
        'Overcast'] or regexCloud20Hour == ['overcast'] or regexCloud20Hour == ['Cloudy'] or regexCloud20Hour == [
        'cloudy']:
        weatherAPI20HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear20Hour == ['Clear'] or regexClear20Hour == ['clear'] or regexClear20Hour == [
        'Sun'] or regexClear20Hour == ['sun']:
        weatherAPI20HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow20Hour == ['Snow'] or regexSnow20Hour == ['snow'] or regexSnow20Hour == [
        'Sleet'] or regexSnow20Hour == ['sleet']:
        weatherAPI20HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind20Hour == ['Wind'] or regexWind20Hour == ['wind']:
        weatherAPI20HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail20Hour == ['Hail'] or regexHail20Hour == ['hail']:
        weatherAPI20HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist20Hour == ['Mist'] or regexMist20Hour == ['mist'] or regexMist20Hour == ['Fog'] or regexMist20Hour == ['fog']:
        weatherAPI20HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")

    # 21 Hour Forecast
    weatherAPI21HourData = weatherAPIData['forecast']
    weatherAPI21HourData = weatherAPI21HourData['forecastday']
    weatherAPI21HourData = weatherAPI21HourData[0]
    weatherAPI21HourData = weatherAPI21HourData['hour']
    weatherAPI21HourData = weatherAPI21HourData[20]
    weatherAPI21HourDataConditionTime = weatherAPI21HourData['time']
    weatherAPI21HourDataConditionTime = weatherAPI21HourDataConditionTime.split(" ")
    print(weatherAPI21HourDataConditionTime)

    weatherAPI21HourDataConditionTime = weatherAPI21HourDataConditionTime[1]
    print(weatherAPI21HourDataConditionTime)
    weatherAPI21HourDataConditionTime = weatherAPI21HourDataConditionTime.split(":")
    print(weatherAPI21HourDataConditionTime)
    weatherAPI21HourDataConditionTime = weatherAPI21HourDataConditionTime[0]
    print(weatherAPI21HourDataConditionTime)
    weatherAPI21HourDataTemperature = weatherAPI21HourData['temp_c']
    print(weatherAPI21HourDataTemperature)
    weatherAPI21HourDataTemperature = round(weatherAPI21HourDataTemperature, 0)
    weatherAPI21HourDataTemperature = int(weatherAPI21HourDataTemperature)
    weatherAPI21HourDataTemperature = str(weatherAPI21HourDataTemperature) + "°C"
    print(weatherAPI21HourDataTemperature)
    weatherAPI21HourDataCondition = weatherAPI21HourData['condition']
    print(weatherAPI21HourDataCondition)
    weatherAPI21HourDataCondition = weatherAPI21HourDataCondition['text']
    print(weatherAPI21HourDataCondition)

    regexThunder21Hour = re.findall("Thunder|thunder", weatherAPI21HourDataCondition)
    regexRain21Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI21HourDataCondition)
    regexCloud21Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI21HourDataCondition)
    regexClear21Hour = re.findall("Clear|clear|Sun|sun", weatherAPI21HourDataCondition)
    regexSnow21Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI21HourDataCondition)
    regexWind21Hour = re.findall("Wind|wind", weatherAPI21HourDataCondition)
    regexHail21Hour = re.findall("Hail|hail", weatherAPI21HourDataCondition)
    regexMist21Hour = re.findall("Mist|mist|Fog|fog", weatherAPI21HourDataCondition)

    if regexThunder21Hour == ['Thunder'] or regexThunder21Hour == ['thunder']:
        weatherAPI21HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain21Hour == ['Rain'] or regexRain21Hour == ['rain'] or regexRain21Hour == [
        'Shower'] or regexRain21Hour == ['shower'] or regexRain21Hour == ['Drizzle'] or regexRain21Hour == [
        'drizzle']:
        weatherAPI21HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud21Hour == ['Cloud'] or regexCloud21Hour == ['cloud'] or regexCloud21Hour == [
        'Overcast'] or regexCloud21Hour == ['overcast'] or regexCloud21Hour == ['Cloudy'] or regexCloud21Hour == [
        'cloudy']:
        weatherAPI21HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear21Hour == ['Clear'] or regexClear21Hour == ['clear'] or regexClear21Hour == [
        'Sun'] or regexClear21Hour == ['sun']:
        weatherAPI21HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow21Hour == ['Snow'] or regexSnow21Hour == ['snow'] or regexSnow21Hour == [
        'Sleet'] or regexSnow21Hour == ['sleet']:
        weatherAPI21HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind21Hour == ['Wind'] or regexWind21Hour == ['wind']:
        weatherAPI21HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail21Hour == ['Hail'] or regexHail21Hour == ['hail']:
        weatherAPI21HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist21Hour == ['Mist'] or regexMist21Hour == ['mist'] or regexMist21Hour == ['Fog'] or regexMist21Hour == ['fog']:
        weatherAPI21HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")

    # 22 Hour Forecast
    weatherAPI22HourData = weatherAPIData['forecast']
    weatherAPI22HourData = weatherAPI22HourData['forecastday']
    weatherAPI22HourData = weatherAPI22HourData[0]
    weatherAPI22HourData = weatherAPI22HourData['hour']
    weatherAPI22HourData = weatherAPI22HourData[21]
    weatherAPI22HourDataConditionTime = weatherAPI22HourData['time']
    weatherAPI22HourDataConditionTime = weatherAPI22HourDataConditionTime.split(" ")
    print(weatherAPI22HourDataConditionTime)
    weatherAPI22HourDataConditionTime = weatherAPI22HourDataConditionTime[1]
    print(weatherAPI22HourDataConditionTime)
    weatherAPI22HourDataConditionTime = weatherAPI22HourDataConditionTime.split(":")
    print(weatherAPI22HourDataConditionTime)
    weatherAPI22HourDataConditionTime = weatherAPI22HourDataConditionTime[0]
    print(weatherAPI22HourDataConditionTime)
    weatherAPI22HourDataTemperature = weatherAPI22HourData['temp_c']
    print(weatherAPI22HourDataTemperature)
    weatherAPI22HourDataTemperature = round(weatherAPI22HourDataTemperature, 0)
    weatherAPI22HourDataTemperature = int(weatherAPI22HourDataTemperature)
    weatherAPI22HourDataTemperature = str(weatherAPI22HourDataTemperature) + "°C"
    print(weatherAPI22HourDataTemperature)
    weatherAPI22HourDataCondition = weatherAPI22HourData['condition']
    print(weatherAPI22HourDataCondition)
    weatherAPI22HourDataCondition = weatherAPI22HourDataCondition['text']
    print(weatherAPI22HourDataCondition)

    regexThunder22Hour = re.findall("Thunder|thunder", weatherAPI22HourDataCondition)
    regexRain22Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI22HourDataCondition)
    regexCloud22Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI22HourDataCondition)
    regexClear22Hour = re.findall("Clear|clear|Sun|sun", weatherAPI22HourDataCondition)
    regexSnow22Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI22HourDataCondition)
    regexWind22Hour = re.findall("Wind|wind", weatherAPI22HourDataCondition)
    regexHail22Hour = re.findall("Hail|hail", weatherAPI22HourDataCondition)
    regexMist22Hour = re.findall("Mist|mist|Fog|fog", weatherAPI22HourDataCondition)

    if regexThunder22Hour == ['Thunder'] or regexThunder22Hour == ['thunder']:
        weatherAPI22HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain22Hour == ['Rain'] or regexRain22Hour == ['rain'] or regexRain22Hour == [
        'Shower'] or regexRain22Hour == ['shower'] or regexRain22Hour == ['Drizzle'] or regexRain22Hour == [
        'drizzle']:
        weatherAPI22HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud22Hour == ['Cloud'] or regexCloud22Hour == ['cloud'] or regexCloud22Hour == [
        'Overcast'] or regexCloud22Hour == ['overcast'] or regexCloud22Hour == ['Cloudy'] or regexCloud22Hour == [
        'cloudy']:
        weatherAPI22HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear22Hour == ['Clear'] or regexClear22Hour == ['clear'] or regexClear22Hour == [
        'Sun'] or regexClear22Hour == ['sun']:
        weatherAPI22HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow22Hour == ['Snow'] or regexSnow22Hour == ['snow'] or regexSnow22Hour == [
        'Sleet'] or regexSnow22Hour == ['sleet']:
        weatherAPI22HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind22Hour == ['Wind'] or regexWind22Hour == ['wind']:
        weatherAPI22HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail22Hour == ['Hail'] or regexHail22Hour == ['hail']:
        weatherAPI22HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist22Hour == ['Mist'] or regexMist22Hour == ['mist'] or regexMist22Hour == ['Fog'] or regexMist22Hour == ['fog']:
        weatherAPI22HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")

    # 23 Hour Forecast
    weatherAPI23HourData = weatherAPIData['forecast']
    weatherAPI23HourData = weatherAPI23HourData['forecastday']
    weatherAPI23HourData = weatherAPI23HourData[0]
    weatherAPI23HourData = weatherAPI23HourData['hour']
    weatherAPI23HourData = weatherAPI23HourData[22]
    weatherAPI23HourDataConditionTime = weatherAPI23HourData['time']
    weatherAPI23HourDataConditionTime = weatherAPI23HourDataConditionTime.split(" ")
    print(weatherAPI23HourDataConditionTime)
    weatherAPI23HourDataConditionTime = weatherAPI23HourDataConditionTime[1]
    print(weatherAPI23HourDataConditionTime)
    weatherAPI23HourDataConditionTime = weatherAPI23HourDataConditionTime.split(":")
    print(weatherAPI23HourDataConditionTime)
    weatherAPI23HourDataConditionTime = weatherAPI23HourDataConditionTime[0]
    print(weatherAPI23HourDataConditionTime)
    weatherAPI23HourDataTemperature = weatherAPI23HourData['temp_c']
    print(weatherAPI23HourDataTemperature)
    weatherAPI23HourDataTemperature = round(weatherAPI23HourDataTemperature, 0)
    weatherAPI23HourDataTemperature = int(weatherAPI23HourDataTemperature)
    weatherAPI23HourDataTemperature = str(weatherAPI23HourDataTemperature) + "°C"
    print(weatherAPI23HourDataTemperature)
    weatherAPI23HourDataCondition = weatherAPI23HourData['condition']
    print(weatherAPI23HourDataCondition)
    weatherAPI23HourDataCondition = weatherAPI23HourDataCondition['text']
    print(weatherAPI23HourDataCondition)

    regexThunder23Hour = re.findall("Thunder|thunder", weatherAPI23HourDataCondition)
    regexRain23Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI23HourDataCondition)
    regexCloud23Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI23HourDataCondition)
    regexClear23Hour = re.findall("Clear|clear|Sun|sun", weatherAPI23HourDataCondition)
    regexSnow23Hour = re.findall("Snow|snow|Sleet|sleet", weatherAPI23HourDataCondition)
    regexWind23Hour = re.findall("Wind|wind", weatherAPI23HourDataCondition)
    regexHail23Hour = re.findall("Hail|hail", weatherAPI23HourDataCondition)
    regexMist23Hour = re.findall("Mist|mist|Fog|fog", weatherAPI23HourDataCondition)

    if regexThunder23Hour == ['Thunder'] or regexThunder23Hour == ['thunder']:
        weatherAPI23HourDataConditionIcon = "/static/images/thunderstorms.svg"
        print("Regex: Thunder")
    elif regexRain23Hour == ['Rain'] or regexRain23Hour == ['rain'] or regexRain23Hour == [
        'Shower'] or regexRain23Hour == ['shower'] or regexRain23Hour == ['Drizzle'] or regexRain23Hour == [
        'drizzle']:
        weatherAPI23HourDataConditionIcon = "/static/images/rain.svg"
        print("Regex: Rain")
    elif regexCloud23Hour == ['Cloud'] or regexCloud23Hour == ['cloud'] or regexCloud23Hour == [
        'Overcast'] or regexCloud23Hour == ['overcast'] or regexCloud23Hour == ['Cloudy'] or regexCloud23Hour == [
        'cloudy']:
        weatherAPI23HourDataConditionIcon = "/static/images/cloudy.svg"
        print("Regex: Cloud")
    elif regexClear23Hour == ['Clear'] or regexClear23Hour == ['clear'] or regexClear23Hour == [
        'Sun'] or regexClear23Hour == ['sun']:
        weatherAPI23HourDataConditionIcon = "/static/images/sunny.svg"
        print("Regex: Clear")
    elif regexSnow23Hour == ['Snow'] or regexSnow23Hour == ['snow'] or regexSnow23Hour == [
        'Sleet'] or regexSnow23Hour == ['sleet']:
        weatherAPI23HourDataConditionIcon = "/static/images/snow.svg"
        print("Regex: Snow")
    elif regexWind23Hour == ['Wind'] or regexWind23Hour == ['wind']:
        weatherAPI23HourDataConditionIcon = "/static/images/wind.svg"
        print("Regex: Wind")
    elif regexHail23Hour == ['Hail'] or regexHail23Hour == ['hail']:
        weatherAPI23HourDataConditionIcon = "/static/images/hailstones.svg"
        print("Regex: Hail")
    elif regexMist23Hour == ['Mist'] or regexMist23Hour == ['mist'] or regexMist23Hour == ['Fog'] or regexMist23Hour == ['fog']:
        weatherAPI23HourDataConditionIcon = "/static/images/mist.svg"
        print("Regex: Mist")


    data = strTemperatureCelsius1, strHumidity, aqi, aqi_description, strWindSpeed, windDirectionDescription, UV_index, UV_index_description, UV_index_percentage, UV_index_colour, aqi_percentage, aqi_colour, compass, strTemperatureFarenheit, strWindSpeedKMH, openWeatherDataToday, temperatureforecastToday, weatherConditionsTodayIcon, tomorrowDate, weatherConditionsTomorrowIcon, temperatureforecastTomorrow, tomorrowWindSpeed, tomorrowWindDirectionDescription, tomorrowHumidity, ThreeDayDate, weatherConditionsThreeDayIcon, temperatureforecastThreeDay, ThreeDayWindSpeed, ThreeDayWindDirectionDescription, ThreeDayHumidity, FourDayDate, weatherConditionsFourDayIcon, temperatureforecastFourDay, FourDayWindSpeed, FourDayWindDirectionDescription, FourDayHumidity, FiveDayDate, weatherConditionsFiveDayIcon, temperatureforecastFiveDay, FiveDayWindSpeed, FiveDayWindDirectionDescription, FiveDayHumidity, SixDayDate, weatherConditionsSixDayIcon, temperatureforecastSixDay, SixDayWindSpeed, SixDayWindDirectionDescription, SixDayHumidity, weatherAPIDataCurrentTemperature, weatherAPIDataCurrentConditionIcon, weatherAPI01HourDataConditionTime, weatherAPI01HourDataTemperature, weatherAPI01HourDataConditionIcon, weatherAPI02HourDataConditionTime, weatherAPI02HourDataTemperature, weatherAPI02HourDataConditionIcon, weatherAPI03HourDataConditionTime, weatherAPI03HourDataTemperature, weatherAPI03HourDataConditionIcon, weatherAPI04HourDataConditionTime, weatherAPI04HourDataTemperature, weatherAPI04HourDataConditionIcon, weatherAPI05HourDataConditionTime, weatherAPI05HourDataTemperature, weatherAPI05HourDataConditionIcon, weatherAPI06HourDataConditionTime, weatherAPI06HourDataTemperature, weatherAPI06HourDataConditionIcon, weatherAPI07HourDataConditionTime, weatherAPI07HourDataTemperature, weatherAPI07HourDataConditionIcon, weatherAPI08HourDataConditionTime, weatherAPI08HourDataTemperature, weatherAPI08HourDataConditionIcon, weatherAPI09HourDataConditionTime, weatherAPI09HourDataTemperature, weatherAPI09HourDataConditionIcon, weatherAPI10HourDataConditionTime, weatherAPI10HourDataTemperature, weatherAPI10HourDataConditionIcon, weatherAPI11HourDataConditionTime, weatherAPI11HourDataTemperature, weatherAPI11HourDataConditionIcon, weatherAPI12HourDataConditionTime, weatherAPI12HourDataTemperature, weatherAPI12HourDataConditionIcon, weatherAPI13HourDataConditionTime, weatherAPI13HourDataTemperature, weatherAPI13HourDataConditionIcon, weatherAPI14HourDataConditionTime, weatherAPI14HourDataTemperature, weatherAPI14HourDataConditionIcon, weatherAPI15HourDataConditionTime, weatherAPI15HourDataTemperature, weatherAPI15HourDataConditionIcon, weatherAPI16HourDataConditionTime, weatherAPI16HourDataTemperature, weatherAPI16HourDataConditionIcon, weatherAPI17HourDataConditionTime, weatherAPI17HourDataTemperature, weatherAPI17HourDataConditionIcon, weatherAPI18HourDataConditionTime, weatherAPI18HourDataTemperature, weatherAPI18HourDataConditionIcon, weatherAPI19HourDataConditionTime, weatherAPI19HourDataTemperature, weatherAPI19HourDataConditionIcon, weatherAPI20HourDataConditionTime, weatherAPI20HourDataTemperature, weatherAPI20HourDataConditionIcon, weatherAPI21HourDataConditionTime, weatherAPI21HourDataTemperature, weatherAPI21HourDataConditionIcon, weatherAPI22HourDataConditionTime, weatherAPI22HourDataTemperature, weatherAPI22HourDataConditionIcon, weatherAPI23HourDataConditionTime, weatherAPI23HourDataTemperature, weatherAPI23HourDataConditionIcon, strPressure, angle
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

@app.route('/weatherapitest', methods=['GET', 'POST'])
def weatherapitest():
    weatherAPI_key = '33d91967a1b04700807201804242711'
    weatherAPIurl = 'https://api.weatherapi.com/v1/forecast.json?key=' + weatherAPI_key + '&q=IP5 3RE&days=1&aqi=yes&alerts=yes'
    print(weatherAPIurl)
    response = requests.get(weatherAPIurl)
    weatherAPIData = response.json()
    print(weatherAPIData)
    print(type(weatherAPIData))
    weatherAPIDataCurrent = weatherAPIData['current']
    print(weatherAPIDataCurrent)
    weatherAPIDataCurrentTemperature = weatherAPIDataCurrent['temp_c']
    print(weatherAPIDataCurrentTemperature)
    weatherAPIDataCurrentTemperature = str(weatherAPIDataCurrentTemperature) + "°C"
    print(weatherAPIDataCurrentTemperature)
    weatherAPIDataCurrentCondition = weatherAPIDataCurrent['condition']
    print(weatherAPIDataCurrentCondition)
    weatherAPIDataCurrentCondition = weatherAPIDataCurrentCondition['text']
    print(weatherAPIDataCurrentCondition)

    weatherAPI01HourData = weatherAPIData['forecast']
    weatherAPI01HourData = weatherAPI01HourData['forecastday']
    weatherAPI01HourData = weatherAPI01HourData[0]
    weatherAPI01HourData = weatherAPI01HourData['hour']
    weatherAPI01HourData = weatherAPI01HourData[0]
    weatherAPI01HourDataTemperature = weatherAPI01HourData['temp_c']
    print(weatherAPI01HourDataTemperature)
    weatherAPI01HourDataTemperature = str(weatherAPI01HourDataTemperature) + "°C"
    print(weatherAPI01HourDataTemperature)
    weatherAPI01HourDataCondition = weatherAPI01HourData['condition']
    print(weatherAPI01HourDataCondition)
    weatherAPI01HourDataCondition = weatherAPI01HourDataCondition['text']
    print(weatherAPI01HourDataCondition)
    weatherAPI01HourDataConditionTime = weatherAPI01HourData['time']
    print(weatherAPI01HourDataConditionTime)
    weatherAPI01HourDataConditionTime = weatherAPI01HourDataConditionTime.split(" ")
    weatherAPI01HourDataConditionTime = weatherAPI01HourDataConditionTime[1]
    print(weatherAPI01HourDataConditionTime)


    return jsonify(weatherAPIData)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # port number
    app.run(debug=True, host='0.0.0.0', port=port)  # run the application
