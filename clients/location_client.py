import requests

class LocationClient:
    url = "http://ip-api.com/json/"
    def __init__(self):
        self.url = "http://ip-api.com/json/"
        pass

    def getLocationInfo(self):
        print("Call made to get location via IP")
        response = requests.get(self.url).json()
        if response and response.get("status") == "success":
            location_data = {
                "city": response.get("city"),
                "latitude": response.get("lat"),
                "longitude": response.get("lon")
            }
            print(response.get("region"))
            return location_data
        else:
            return None
