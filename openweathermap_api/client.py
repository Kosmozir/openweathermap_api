from . import auth
from . import exceptions
import requests
from .models import Locaation
import xml.etree.ElementTree as ET

class Client():
    def __init__(self, api_key: str):
        auth.auth_api_key(api_key)
        self.api_key = api_key
    
    def geocode(self, zip_code: str, country_code: str):
        """
            Creates a new dataclass with geocoded data from zip code and country code

            args:
                zip_code - required zip code
                country_code - required country code
        """
        geocode_http_request = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={self.api_key}"
        
        try:
            http_response = requests.get(geocode_http_request)
            http_response.raise_for_status()

            geocoded_json_data = http_response.json()

            self.location_data = Locaation(
                geocoded_json_data["zip"],
                geocoded_json_data["name"],
                geocoded_json_data["lat"],
                geocoded_json_data["lon"],
                geocoded_json_data["country"]
            )
        
        except requests.HTTPError as err:
             http_err_response = http_response.json()["message"]

             match http_response.status_code:
                 case 404:
                    raise exceptions.ApiNotFoundError(http_err_response, 404) from err
        

                     

    def current_weather(self, flag_xml: bool = False) -> dict | ET.Element:
        """
        Returns current weather data as a formatted http response from openweather api in the form of JSON or XML

        args:
            flag_xml (bool): optional flag to set xml response

        """
        http_request = f"https://api.openweathermap.org/data/2.5/weather?lat={self.location_data.lat}&lon={self.location_data.lon}{"&mode=xml" if flag_xml else ""}&appid={self.api_key}"

        try:
            http_response = requests.get(http_request)
            http_response.raise_for_status()

            if flag_xml:
                xml_content = http_response.content
                root = ET.fromstring(xml_content)

                return root
            else:
                return http_response.json()
        except requests.HTTPError as err:
            http_err_response = http_response.json()["message"]

            match http_response.status_code:
                case 400:
                    raise exceptions.ApiBadRequestError(http_err_response, 400) from err

    def hourly_weather(self, flag_xml: bool = True):
        api_request = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={self.location_data.lat}&lon={self.location_data.lon}&appid={self.api_key}"

        try:
            api_response = requests.get(api_request)
            api_response.raise_for_status

            return api_response.json()
        
        except requests.HTTPError as err:
            print(err)
try:
    key = "0efb8b905c24e185100b24f4f29bcaf7"
    client = Client(api_key=key)
    client.geocode("95843", "US")

    print(client.current_weather())

except exceptions.ApiKeyError as e:
    print(f"ApiKeyError: {e}")
except exceptions.ApiBadRequestError as e:
    print(f"ApiBadRequestError: {e}")
except exceptions.ApiNotFoundError as e:
    print(f"ApiNotFoundError: {e}")