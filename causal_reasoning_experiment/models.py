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
    num_rounds = 100
    reward = 150
    # num_hire = 20
    dollars_per_point = 0.001


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
        label="How much do you want to invest in research and development?"
    )
    reach = models.FloatField(initial=0)
    skill = models.FloatField(initial=0)
    wage = models.IntegerField(initial=0)
    treatment = models.IntegerField()
    β = models.FloatField(initial=0.5)
    patent = models.StringField()
    success = models.StringField()

    # hire_cost = models.IntegerField()
    # hire_reach = models.IntegerField()
    # hire_decision = models.BooleanField(label="Do you want to buy this add?", choices=[[True, "Yes"], [False, "No"]], widget=widgets.RadioSelect)

    # skill_σ = models.IntegerField(initial=13)
    # reach_σ = models.IntegerField(initial=0.1)
    # wage_σ = models.IntegerField(initial=0.1)
    # investment_order = models.IntegerField()
    # policy_order = models.IntegerField()

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
    # def hire_calc_result(self):
    #     if self.hire_decision:
    #         self.skill = round(np.random.randn()*self.skill_σ,2)
    #         self.reach = round(np.random.rand()*self.reach_σ + self.hire_reach + self.skill)
    #         self.wage = round(np.random.randn()*self.wage_σ + self.β*self.reach + self.skill)
    #         self.payoff = self.wage -  self.hire_cost
    #     else:
    #         self.payoff = 0

    def calc_result(self):
        a = np.sqrt(float(self.investment))/10
        # self.skill = round(np.random.randn()*self.skill_σ, 2)
        # self.reach = round(np.random.randn()*self.reach_σ + a + self.skill/self.β)
        # self.wage = round(np.random.randn()*self.wage_σ + self.β*self.reach + self.skill)
        # self.payoff = self.wage -  self.investment
        p_θ1 = 0.5
        θ_0 = 0.2
        θ_1 = 1.
        β_0 = 0.1
        β_1 = 1.
        self.skill = θ_1 if np.random.rand() < p_θ1 else θ_0
        self.reach = β_1 if np.random.rand() < self.skill*a else β_0
        self.wage = Constants.reward if np.random.rand() < self.skill*self.reach else 0
        self.payoff = self.wage -  self.investment
        self.patent = "Yes" if self.reach == β_1 else "No"
        self.success = "Yes" if self.wage == Constants.reward else "No"
