class Dialogue:

    def __init__(self):
        self.actions = []
        self.question_pool = []
        self.depth = 0
        
    def give_actions(self, time):
        if time < 5:
            return "Buzzer Beater"
    
    