from flask import Blueprint, render_template, request, jsonify
import requests

weather_bp = Blueprint('weather', __name__)

API_KEY = '8b5aca057d7fa197d03ae7c998a48425'

@weather_bp.route('/')
def homepage():
    return render_template('index.html')

@weather_bp.route('/weather', methods=['GET', 'POST'])
def weather():
    weather_data = None
    error = None
    if request.method == 'POST':
        location = request.form.get('location')
        if location:
            try:
                url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&appid={API_KEY}'
                response = requests.get(url)
                response.raise_for_status()
                weather_data = response.json()
            except Exception as e:
                error = "Failed to retrieve weather data. Please try again."
        else:
            error = "Please enter a location."

    return render_template('weather.html', weather_data=weather_data, error=error)

@weather_bp.route('/projects')
def projects():
    return render_template('projects.html')

@weather_bp.route('/account')
def account():
    return render_template('account.html')

@weather_bp.route("/resume")
def resume():
    return render_template("resume.html")

@weather_bp.route("/about")
def about():
    return render_template("about.html")

@weather_bp.route('/get_weather')
def get_weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if not lat or not lon:
        return jsonify({'error': 'Missing coordinates'}), 400
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={API_KEY}'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return jsonify({
            'location': data.get('name'),
            'temp': data['main']['temp'],
            'condition': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'timezone_offset': data.get('timezone', 0)  # in seconds
        })
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Failed to fetch weather data'}), 500

@weather_bp.route('/get_weather_by_city')
def get_weather_by_city():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'Missing city parameter'}), 400

    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={API_KEY}'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return jsonify({
            'location': data.get('name'),
            'temp': data['main']['temp'],
            'condition': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'timezone_offset': data.get('timezone', 0)  # in seconds
        })
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Failed to fetch weather data for city'}), 500
