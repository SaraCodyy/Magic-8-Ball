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
def getUserInput():
    question=input("Ask the magical 8 ball a question(type'exit' to quit):")
    if question.lower()=="exit":
        return None
    return question
def display(response):
    print(response)
def playAgain():
    while True:
        choice=input("Do you want to ask another question?")
        if choice=="yes":
            return True
        elif choice=='no':
            print("Thanks for playing good Bye!!")
            return False
        else:
            print("Please Type Yes or no")
def Magic8ball():
    print("Welcome to the Magic ball!!")
    while True:
        question=getUserInput()
        if question is None:
            break
        response=generateResponse()
        display(response)
        if not playAgain():
            break
Magic8ball()


