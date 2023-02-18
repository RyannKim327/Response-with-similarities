
class Reponses:
	def __init__(self):
		self.data = open("data/response.json", "r")
	
	def getPercent(self, percents: list[dict]):
		key = ""
		