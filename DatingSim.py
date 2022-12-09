import random
import names
from rizzgod import Player

class Simulation:
    def __init__(self):
        pass
    def provide_woman():
        pass
    def display_win():
        pass
    def start():
        age = random.randint(18, 120)
        if input("Would like to input your own name or use a randomly generated name? own/random").lower() == "own":
            name = input("Input name here:")
        else:
            name = names.get_name()
        user = Player(age, name)
        print(f"You will be playing as {name}. You are {age} years old. Good luck out there.")

