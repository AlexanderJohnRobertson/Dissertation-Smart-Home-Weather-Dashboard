"""Flask application for the Smart Home Weather Dashboard Author: S275931."""
from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/temperature')
def temperature():
    return render_template('temperature.html')

@app.route('/humidity')
def humidity():
    return render_template('humidity.html')

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


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # port number
    app.run(debug=True, host='0.0.0.0', port=port)  # run the application
