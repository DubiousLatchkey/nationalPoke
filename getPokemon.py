from bs4 import BeautifulSoup
import pandas as pd
import requests
import urllib3.request
import time

url = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
response = requests.get(url)

#print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
#print(soup.findAll("a"))

pokemonLinks = []
pokemonNamesPre = []
pokemonNames = []
pokemonNumbers = []

for i in soup.findAll("a"):
	#print(i.get("title"))
	#print(i.parent)
	if(i.get("title") != None and "mon)" in i.get("title") and i.parent.name == "td"):
		pokemonLinks.append("https://bulbapedia.bulbagarden.net" + i.get("href"))
		#pokemonNamesPre.append(i.get("title")[:-10])
		pokemonNamesPre.append(i.get_text())
		pokemonNumbers.append(i.parent.find_previous_sibling("td").get_text())
		#print(pokemonLinks[-1])

deleted = 0
for i in range(len(pokemonNamesPre)):
	if(pokemonNamesPre[i] not in pokemonNames):
		pokemonNames.append(pokemonNamesPre[i])
	else:
		del pokemonLinks[i - deleted]
		del pokemonNumbers[i -deleted]
		deleted += 1
		
def text_with_processing(elem):
    text = ''
    for e in elem.descendants:
        if isinstance(e, str):
            text += e
			
        elif e.name == 'br' or e.name == 'p':
            text += ', '

        elif e.name == 'sup':
            text+= '^'

    return text


df = pd.DataFrame({"Pokemon Number":pokemonNumbers, "Pokemon Name":pokemonNames, "Pokemon Links":pokemonLinks})
df.to_csv("pokemon.csv", index = False, encoding = "utf-8")

pokemonCatchMethods = []
pokemonCatchGames = []
df = None
df = pd.DataFrame({"Pokemon":[], "Game to Catch in":[], "Catch Methods":[]})

pokeNum = 0
for i in pokemonLinks:
	
	response = requests.get(i)
	soup = BeautifulSoup(response.text, "html.parser")
	for j in soup.findAll("table"):
		#print(type(j.find_previous_sibling("h3")), " ", type(None))
		if(type(j.find_previous_sibling("h3")) != type(None) and j.find_previous_sibling("h3").get_text() == "Game locations"):
			for k in j.findAll("td"):
				#print(str(k.get("class")))
				if(str(k.get("class")) == "['roundy']"):
					#print(k.parent.parent.parent.parent.find("a").get("title"))
					#print(k.get_text())
					#print(text_with_processing(k))
					pokemonCatchGames.append(k.parent.parent.parent.parent.find("a").get("title"))
					#pokemonCatchMethods.append(k.get_text())
					pokemonCatchMethods.append(text_with_processing(k))
	
					
	dfTemp = pd.DataFrame({"Game to Catch in":pokemonCatchGames, "Catch Methods":pokemonCatchMethods})		
	dfTemp["Pokemon"] = pokemonNames[pokeNum]
	df = pd.concat([dfTemp, df])
	print("That's " + pokemonNames[pokeNum] )
	pokeNum += 1
	pokemonCatchMethods = []
	pokemonCatchGames = []

df.to_csv("PokemonCatchMethods.csv", index = False, encoding = "utf-8")
