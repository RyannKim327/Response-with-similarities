from utils.checker import Similarities, Reponses

response = Reponses(percentage=25)
keys = list(response.getJson().keys())
response.setName("Nix")
response.setYourName("RySes")

text = input(f"{response.getName()}: Welcome user, my name is {response.getName()}, your vitual chat bot, what do you want to ask for?\nYou: ")
while True:
	data = []
	for i in keys:
		similar = Similarities(i.lower().replace(response.getName().lower(), response.getKeyName()))
		similar.compare(text)
		response.getPercent(similar.getAllResponse())
		data.append(response.getResponse())
	
	for i in range(len(data)):
		for j in range(len(data)):
			if data[i]['percentage'] < data[j]['percentage']:
				data[i], data[j] = data[j], data[i]
	
	if data[len(data) - 1]['percentage'] == 0:
		print("I don't know what you're talking about")
	else:
		print(data[len(data) - 1]['msg'])

	text = input("You: ")