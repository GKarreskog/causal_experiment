from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import numpy as np
import scipy.stats as stats

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'causal_reasoning_experiment'
    players_per_group = None
    num_rounds = 50


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars["treatment"] = (p.id_in_group % 3) + 1
                # p.participant.vars["investment"], p.participant.vars["policy"] = np.random.permutate([1,2])
        for p in self.get_players():
            p.treatment = p.participant.vars["treatment"]
            # p.policy_order = p.participant.vars["policy"]
            # p.investment_order = p.participant.vars["investment"]



class Group(BaseGroup):
    pass


# def my_trunc_norm(µ, min=0, max=1, σ=0.2):
#     a,b = (min - μ)/σ, (max - μ)/σ
#     return stats.truncnorm.rvs(a,b,loc=μ, scale=σ)

class Player(BasePlayer):
    investment = models.CurrencyField(
        min=0, max=100,
        label="Much do you want to invest?"
    )
    capital = models.FloatField()
    skill = models.FloatField()
    wage = models.IntegerField()
    treatment = models.IntegerField()
    investment_order = models.IntegerField()
    policy_order = models.IntegerField()

    # policy_a = model.IntegerField()
    # policy_y = model.IntegerField()
    # policy_e = model.FloatField()
    # policy_z = model.FloatField()
    # policy_u = model.FloatField()
    # policy_β = model.FloatField()
    # policy_κ = model.FloatField()
    # policy_δ = model.FloatField()

    # def policy_calc_result(self):
    #     self.policy_β = 0.6
    #     self.policy_y = 1 if np.random.rand() < self.policy_a*self.policy_β else 0

    def calc_result(self):
        a = np.sqrt(float(self.investment)/100)*100
        self.skill = round(max(0.1, np.random.randn()*0.1 + 1), 2)
        self.capital = round(max(0, np.random.randn()*10 + a*self.skill))
        self.wage = round(max(0, np.random.randn()*1 + self.skill*self.capital))
        self.payoff = self.wage -  self.investment 
        # p_θ1 = 0.5
        # θ_0 = 0.5
        # θ_1 = 1.
        # β_0 = 0.3
        # β_1 = 0.8
        # self.skill = θ_1 if np.random.rand() < p_θ1 else θ_0
        # self.capital = β_1 if np.random.rand() < self.skill*a else β_0
        # self.wage = 120 if np.random.rand() < self.skill*self.capital else 20
        # self.payoff = self.wage -  self.investment 


