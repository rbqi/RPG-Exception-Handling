# Description: Map Module

import sys
import numpy as np

# List of the territories on the map
territories = ["monu", "gozen"]

# Layout of Monu Territory (South Side 4x4 grid)
# MonuBorder is the starting base of the first quest
# MoNO is an area filled with hidden enemies
# MV is an empty area
# Mource is where you can find weapons, food and treatment
# Mountik is the mountain 800km away where the first amulet is hidden
# MonuLiberty is where the first quest is completed

monu_territory = np.array([
      ["MonuBorder", "MV", "MV", "MoNo"],
      ["MoNo", "Mource", "MV", "MoNo"],
      ["MV", "MoNo", "Mource", "Mountik"],
      ["MonuLiberty", "MV", "MoNo", "MV"]
 ])

# Layout of Gozen Territory (North Side 4x4 grid)
# GozenBorder is where the starting base & second quest begins
# Gwar is an area filled with scattered enemies
# GV is an empty area
# Goreload is where you can find weapons, food and treatment
# Gwind is the windmill 600km away and where the last amulet is hidden
# GozenLiberty is where the final quest is completed

gozen_territory = np.array([
      ["GozenBorder", "GV", "GV", "Gwar"],
      ["Gwar", "Goreload", "GV", "Gwar"],
      ["Gwind", "Gwar", "Goreload", "GV"],
      ["GV", "GV", "Gwar", "GozenLiberty"]
 ])


print("Welcome to the Mantik Village Map!")
print("\n")
# Ask user which territory they would like to go
print("Which territory would you like to go? ")
for t in territories:
    print(f"* {t}")
map_input = input("Choice: ")


def map_int():
    """ fiunction for map to import to main"""
    # If user choose Monu
    if map_input == "monu":
        print("\n")
        print("MONU TERRITORY: ")
        print(f" {monu_territory}")
        print("\n")
        print("You are currently located at the MonuBorder")
        print("\n")
        print("O oh! You just entered MoNo. Shoot enemies ahead!")

    # If user choose Gozen
    elif map_input == "gozen":
        print("\n")
        print("GOZEN TERRITORY: ")
        print(f" {gozen_territory}")
        print("\n")
        print("You are currently located at the GozenBorder")
        print("\n")
        print("Watch out! You're crossing Gwar. Shoot enemies ahead!")

    # If user chooses an invalid choice from the list
    else:
        print("Invalid Choice!")
        sys.exit()
