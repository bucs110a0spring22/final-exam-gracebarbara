import requests

class GeolocationAPI:
	def __init__(self, postal_code):
		self.api_url = f"https://ipgeolocation.abstractapi.com/v1/?api_key=27977de3b6d846b0856d51a1ccbe262b&postal_code={postal_code}"

	def get(self):
		r = requests.get(self.api_url)
		response = r.json()
		return response

	def latitude(self):
		response = self.get()
		latitude = response.get('latitude')
		print("Your Latitude: ", latitude)
		return latitude

	def longitude(self):
		response = self.get()
		longitude = response.get('longitude')
		print("Your Longitude: ", longitude)
		return longitude
		



		
		
