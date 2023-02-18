import re
import json
import random

class Similarities:
	def __init__(self, base: str = ""):
		'''Just call this first, before the response.'''
		self.respo = []
		self.base = base
	
	def compare(self, _input: str = "", isReturn: bool = True) -> dict:
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
								result += (len(first[i]) / len(second[j]) * 0.1)
		
		similar = (result / len(first)) * 100

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
		return self.respo

class Reponses:
	def __init__(self):
		self.data = json.loads(open("data/response.json", "r").read())
		self.bot = "<data>"
	
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

	def getKeyName(self) -> str:
		return self.bot

	def setName(self, name: str):
		self.name = name

	def getName(self) -> str:
		return self.name

	def setYourName(self, name: str = ""):
		self.yourname = name

	def getJson(self) -> dict:
		return self.data

	def getResponse(self, base: str = "", auto: bool = True) -> dict:
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
				if float(self.response.get("similar")) < 75:
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