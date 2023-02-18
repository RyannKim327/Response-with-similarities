from utils.check_similar import Similarities
from utils.response import Reponses

a = Similarities("Hello World")
b = Reponses()

print(a.compare("Hi world"))
print(a.compare("Hello World"))
b.getPercent(a.getAllResponse())
print(b.getResponse())