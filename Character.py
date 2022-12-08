import Personality
import names
import random
from abc import ABC, abstractmethod

class Character:
    @abstractmethod
    def getName(self):
        pass
    @abstractmethod
    def getAge(self):
        pass



if __name__ == "__main__":
    robby = Character   
    print(robby.per.Personality.traitList)
    print(robby.name)
    print(robby.age)
