from Personality import Personality
import names
import random
from Character import Character

class Woman(Character):
    name = names.get_female_name()
    age = random.randint(17, 45)
    per = Personality
    
    def __init__(self):
        pass
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getPersonality(self):
        return self.per



if __name__ == "__main__":
    roberta = Woman  
    print(roberta.per.traitList)
    print(roberta.name)
    print(roberta.age)
