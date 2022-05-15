import requests
import GeolocationAPI
import SunsetsunriseAPI

def main():
	geoapi = GeolocationAPI.GeolocationAPI()
	latitude = geoapi.latitude()
	longitude = geoapi.longitude()
	sunapi = SunsetsunriseAPI.SunsetsunriseAPI(latitude, longitude)
	sunapi.get()
	sunapi.sunrisetime()
	sunapi.sunsettime()

main()