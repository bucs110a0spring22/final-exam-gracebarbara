import GeolocationAPI
import SunsetsunriseAPI

def main():
	postal_code = input("What is your ZIP code? ")
	geoapi = GeolocationAPI.GeolocationAPI(postal_code)
	latitude = geoapi.latitude()
	longitude = geoapi.longitude()
	sunapi = SunsetsunriseAPI.SunsetsunriseAPI(latitude, longitude)
	sunapi.sunrisetime()
	sunapi.sunsettime()

main()