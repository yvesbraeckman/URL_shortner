import random
from functools import wraps

def remember(f):
    questions = set()

    @wraps(f)
    def wrapper(*args, **kwargs):
        if args[0] in questions:
            print("You have asked this question before")
        else:
            questions.add(args[0])
            return f(*args, **kwargs)
    return wrapper


@remember
def magic_eight_ball(question):
    answers = ["It is certain", "It is decidedly so", "Without a doubt", "Better not tell you now", "Cannot predict now",
               "Maybe rephrase the question", "Don’t count on it", "Outlook not so good", "My reply is no"]
    getal = random.randint(0, 8)
    print(answers[getal])


magic_eight_ball("test")
magic_eight_ball("b")
magic_eight_ball("a")
magic_eight_ball("test")
magic_eight_ball("c")
magic_eight_ball("a")
magic_eight_ball("test")