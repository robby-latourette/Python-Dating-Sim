import random
import names
from rizzgod import Player

class Simulation:
    def __init__(self):
        self.player = None
        self.curr_char = None

    def provide_woman(self):
        pass
    
    def start(self):
        diff = input("Welcome to the Rizz Trainer. What difficulty are you prepared to play? easy or hard? (Easy mode is recommended for all CS majors) ")
        rizz = 0
        money = 0
        strength = 0
        if diff.lower() == 'easy':
            rizz = random.randint(0, 20)
            money = random.randint(0, 20)
            strength = random.randint(0, 20)

        age = random.randint(18, 120)

        if input("Would like to input your own name or use a randomly generated name? own/random: ").lower() == "own":
            name = input("Input name here: ")
        else:
            name = names.get_male_name()
        self.player = Player(age, name, rizz, money, strength)
        print(f"You will be playing as {name}. You are {age} years old. Good luck out there.")
        self.player.status_report()
        print("You will receive a status report like this one after each round of speed-dating.")

if __name__ == "__main__":
    game = Simulation()
    game.start()
    while True:
        
        game.player.stat_dict['dates'] += 1
        break
    