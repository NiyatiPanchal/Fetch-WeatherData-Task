# WeatherAPI Flask API

The WeatherAPI Flask API is a simple RESTful API that retrieves current weather data for a given city using the WeatherAPI.com service. The API supports both JSON and XML response formats.

## Table of Contents

<!--ts-->

- [Framework](#framework)
- [Instructions to Run](#instructions-to-run)
<!--te-->

# Framework

**`Flask`** : Flask is a lightweight and easy-to-use web framework that allows us to quickly create web applications and APIs.

# Instructions to Run

To run the API locally, follow these steps:

1. Clone the repository:
   ```yml
   git clone https://github.com/NiyatiPanchal/Fetch-WeatherData-Task.git
   cd weatherapi-flask-api
    ```

2. Install the required dependencies:
    ```yml
    pip install flask requests
    ```

3. Create a **`config.py`** file in the root directory and add your API key:
   ```yml
   API_KEY = 'YOUR_RAPIDAPI_KEY'
   ```

4. Run the Flask API:
   ```yml
   python app.py
   ```

5. The API will be accessible at http://127.0.0.1:5000/.
