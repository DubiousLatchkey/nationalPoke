# -*- coding: UTF-8 -*-
import csv
import pandas as pd

mainlineGames = ["Pokémon Sword", "Pokémon Shield", "Pokémon Ultra Sun", "Pokémon Ultra Moon",
 "Pokémon Sun", "Pokémon Moon", "Pokémon X", "Pokémon Y", "Pokémon Omega Ruby", "Pokémon Alpha Sapphire",
 "Pokémon Black 2", "Pokémon White 2", "Pokémon Black", "Pokémon White", "Pokémon HeartGold",
 "Pokémon SoulSilver", "Pokémon Diamond", "Pokémon Pearl", "Pokémon Platinum"]

forbiddenMethods = ["Trade", "Event", "Poké Transfer", "Pokémon HOME", "Unobtainable", "Pokémon Home",
"event", "Trade, Event", "", "Pokémon Bank"]

data = pd.read_csv("PokemonCatchMethods.csv") 
pokemonCatchMethodsPreProcessed = data.values.tolist()

#Remove non-mainline games, trade
pokemonCatchMethods = []
for method in pokemonCatchMethodsPreProcessed:
    gameFlag = False
    for game in mainlineGames:
        if(game in method[1]):
            gameFlag = True

    methodFlag = True
    for badMethod in forbiddenMethods:
        if(badMethod == method[0]):
            methodFlag = False
            
    if(gameFlag and methodFlag):
        pokemonCatchMethods.append(method)
        #print(method[2] + "(" +method[1] + "): " +method[0])

pokemonNames = []
pokemonGames = []
catchMethods = []
for method in pokemonCatchMethods:
    pokemonNames.append(method[2])
    pokemonGames.append(method[1])
    catchMethods.append(method[0])

df = pd.DataFrame({"Catch Method": catchMethods, "Pokemon Game":pokemonGames, "Pokemon Name":pokemonNames })
df = df[['Pokemon Name','Pokemon Game','Catch Method']]
df.to_csv("NationalPokedexCatchMethods.csv", index = False, encoding = "utf-8")