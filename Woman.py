from Personality import Personality
import names
import random
from Character import Character
from LoveMeter import LoveMeter

class Woman(Character):
    def __init__(self) -> None:
        self.name = names.get_female_name()
        self.age = random.randint(17, 45) 
        self.love = LoveMeter()
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getlove(self):
        return self.love.getLevel()
    def increaseLove(self, amt):
        self.love.increaseLevel(amt) 



if __name__ == "__main__":
    roberta = Woman()
    roberta.increaseLove(5)
    print(roberta.getlove())
    print(roberta.name)
    print(roberta.age)
