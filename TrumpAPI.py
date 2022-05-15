import requests

class TrumpAPI:
	def __init__(self):
		'''stores url in instance variable
		args: none
		return: none
		'''
		self.api_url = "https://api.whatdoestrumpthink.com/api/v1/quotes/random"
		
	def get(self):
		'''uses API url to retrieve data
		args: none
		return: response(str)'''
		r = requests.get(self.api_url)
		response = r.json()
		return response

	def retrievequote(self):
		'''uses get method to retrieve only the quote from the API dictionary
		args: none
		returns: trump quote (str)'''
		quote = self.get()
		trump = quote.get('message')
		return trump




		
		
