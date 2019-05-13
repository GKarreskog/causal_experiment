from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']
mturk_hit_settings = {
    'keywords': ['bonus', 'study'],
    'title': 'Experiment on decison making and learning from experience',
    'description': 'You will participate in an experiment on decision making, where the biggest part of the payment will be the bonus payment. The experiment will help us understand how people learn from experience.',
    'frame_height': 800,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24, # 7 days
    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': [
    {
        'QualificationTypeId': "000000000000000000L0",
        'Comparator': "GreaterThan",
        'IntegerValues': [95]
    },
    {
        'QualificationTypeId': "00000000000000000071",
        'Comparator': "EqualTo",
        'LocaleValues': [{
            'Country': "US",
        }]
    }
    ]
}

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.0005,
    'participation_fee': 0.25,
    'mturk_hit_settings': mturk_hit_settings,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'causal_reasoning_experiment',
        'display_name': "Causal Reasoning",
        'num_demo_participants': 3,
        'num_rounds_to_show':100,
        'reward_to_show': 200,
        'app_sequence': ['lobby', 'causal_reasoning_experiment'],
    }
    # ,
    # {
    #     'name': 'survey',
    #     'display_name': "Survey",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['survey'],
    # }
]


# see the end of this file for the inactive session configs


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    {
        'name': 'econ101',
        'display_name': 'Econ 101 class',
        'participant_label_file': '_rooms/econ101.txt',
    },
    {
        'name': 'live_demo',
        'display_name': 'Room for live demo (no participant labels)',
    },
]


# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """
Here are various games implemented with
oTree. These games are open
source, and you can modify them as you wish.
"""

# don't share this with anybody.
SECRET_KEY = '9wtw-y$i7mp0e5gevgfqvgpoj0ml)z*%r=!=3vge4i*-o-^++&'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
