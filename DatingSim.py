import random
import names
from rizzgod import Player
from Woman import Woman
from dialogue import Dialogue
class Simulation:
    def __init__(self):
        self.player = None
        self.woman = None
        self.diff = 'easy'
    
    def start(self):
        self.diff = input("Welcome to the Rizz Trainer. What difficulty are you prepared to play? easy or hard? (Easy mode is recommended for all CS majors) ")
        rizz = 0
        money = 0
        strength = 0
        if self.diff.lower() == 'easy':
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
    
    def generate_woman(self):
        self.woman = Woman()
        if self.diff == 'easy':
            self.woman.increaseLove(random.randint(0, 20))
    def woman_status(self):
        print("---------Current Date----------")
        print("Name:", self.woman.getName())
        print("Age:", self.woman.getAge())
        print("Interest", self.woman.getLove())
        print('-------------------------------')

if __name__ == "__main__":
    game = Simulation()
    dialogue = Dialogue()
    game.start()
    while True:
        game.generate_woman()
        game.woman_status
        dialogue.give_actions(game.player)
        if game.woman.getlove() >= 100:
            game.player.display_win()
            break
        game.player.stat_dict['dates'] += 1
        break
    