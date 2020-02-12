# -*- coding: UTF-8 -*-
from tkinter import *
import pandas as pd
from bs4 import BeautifulSoup
import requests
import urllib3.request
root = Tk()

class Location:
    #name = ""
    #url = ""
    #connectedLocations = []
    #locationLinks = []
    #listOfPokemon = []
    def __init__(self, name, pokemon):
        self.name = name
        self.url = ""
        self.connectedLocations = []
        self.locationLinks = []
        self.listOfPokemon = pokemon

    def addLocation(self, location, link):
        self.connectedLocations.append(location)
        self.locationLinks.append(link)

class PokemonAtLocation:

    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

class Region:
    locations = []

    def floodFillVisualize():
        print("This is fine")


#initialize
root.title("Pokedex")
myLabel = Label(root, text="Kalos")
myLabel.grid()

#Read in pokes
data = pd.read_csv("NationalPokedexCatchMethods.csv")
pokemonCatchMethods = data.values.tolist()
pokemonNames = []
pokemonGames = []
catchMethods = []
for method in pokemonCatchMethods:
    pokemonNames.append(method[0])
    pokemonGames.append(method[1])
    catchMethods.append(method[2])

regions = [[] for i in range(5)]

def text_with_processing(elem):
    text = ''
    for e in elem.descendants:
        if isinstance(e, str):
            text += e
			
        elif e.name == 'br' or e.name == 'p':
            text += '\n'

        elif e.name == 'sup':
            text+= '^'

    return text

def processRates(rate):
    if(rate == "One"):
        return 0.00001
    elif(rate == "Common"):
        return 0.5
    elif(rate == "Rare"):
        return 0.1
    elif(rate == "Very Rare" or rate == "Fossil"):
        return 0.05
    else:
        return float(rate.strip("~%")) / 100
        
def compareRates(oldRate, newRate):
    if(float(oldRate) > processRates(newRate)):
        return oldRate
    else:
        return processRates(newRate)

#Build map
def getLocations(url, region, generation):
    #Fetch link
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    location = Location(soup.h1.get_text(), [])
    location.url = url
    print(location.name)

    #Add Pokemon
    for tableTitle in soup.findAll("h2"):
        if(tableTitle.get_text() == "Pokémon"):
            for tableRow in tableTitle.find_next_sibling("table").find_all("tr")[2:]:
                #print(tableRow.get_text())
                name = ""
                rate = ""
                text = [i.strip() for i in text_with_processing(tableRow).split("\n") if i]
                if(len(text) > 4): 
                    name = text[1]
                    rate = text[-1]
                    if("with" in rate): #Horde encounter with another pokemon case
                        rate = text[-2]
                    #print(name, rate)
                    alreadyHave = False
                    for pokemon in location.listOfPokemon:
                        if(pokemon.name == name):
                            alreadyHave = True
                            pokemon.rate = compareRates(oldRate=pokemon.rate, newRate=rate)
                            break
                    if(not alreadyHave):
                        location.listOfPokemon.append(PokemonAtLocation(name, processRates(rate)))
    
    for i in location.listOfPokemon:
        print (i.name, i.rate)                   
                    

    #Find connected locations
    foundConnections = False
    for i in soup.find_all("td"):
        #Regular location case (routes, towns)
        if("Connecting locations" in i.get_text()):
            foundConnections = True
            for j in i.findAll("a"):
                if("Connecting locations" not in j.get_text()):
                    location.addLocation(j.get_text(), "https://bulbapedia.bulbagarden.net" + j.get("href"))
                    #print(j.get_text())
    #Special location case
    if(not foundConnections):
        for i in soup.find_all("th"):
            if("Location:" in i.get_text()):
                for j in i.find_next_sibling("td").find_all("a"):
                    #print(j.get_text())
                    location.addLocation(j.get_text(), "https://bulbapedia.bulbagarden.net" + j.get("href"))

    print(location.locationLinks)

    #Call in recursion
    global regions
    regions[region].append(location)

    for i in location.locationLinks:
        #Check to see if location has been visited
        beenThere = False
        for j in regions[region]:
            if(j != None and i == j.url):
                print("Already been to: " +j.url)
                beenThere = True
                break
        #Go to novel location
        if(not beenThere):
            print("Going to: " +i + "\n")
            regions[region].append(getLocations(i, region, generation)) 

#Get all links
url = "https://bulbapedia.bulbagarden.net/wiki/Aquacorde_Town"
getLocations(url, 0, 6)
for i in regions[0]:
    if(i != None):
        print(i.name)
#Save to file maybe?


#root.mainloop()
