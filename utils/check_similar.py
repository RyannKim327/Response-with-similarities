import re
class Similarities:
	def __init__(self, base: str = "", _input: str = ""):
		self.base = base
		self.input = _input
	
	def compare(self):
		first = re.split("\s", self.base)
		second = re.split("\s", self.input)
		result = 0
		
		for i in range(len(first)):
			for j in range(i, len(second)):
				if first[i].lower == second[j].lower:
					result += 1
					break
				else:
					for k in range(len(first[i])):
						for l in range(len(second[j])):
							if first[i][k].lower == second[j][l].lower:
								result += 0.1

		return {
			"similar": (round(result) / len(self.base)) * 100,
			"base": self.base,
			"input": self.input
		}