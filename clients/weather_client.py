import requests


class WeatherClient:

    default_url = "this is secret also man!!"

    def __init__(self, url, apiKey):
        self.url = url
        self.apiKey = apiKey

    def getCurrentConditions(self, lat: float, lon: float) -> str:
        print("About to print current condiition")
        print("original url:" + self.url)
        updatedUrl = self.url.replace("{lat}", str(lat))
        updatedUrl = updatedUrl.replace("{lon}", str(lon))
        updatedUrl = updatedUrl.replace("{API key}", self.apiKey)

        print(updatedUrl)
        weather_data = requests.get(updatedUrl).json()
        if weather_data:
            weather_obj = weather_data.get("data")
            weather_dt = weather_obj[0]
            print(weather_dt)
            weather_info = {
                "temp": weather_dt.get("temp"),
                "feels_like": weather_dt.get("feels_like")
            }
            return weather_info
        return None
