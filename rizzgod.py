import random
from dialogue import Dialogue

class Player:
    def __init__(self, age, name='Mario', rizz=0, money=0, strength=0):
        self.stat_dict = {'name':name, "rizz": rizz, "money": money, "dates": 0, "age": 20, "strength": strength}

        self.action_controller = Dialogue

    def perform_action(self, category, action):
        r_num = random.random(0, 1)
        success_rate = self.stat_dict[category] + action[1]
        if success_rate > r_num:
            print('YOU SUCCEEDED!')
            print(f"{action[1].upper()} INCREASED BY 1 POINT!")
            self.stat_dict[action[1]] += 1
        else:
            print("You were unsuccessful :(")

    def status_report(self):
        print("-------------------------------")
        print("-------------Status------------")
        print("Name:", self.stat_dict['name'])
        print("Age:", self.stat_dict['age'])
        print("Rizz:", self.stat_dict['rizz'])
        print("Strength:", self.stat_dict['strength'])
        print("Total Dates:", self.stat_dict['dates'])
        print('-------------------------------')

    def display_win(self):
        print("-------------------------------")
        print("-----------Win Report----------")
        print("Name:", self.stat_dict['name'])
        print("Age:", self.stat_dict['age'])
        print("Rizz:", self.stat_dict['rizz'])
        print("Strength:", self.stat_dict['strength'])
        print("Total Dates:", self.stat_dict['dates'])
        print('-------------------------------')
            


    

if __name__ == "__main__":
    pass