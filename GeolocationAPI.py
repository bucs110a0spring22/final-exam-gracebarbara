import requests

class GeolocationAPI:
	def __init__(self):
		self.api_url = "https://ipgeolocation.abstractapi.com/v1/?api_key=27977de3b6d846b0856d51a1ccbe262b"


	def get(self):
		r = requests.get(self.api_url)
		response = r.json()
		latitude = response.get('latitude')
		longitude = response.get('longitude')
		print("Your Latitude: ", latitude)
		print("Your Longitude: ", longitude)
		



		
		
