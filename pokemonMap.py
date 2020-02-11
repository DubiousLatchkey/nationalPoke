#Towns/Major locations
class Node:
    locations = []
    attachedEdges = []

#Routes/Minor locations
class Edge:
    locations = [] #Max of 2 locations
    orientation = ""
    attachedNodes = []

class Location:
    name = ""
    listOfPokemon = []

class PokemonAtLocation:
    name = ""
    catchMethod = ""

class Region:
    nodes = []
    edges = []

    def floodFillVisualize():
        