import requests

class SunsetsunriseAPI:
	def __init__(self, latitude, longitude):
		self.api_url = f'https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}'

	def get(self):
		r = requests.get(self.api_url)
		response = r.json()
		return response

	def sunsettime(self):
		response = self.get()
		results = response.get('results')
		sunset = results.get('sunset')
		print("Sunset Time: ", sunset)
		
	def sunrisetime(self):
		response = self.get()
		results = response.get('results')
		sunrise = results.get('sunrise')
		print("Sunrise Time: ", sunrise)
		
