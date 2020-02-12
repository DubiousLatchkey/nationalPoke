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
    name = ""
    catchMethod = ""
    def __init__(self, name, method):
        self.name = name
        self.catchMethod = method

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

#Build map
def getLocations(url, region):
    #Fetch link
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    location = Location(soup.h1.get_text(), None)
    location.url = url
    print(location.name)
    #Add Pokemon


    #Find connected locations
    for i in soup.findAll("td"):
        #Regular location case
        if("Connecting locations" in i.get_text()):
            for j in i.findAll("a"):
                if("Connecting locations" not in j.get_text()):
                    location.addLocation(j.get_text(), "https://bulbapedia.bulbagarden.net" + j.get("href"))
                    #print(j.get_text())
            break

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
            print("Going to: " +i)
            regions[region].append(getLocations(i, region)) 

#Get all links
url = "https://bulbapedia.bulbagarden.net/wiki/Aquacorde_Town"
getLocations(url, 0)
for i in regions[0]:
    if(i != None):
        print(i.name)
#Save to file


#root.mainloop()
