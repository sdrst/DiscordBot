import random
from datetime import date

class Boy:
    def __init__(self):
        self.current_date = date.today()
        self.filled_date = None
        self.selected = False
        self.boy_of_the_day = None

    def isSelected(self):
        return self.selected

    def getBoy(self):
        return self.boy_of_the_day

    def boy_of_the_day(self, members):
        self.selected = True
        self.filled_date = date.today()
        bots = ['MEE6', 'Simple Poll', 'LolCounters']

        boy = random.randint(0, len(members))

        while members[boy] in bots:
            boy = random.randint(0, len(members))

        self.boy_of_the_day = members[boy]
        return self.boy_of_the_day
