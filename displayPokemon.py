# -*- coding: UTF-8 -*-
from tkinter import *
import tkinter.font as font
import pandas as pd
import os
root = Tk()

root.title("Pokedex")
myLabel = Label(root, text="Kalos")
myLabel.grid(row=1, column=9)

data = pd.read_csv("Kalos/Kalos.csv") 
locations = data.values.tolist()

def showData():
    print("Placeholder")

buttons = []
for location in locations:
    buttons.append(Button(root, text=location[0], command=showData))
    buttons[-1]["width"] = 10
    buttons[-1]["height"] = 2
    buttons[-1]["wraplength"] = 65
    myFont = font.Font(size=7)
    buttons[-1]['font'] = myFont


buttons[54].grid(row=14, column=10) #Vanville Town
buttons[53].grid(row=13, column=10) #Route 1
buttons[0].grid(row=12, column=10) #Aquacorde
buttons[1].grid(row=11, column=10) #Route 2
buttons[2].grid(row=10, column=10) #Santalune Forest
buttons[3].grid(row=9, column=10) #Route 3
buttons[4].grid(row=8, column=10) #Santalune City
buttons[5].grid(row=7, column=10) #Route 4
buttons[6].grid(row=6, column=9) #Lumiose

buttons[46].grid(row=7, column=8) #Route 5
buttons[45].grid(row=8, column=7) #Camphrier
buttons[43].grid(row=7, column=6) #Route 6
buttons[44].grid(row=6, column=6) #Parfum Palace
buttons[42].grid(row=8, column=6) #Route 7
buttons[47].grid(row=9, column=6) #Berry Fields
buttons[41].grid(row=8, column=5) #Connecting Cave
buttons[40].grid(row=8, column=4) #Cyllage City
buttons[48].grid(row=9, column=4) #Route 8
buttons[49].grid(row=10, column=4) #Amberette Town
buttons[50].grid(row=10, column=5) #Route 9
buttons[51].grid(row=10, column=6) #Glittering Cave

buttons[39].grid(row=7, column=3) #Route 10
buttons[37].grid(row=6, column=2) #Geosenge Town
buttons[38].grid(row=6, column=1) #Team Flare
buttons[36].grid(row=5, column=3) #Route 11
buttons[35].grid(row=4, column=4) #Reflection Cave
buttons[33].grid(row=4, column=5) #Shalour City
buttons[34].grid(row=3, column=5) #Tower of Mastery
buttons[31].grid(row=3, column=6) #Route 12
buttons[30].grid(row=3, column=7) #Coumarine City
buttons[32].grid(row=2, column=6) #Azure bay
buttons[29].grid(row=4, column=8) #Route 13
buttons[52].grid(row=5, column=8) #Kalos Power Plant

buttons[7].grid(row=5, column=9) #Route 14
buttons[8].grid(row=4, column=9) #Laverre City
buttons[9].grid(row=3, column=9) #Pokeball Factory

buttons[24].grid(row=10, column=11) #Route 22
buttons[25].grid(row=11, column=11) #Chamber of Emptiness
buttons[23].grid(row=10, column=12) #Victory Road
buttons[22].grid(row=10, column=13) #Route 21
buttons[26].grid(row=9, column=12) #Pokemon League
buttons[22].grid(row=10, column=13) #Route 21
buttons[21].grid(row=10, column=14) #Snowbelle City
buttons[27].grid(row=11, column=14) #Route 20
buttons[28].grid(row=12, column=14) #Pokemon Village

buttons[20].grid(row=9, column=15) #Route 19
buttons[19].grid(row=8, column=16) #Couriway Town
buttons[17].grid(row=7, column=15) #Route 18
buttons[18].grid(row=6, column=16) #Terminus Cave
buttons[16].grid(row=6, column=14) #Anistar City
buttons[15].grid(row=5, column=13) #Route 17

buttons[13].grid(row=4, column=12) #Dendemille Town
buttons[14].grid(row=3, column=13) #Frost Cavern
buttons[11].grid(row=4, column=11) #Lost Hotel
buttons[12].grid(row=4, column=10) #Route 16
buttons[10].grid(row=3, column=10) #Route 15



root.mainloop()