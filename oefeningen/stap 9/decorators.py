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


def remember_recent_calls(f):
    od = OrderedDict()
    print(od)

    @wraps(f)
    def wrapper(*args, **kwargs):
        if args[0] in od:
            print(od[args[0]])
            return od[args[0]]
        else:
            print(f(*args, **kwargs))
            result = f(*args, **kwargs)
            if len(od) >= 5:
                od.popitem(last=False)
            od[args[0]] = result
            return result