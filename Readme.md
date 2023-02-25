### Response with similarities
#### MPOP Reverse II
---
### Basic information about the project
```JSON
{
	"name": "Nix",
	"description": "A simple program like simsimi",
	"author": "RyannKim327",
	"screenNames": [
		"RyannKim327",
		"MPOP",
		"MPOP Reverse II",
		"RySes"
	],
	"dateStarted": "02-18-2023 17:37"
}
```
---
### Information
> This is just a simple program developed as basics for auto responses chatting bot. Also a way of trying to learn some basics of Data Analyticss and Machine Learning.
---
### Notices
> This program is still in development, I try to make it more accurate, so that I can share the idea of the program very well, also the accuracy of the program. For more details, you may message me on facebook attached on my github account.

---
### Tutorial
> Mostly the program uses the keywords from the python dictionary, which calls the data from the json file.

### Use Response
> Response is a class that has optional requirement parameter, which is the posibility. So the default value of the posibility is just 25 for some lower percentage of data

```Python
response = Response()
# or
# response = Response(50)
# Where 50 is the 50 percent
```

> It has function names, which can be used to this project

#### .setName [Response]
> It only composed of 1 parameter, which is string
```Python
response = Response()
response.setName("Bot Name")
```
> This is to identify the name used. It is same as the `.setYourName` for the user's name.

#### .getPercent
> This function is to get all the percentage or the highest percentage it has. In this current program there are boolean parameter, if you want ot print or have return in the current data. The required parameter for this function is to have a list of dictionary.

#### .getResponse()
> This function returns a dictionary format
```Python
{
	"ok": False, # bool
	"msg": "I don't know what is this, sorry", # String
	"percentage": 0 # float
}
```

### Similarities
> This class is use to compare things, this is to get all the possible data that may have in a specific phrase. The constructor has the required parameter which is the base or the data pr phrase.

#### .compare
> This is to compare the base phrase into the input, the main function for this, is to get the percentage of having similarities of the phrase given.

### .getAllResponse
> This function is just to get all the data given with its percentage in a dictionary format

---
### Disclaimer
> The main idea of the program is not just big as this one, the main idea here is just to get the possibilities of having the similarities of the phrase to each other.

---
**Developed by *(RyannKim327)***