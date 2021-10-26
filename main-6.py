# Coarse: CS 30
# Period:3
# Date created: 20/09/21
# Date las modified: 18/10/21
# Name: Rabi Jasteen Juancito
# Description: RPG exception handling

# Ask user to inuput a username for their character
name = (input("What is your character username: "))
print("\n")

print(f"Hi {name}!")
print("\n")

while True:
    import sys
    import rpgmapa as m
    print(m.map_int())
    break


def weapon_int(message):
    """Check if user input is a positive number"""
    # While loop allows the program to contiue until
    # user puts a positive number
    while True:
        # User try to input a number
        try:
            userchoice = int(input(message))
            if userchoice > 0:
                return userchoice
            # If number is not positive user must input new number
            else:
                print("Use a positive number. Please try again.")
                continue
            # If input is not a number
        except ValueError:
            print("Invalid! Use a number. Please try again.")
            continue
            # Every time user inputs something
        finally:
            print(f"Hurry {name}! Shoot it!!")


# Using the function weapon_int to ask user to input
w = weapon_int("How many Arrows would you like to shoot to attack? ")
print("\n")
# Print(f" You just fired {userchoice} arrows!")
print(f"{w} Arrows has been fired.")
print(f"Impressive! Nice shot {name}!")
sys.exit()
