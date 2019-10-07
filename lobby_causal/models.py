from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Gustav Karreskog & Benjamin Mandl'

doc = """
Short quiz to test comprehension for Causal thinking experiment
"""


class Constants(BaseConstants):
    name_in_url = 'lobby'
    players_per_group = None
    num_rounds = 10

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars["failed"] = False
                p.participant.vars["treatment"] = (p.id_in_group % 3) + 1
                    # p.participant.vars["investment"], p.participant.vars["policy"] = np.random.permutate([1,2])
            for p in self.get_players():
                p.treatment = p.participant.vars["treatment"]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.IntegerField()
    q1 = models.IntegerField(choices=[0,50,150,200], widget=widgets.RadioSelect)
    q2 = models.IntegerField(choices=[0, 10, 15, 30, 60], widget=widgets.RadioSelect)
    q3 = models.IntegerField(choices=[10,30,50,100,], widget=widgets.RadioSelect)
    q4 = models.StringField(choices=["Yes", "No"], widget=widgets.RadioSelect)
    q5 = models.FloatField(choices=[0.25,1,2,2.5], widget=widgets.RadioSelect)
