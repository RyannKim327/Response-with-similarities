import re
class Similarities:
	def __init__(self, base: str = ""):
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
		
		self.respo.append({
			"similar": ((result / len(first)) * 100),
			"base": self.base,
			"input": _input
		})
		if isReturn:
			return {
				"similar": ((result / len(first)) * 100),
				"base": self.base,
				"input": _input
			}
	
	def getAllResponse(self) -> list[dict]:
		return self.respo