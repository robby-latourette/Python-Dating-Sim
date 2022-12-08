import random
class Personality:
    def getTrait():
        if (random.random()>.49):
            return True
        else:
            return False

    traitList = {'nerdy':getTrait(),'sporty':getTrait(),'musical':getTrait(),'happy':getTrait(),'adventurous':getTrait(),'urban':getTrait(),
        'techy':getTrait(),'animalLover':getTrait()} 

    

if __name__ == "__main__":
    per = Personality
    print(per.traitList)
    