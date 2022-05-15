import KanyeAPI
import TrumpAPI
import random

def main():
	kapi = KanyeAPI.KanyeAPI()
	tapi = TrumpAPI.TrumpAPI()
	trumpquote = tapi.retrievequote()
	kanyequote = kapi.retrievequote()
	quotes = [trumpquote, kanyequote]
	randomchoice = random.choice(quotes)
	print(randomchoice)
	samelist = ["America", "money", "God", "president", "President", "office", "George Bush", "campaign", "greatest"]
	if randomchoice == trumpquote:
		correctuserguess = "t" 
	elif randomchoice == kanyequote:
		correctuserguess = "k" 
		
	userguess = input("Trump or Kanye? (t/k) ")
	if userguess == correctuserguess:
		if correctuserguess == "t":
			print("Correct....suprising right")
			for word in samelist:
				if word in randomchoice:
					print("Kanye would agree")
		elif correctuserguess == "k":
			print("Correct....suprising right")
			for word in samelist:
				if word in randomchoice:
					print("Trump would agree")
	else:
		print("WRONG")
	
main()

