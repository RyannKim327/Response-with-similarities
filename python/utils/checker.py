import re
import json
import random

class Similarities:
	def __init__(self, base: str = ""):
		'''Just call this first, before the response.'''
		self.respo = []
		self.base = base
	
	def compare(self, _input: str = "", isReturn: bool = True) -> dict:
		'''This is to compare the text and get all the possibilities'''
		first = re.split("\s", self.base)
		second = re.split("\s", _input)
		result = 0
		
		for i in range(len(first)):
			for j in range(i, len(second)):
				if first[i].lower() == second[j].lower():
					result += 1
					break
				else:
					for k in range(len(first[i])):
						for l in range(len(second[j])):
							if first[i][k].lower() == second[j][l].lower():
								result += ((len(first[i]) / len(second[j])) * 0.001)
		
		similar = round((result / len(first)) * 100)

		self.respo.append({
			"similar": similar,
			"base": self.base,
			"input": _input
		})

		if isReturn:
			return {
				"similar": similar,
				"base": self.base,
				"input": _input
			}
	
	def getAllResponse(self) -> list[dict]:
		'''Get all the responses'''
		return self.respo

class Reponses:
	def __init__(self, percentage: float = 25):
		'''This is to get all the data connected to the json file'''
		self.data = json.loads(open("../data/response.json", "r").read())
		self.bot = "<data>"
		self.percentage = percentage
	
	def getPercent(self, percents: list[dict], isResponse: bool = False) -> dict:
		'''Get the percentage and the posibility'''
		key = percents[0]['base']
		percent = int(percents[0]['similar'])
		for i in percents:
			if percent < int(i['similar']):
				percent = int(i['similar'])
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

	def getKeyName(self) -> str:
		'''Get the bot name'''
		return self.bot

	def setName(self, name: str):
		'''Set the bot name'''
		self.name = name

	def getName(self) -> str:
		'''Get your bot name'''
		return self.name

	def setYourName(self, name: str = ""):
		'''Get your name (username)'''
		self.yourname = name

	def getJson(self) -> dict:
		'''Get the current data exists in json'''
		return self.data

	def getResponse(self, base: str = "", auto: bool = True) -> dict:
		'''Get the highest response'''
		base = base.lower()
		if self.data.get(base) == "" or self.data.get(base) == None:
			base = self.response['base'].lower()
			if self.name.lower() in base:
				base = base.replace(self.name.lower(), self.bot)
			if self.data.get(base) == None:
				return {
					"ok": False,
					"msg": "I don't know what is this, sorry",
					"percentage": 0
				}
			else:
				if float(self.response.get("similar")) < self.percentage:
					return {
						"ok": False,
						"msg": "Low Possibility",
						"percentage": self.response.get("similar")
					}
				else:
					if auto:
						return {
							"ok": True,
							"msg": self.data.get(base)[random.randint(0, len(self.data.get(base)) - 1)].replace("<name>", self.yourname).replace("<myname>", self.name),
							"percentage": self.response.get("similar")
						}
					else:
						return {
							"ok": True,
							"msg": self.data.get(base),
							"percentage": self.response.get("similar")
						}
		else:
			if auto:
				return {
					"ok": True,
					"msg": self.data.get(base)[random.randint(0, len(self.data.get(base)) - 1)].replace("<name>", self.yourname).replace("<myname>", self.name),
					"percentage": self.response.get("similar")
				}
			else:
				return {
					"ok": True,
					"msg": self.data.get(base),
					"percentage": self.response.get("similar")
				}