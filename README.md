# openweathermap_api

This python library is an api interface for openweathermap api. As of now it only is able to request current weather data.

**[Installation](#installation)**

```
git clone https://github.com/Kosmozir/openweathermap_api.git
cd openweathermap_api
pip install .
```

**[Usage](#usage)**
```py
from openweathermap_api import Client

api_key = "[API KEY HERE]"
client = Client(api_key=api_key)

# Get geocoded data for lon. and lat.
client.geocode("14738", "US")

# Returns a JSON object containing the weather data or an optional flag_xml=True argument to return XML data
get_current_weather = client.current_weather()
```