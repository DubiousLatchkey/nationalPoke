# -*- coding: UTF-8 -*-
from tkinter import *
import pandas as pd
root = Tk()

#Towns/Major locations
class Node:
    locations = []
    attachedEdges = []
    nodeButton = None
    name = ""
    row = 0
    column = 0
    def __init__(self, locations, attachedEdges, name, row, column):
        self.locations = locations
        self.attachedEdges = attachedEdges
        self.name = name
        self.row = row
        self.column = column
        nodeButton = Button(root, Text=name, row=row, column=column, COMMAND=showData)
        nodeButton.grid()

    def showData():
        #open new window
        print("Placeholder")


#Routes/Minor locations
class Edge:
    locations = [] 
    orientation = ""
    attachedNodes = [] #Max of 2 locations
    name = ""

class Location:
    name = ""
    listOfPokemon = []
    def __init__(self, name, pokemon):
        self.name = name
        self.listOfPokemon = pokemon

class PokemonAtLocation:
    name = ""
    catchMethod = ""

class Region:
    nodes = []
    edges = []

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
    pokemonNames.append(method[2])
    pokemonGames.append(method[1])
    catchMethods.append(method[0])




root.mainloop()
