import requests

class SunsetsunriseAPI:
	def __init__(self, latitude=0, longitude=0):
		self.api_url = f'https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}'

	def get(self):
		self.r = requests.get(self.api_url)
		self.response = self.r.json()