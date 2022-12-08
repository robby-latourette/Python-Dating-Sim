
class LoveMeter:
    def __init__(self) -> None:
        self.level = 0

    def getLevel(self):
        return self.level

    def increaseLevel(self, amt):
        self.level = self.level + amt
    
    

if __name__ == "__main__":
    temp = LoveMeter()
    print(temp.getLevel())
    temp.increaseLevel(4)
    print(temp.getLevel())