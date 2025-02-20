import random
responses=[
    'Yes, definitely!!',
    'No,not now',
    'Ask again later',
    'It is certain',
    'very doubtful',
    'Outlook is good',
    'Better not tell you',
    'Concentrate and ask again'
]
def generateResponse():
    return random.choice(responses)