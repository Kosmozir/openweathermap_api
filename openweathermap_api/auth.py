import requests
from . import exceptions

def auth_api_key(api_key: str) -> None:
    try:
        auth_http_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={api_key}")
        auth_http_response.raise_for_status()

    except requests.HTTPError as e:
        exception_message = auth_http_response.json()["message"]

        if auth_http_response.status_code == 401:
            raise exceptions.ApiKeyError(exception_message, 401) from e