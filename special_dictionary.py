
class SpecialDictionary:
    def __init__(self):
        self.definitions = {}

    def define(self, word, definition):
        if word not in self.definitions:
            self.definitions[word] = definition

    def get_definition(self, word):
        
        if item in self.definitions:
            
            return self.definitions[word]


import special_dictionary

farm_animals = special_dictionary.SpecialDictionary()

farm_animals.define('horse', 'an adult equine')


farm_animals.define('cat', 'a feline')



print(farm_animals.definitions['horse'])
print(farm_animals.definitions['cat'])
