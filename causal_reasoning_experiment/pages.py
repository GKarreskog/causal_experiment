from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Investment(Page):
    form_model = 'player'
    form_fields = ['investment']
    def before_next_page(self):
        self.player.calc_result()
    
    def vars_for_template(self):
        if self.round_number > 1:
            prev_players = self.player.in_previous_rounds()
            if self.round_number > 10: 
                prev_players = prev_players[-10:]
            prev_players = reversed(prev_players)
            cumulative_payoff = sum([p.payoff for p in self.player.in_previous_rounds()])
            return {
            "prev_player":self.player.in_round(self.round_number - 1), 
            "prev_players":prev_players,
            "tot_payoff":cumulative_payoff
            }




class Results(Page):
    def is_displayed(self):
        self.player.calc_result()
        return self.round_number == Constants.num_rounds

page_sequence = [
    Investment, Results
]
