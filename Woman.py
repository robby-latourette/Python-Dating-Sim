from Personality import Personality
import names
import random
from Character import Character
from LoveMeter import LoveMeter

class Woman(Character):
    def __init__(self) -> None:
        self.name = names.get_female_name()
        self.age = random.randint(17, 45) 
        self.love = LoveMeter
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getlove(self):
        return self.love
    def increaseLove(self, amt):
        self.love += amt



if __name__ == "__main__":
    roberta = Woman  
    print(roberta.per.traitList)
    print(roberta.name)
    print(roberta.age)
