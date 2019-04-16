from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import numpy as np
import json

def rand_game(size):
    return np.random.randint(10, size=(size,size,2))

class MyPage(Page):
    def is_displayed(self):
        if self.player.participant.vars['failed'] == True:
            return False
        else:
            return not self.player.participant.vars.get('done', False)
        # return not self.player.participant.vars.get('done', False)



class Instructions(MyPage):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5']

    def before_next_page(self):
        super().before_next_page()
        print(self.player.q1, self.player.q2, self.player.q3, self.player.q4, self.player.q5)
        if self.player.q2 == 30:
            print("apa")
        if (self.player.q1 == 150) and (self.player.q2 == 30) and (self.player.q3 == 100) and (self.player.q4 == "No") and (self.player.q5 == 2.5):
            print("Hej!")
            self.player.participant.vars['done'] = True
        else:
            self.player.participant.vars['done'] = False
            if self.player.round_number == 10:
                    self.player.participant.vars['failed'] = True

    def vars_for_template(self):
            points_per_dollar = int(1/self.session.config['real_world_currency_per_point'])
            return {"points_per_dollar": points_per_dollar,
                    "reward_to_show":self.session.config['reward_to_show']}

class FailPage(Page):
    def is_displayed(self):
        if self.player.participant.vars['failed'] == True:
            return True
        else:
            return False


page_sequence = [
    Instructions,
    FailPage
]
