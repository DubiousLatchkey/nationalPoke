from selenium import webdriver
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
pokemonNames = []
pokemonNumbers = []

for i in soup.findAll("a"):
	#print(i.get("title"))
	#print(i.parent)
	if(i.get("title") != None and "mon)" in i.get("title") and i.parent.name == "td"):
		pokemonLinks.append("https://bulbapedia.bulbagarden.net" + i.get("href"))
		pokemonNames.append(i.get("title")[:-10])
		pokemonNumbers.append(i.parent.find_previous_sibling("td").get_text())
		#print(pokemonLinks[-1])

df = pd.DataFrame({"Pokemon Number":pokemonNumbers, "Pokemon Name":pokemonNames, "Pokemon Links":pokemonLinks})
df.to_csv("pokemon.csv", index = False, encoding = "utf-8")
