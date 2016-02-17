#Angel D.
#CatDiary

import random, sys, locale
from termcolor import colored
from time import sleep

locale.setlocale(locale.LC_ALL, 'en_US')

class CatDiary:

    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.diary = ["Day 983 of captivity: My captors continue to taunt me with bizarre little dangly objects.",
        "Day 672 of captivity: I am convinced that the bird is an informant. I observe him communicating with the guards regularly. My captives have arranged protective custody for him in an elevated cell. He is safe. For now.",
        "Day 392 of captivity: There was some sort of assembly with their accomplices tonight. I was placed in solitary confinement for the duration of the event due to the power of allergies. I must figure out what this is and how to use it to my advantage.",
        "Day 232 of captivity: Today, I was almost successful in an attemp to assassinate one of my tormentors by weaving around his feet as he was walking. I must try this again tomorrow but at the top of the stairs.",
        "Day 108: The humans dine lavishly on fresh meat while the other inmates and I are fed hash and dried nuggets. Though my contempt for the hash is perfectly clear, I must nevertheless eat something to keep up my strength."]


    def excerpt(self):
        #gives a diary excerpt and grumpiness level by printing to terminal/shell using typeWriter
        self.typeWriter(colored(self.name + "'s Diary\n" + random.choice(self.diary) + "\n", 'green'))
        self.typeWriter(colored("Grumpiness Level: " + self.catorial(random.choice(range(1, 11))) + "\n", 'green'))

    

    def hatedThings(self, list):
        self.hateList = list

    

    def typeWriter(self, str):
        #prints given string to shell/terminal letter by letter to simulate typing
        while True:
            for x in str: 
                sleep(0.1)
                sys.stdout.write(x)
                sys.stdout.flush()
            break

    

    def catorial(self, n):
        #returns the factorial of n in the form of a formatted string i.e. '1,500'
        answer = 1
        print n
        if n > 1:
            for i in range (1, n+1):
                answer = answer * i
        answer = locale.format("%d", answer, grouping=True)
        return answer



def cats():
    #makes cat instance and calls excerpt() method
    cat = CatDiary(9, "Earl")
    cat.excerpt()
    cat.hatedThings(["Smiling", "Displays of affection", "Human enjoyment"])
    print "Hate List: " 
    print cat.hateList



cats()



