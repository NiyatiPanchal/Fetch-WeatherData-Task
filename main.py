from flask import Flask, request, jsonify
import requests
import xml.etree.ElementTree as ET
from config import API_KEY

app = Flask(__name__)

def get_weather_data(city):
    url = f'https://weatherapi-com.p.rapidapi.com/current.json?q={city}'
    headers = {
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': 'weatherapi-com.p.rapidapi.com'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        weather = str(int(data['current']['temp_c'])) + ' C'
        temperature = str(data['current']['temp_c'])
        latitude = str(data['location']['lat'])
        longitude = str(data['location']['lon'])
        return weather, temperature, latitude, longitude
    else:
        return None

@app.route('/getCurrentWeather', methods=['POST'])
def get_current_weather():
    try:
        data = request.get_json()
        city = data.get('city')
        output_format = data.get('output_format', 'json')

        if not city:
            return jsonify({"error": "City name is missing in the request body"}), 400

        weather, temperature, latitude, longitude = get_weather_data(city)

        if output_format.lower() == 'json':
            response_data = {
                'Weather': weather,
                'Latitude': latitude,
                'Longitude': longitude,
                'City': f'{city} India',
            }
            return jsonify(response_data)
        elif output_format.lower() == 'xml':
            root = ET.Element('root')
            ET.SubElement(root, 'Temperature').text = temperature
            ET.SubElement(root, 'City').text = f'{city} India'
            ET.SubElement(root, 'Latitude').text = latitude
            ET.SubElement(root, 'Longitude').text = longitude
            xml_response = ET.tostring(root, encoding='utf-8')
            xml_response_with_version = b'<?xml version="1.0" encoding="UTF-8"?>' + xml_response
            return app.response_class(xml_response, content_type='application/xml')
        else:
            return jsonify({"error": "Invalid output_format. Allowed values are 'json' and 'xml'"}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)