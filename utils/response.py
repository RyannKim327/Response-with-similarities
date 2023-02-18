import json
import random
class Reponses:
	def __init__(self):
		self.data = json.loads(open("data/response.json", "r").read())
	
	def getPercent(self, percents: list[dict], isResponse: bool = False) -> dict:
		key = percents[0]['base']
		percent = int(percents[0]['similar'])
		for i in percents:
			if percent < i['similar']:
				percent = i['similar']
				key = i['base']
		self.response = {
			"base": key,
			"similar": percent
		}
		if isResponse:
			return {
				"base": key,
				"similar": percent
			}

	
	def getResponse(self, base: str = "", auto: bool = True) -> str:
		if self.data.get(base) == "" or self.data.get(base) == None:
			print(self.response['base'].lower())
			if self.data.get(self.response['base'].lower()) == None:
				return "I don't know what is this, sorry"
			else:
				if auto:
					return self.data.get(self.response['base'].lower())[random.randint(0, len(self.data.get(self.response['base'].lower())) - 1)]
				else:
					return self.data.get(self.response['base'].lower())
		else:
			return self.data.get(base)