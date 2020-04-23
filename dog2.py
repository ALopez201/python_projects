'''
Anthony Lopez
HW11 CS100 108
SP2019
'''

class Dog:
    'This is a class of dog breeds and names.'
    species = 'canis familiaris' 
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []

    def teach(self, trick):
        self.tricks.append(trick)
        print('Your dog now knows how to ' + trick)

    def knows(self, trick):
        if trick in self.tricks:
            print('Your dog knows how to ' + trick)
            return True
        else:
            print('Your dog does not know how to ' + trick)

            return False

