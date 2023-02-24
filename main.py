from utils.checker import Similarities, Reponses

response = Reponses()
keys = list(response.getJson().keys())
response.setName("Nix")
response.setYourName("RySes")

text = input(f"{response.getName()}: Welcome user, my name is {response.getName()}, your vitual chat bot, what do you want to ask for?\nYou: ")
while True:
	for i in keys:
		similar = Similarities(i.lower().replace(response.getName().lower(), response.getKeyName()))
		similar.compare(text)
		response.getPercent(similar.getAllResponse())
		if response.getResponse()['ok']:
			print(response.getResponse()['msg'])
			break
	else:
		print("I can't see any near match.")

	text = input("You: ")