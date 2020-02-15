from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import numpy as np


class Investment(Page):
    form_model = 'player'
    form_fields = ['investment']
    def is_displayed(self):
        if self.player.participant.vars['failed'] == True:
            return False
        else:
            return True
    def before_next_page(self):
        self.player.calc_result()

    def vars_for_template(self):
        if self.round_number > 1:
            prev_players = self.player.in_previous_rounds()
            if self.round_number > 10:
                prev_players = prev_players[-10:]
            prev_players = reversed(prev_players)
            cumulative_payoff = sum([p.payoff for p in self.player.in_previous_rounds()])
            points_per_dollar = int(1/self.session.config['real_world_currency_per_point'])
            return {
            "prev_player":self.player.in_round(self.round_number - 1),
            "prev_players":prev_players,
            "tot_payoff":self.player.participant.payoff,
            "points_per_dollar": points_per_dollar,
            "reward_to_show": self.session.config["reward_to_show"],
            "num_rounds": self.session.config['num_rounds_to_show']
            # "new_patent": "Yes" if player.reach == Constants.reward else "No"
            # "num_first_exp":Constants.num_rounds - Constants.num_hire
            }
        else:
            points_per_dollar = int(1/self.session.config['real_world_currency_per_point'])
            return {"points_per_dollar": points_per_dollar,
            "tot_payoff":self.player.participant.payoff,
            "reward_to_show": self.session.config["reward_to_show"],
            "num_rounds": self.session.config['num_rounds_to_show']}

class RoundResults(Page):
    def is_displayed(self):
        if self.player.participant.vars['failed'] == True:
            return False
        else:
            return True


    def vars_for_template(self):
        return {
        "tot_payoff":self.player.participant.payoff,
        "investment": int(self.player.investment)
        }
#
# class Hiring(Page):
#     form_model = 'player'
#     form_fields = ['hire_decision']
#     def is_displayed(self):
#         return self.round_number > Constants.num_rounds - Constants.num_hire
#
#     def before_next_page(self):
#         self.player.hire_calc_result()
#
#     def vars_for_template(self):
#         self.player.hire_reach = round(np.random.randint(10,90)/self.player.β)
#         self.player.hire_cost = max(0,round(self.player.hire_reach*self.player.β + np.random.randn()*10))
#         cumulative_payoff = sum([p.payoff for p in self.player.in_previous_rounds()])
#         first_round = Constants.num_rounds - Constants.num_hire + 1
#         if self.round_number > first_round:
#             prev_players = self.player.in_previous_rounds()
#             if self.round_number > first_round + 10:
#                 prev_players = prev_players[-10:]
#             else:
#                 prev_players = prev_players[(first_round-1):]
#             prev_players = reversed(prev_players)
#
#             return {
#             "prev_player":self.player.in_round(self.round_number - 1),
#             "prev_players":prev_players,
#             "tot_payoff":cumulative_payoff,
#             "first_round": first_round
#             }
#         else:
#             return {"tot_payoff":cumulative_payoff,"first_round": first_round}


class OptQuestion(Page):
    form_model = 'player'
    form_fields = ['opt_question']
    def is_displayed(self):
        if self.player.participant.vars['failed'] == True:
            return False
        else:
            return self.round_number == Constants.num_rounds





class Results(Page):
    def is_displayed(self):
        if self.player.participant.vars['failed'] == True:
            return False
        else:
            return self.round_number == Constants.num_rounds


    def vars_for_template(self):
        cumulative_payoff = sum([p.payoff for p in self.player.in_all_rounds()])
        return {"money_payoff":round(float(cumulative_payoff)*self.session.config['real_world_currency_per_point'],2), "tot_payoff":cumulative_payoff}

page_sequence = [
    Investment,
    RoundResults,
    OptQuestion,
    Results
]
