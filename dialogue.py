import action_pool
import random
class Dialogue:

    def __init__(self):
        self.actions = ['rizz', 'money', 'strength', 'other']
        self.question_pool = action_pool.actions

    def give_actions(self, player):
        choices = ['rizz', 'money', 'strength', 'other']
        self.actions[0] = random.choice(self.question_pool['rizz'])
        self.actions[1] = random.choice(self.question_pool['money'])
        self.actions[2] = random.choice(self.question_pool['strength'])
        self.actions[3] = random.choice(self.question_pool['other'])
        print('1)', self.actions[0][0], self.actions[0][1], '% chance')
        print('2)', self.actions[1][0], self.actions[1][1], '% chance')
        print('3)', self.actions[2][0], self.actions[2][1], '% chance')
        print('4)', '??????')
        choice = input('Choose 1, 2, 3, or 4')
        print(self.actions[int(choice)][0], self.actions[0][1], '% chance')
        player.perform_action(choices[int(choice)])


    dislike = {"Yeah...I'm like not a fan."}