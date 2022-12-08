import random
from dialogue import Dialogue
class Player:
    def __init__(self):
        self.stat_dict = {"rizz": 0, "money": 0, "dates": 0, "age": 20, "strength": 0}

        self.action_controller = Dialogue

    def perform_action(self, action):
        r_num = random.random(0, 1)
        success_rate = self.stat_dict[action[1]] + action[2]
        if success_rate > r_num:
            print(f"{action[1].upper()} INCREASED BY 1 POINT!")
        else:
            print("You were unsuccessful :(")
    
            


    

if __name__ == "__main__":
    pass