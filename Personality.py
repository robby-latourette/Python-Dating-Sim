import random
class Personality:
    def getTrait():
        if (random.random()>.49):
            return True
        else:
            return False
    traitList = {'sporty':getTrait()} 

    

if __name__ == "__main__":
    per = Personality
    print(per.traitList['sporty'])