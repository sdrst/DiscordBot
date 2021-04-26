import random

def main():
    b = Boy()

    if b.isSelected():
        b.getBoy()
    else:
        b.botd(['ernie mills', 'LolCounters', 'n8tehgr8', 'JulianF', 'NoahMcP', 'MEE6', 'Levy', 'PlsNoKillerino', 'jacksonisinthehouse?', 'ficuseater', 'paulkim96', 'Simple Poll', 'Firesnaps', 'Fred Frenackapan', 'Cellar Door', 'Jefts', 'BobbyAx', 'DrNibbs', 'Brendan', 'CellarDoor', 'cooperwilliams25', 'ernie_mills', 'toomuchcream', 'BallBaggTheBoy', 'PK', 'SailorRaj'])

class Boy:
    def __init__(self):
        self.selected = False
        self.boy_of_the_day = None

    def isSelected(self):
        return self.selected

    def getBoy(self):
        return self.boy_of_the_day

    def botd(self, members):
        self.selected = True
        bots = ['MEE6', 'Simple Poll', 'LolCounters']

        boy = random.randint(0, len(members))

        while members[boy] in bots:
            boy = random.randint(0, len(members))

        self.boy_of_the_day = members[boy]
        return self.boy_of_the_day

#main()
