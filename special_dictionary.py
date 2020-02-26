
class SpecialDictionary:
    def __init__(self):
        self.definitions = {}

    def define(self, word, definition):
        self.definitions[word] = definition

    def get_definition(self, word):
        
        for item in self.definitions:
            if word in self.definitions:
                return self.definitions[word]


import special_dictionary

farm_animals = special_dictionary.SpecialDictionary()

farm_animals.define('horse', 'an adult equine')

farm_animals.define('bull', 'a male bovine')

print(farm_animals.get_definition('cow'))
