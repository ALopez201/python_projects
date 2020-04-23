class State:
    'Defines states and universities'
    def __init__(self, aName):
        self.name = aName
        self.universities = []

    def addUniversity(self, x):
        self.universities.append(x)

    def is_home_of(self, x):
        if x not in self.universities:
            return False
        else:
            return True

