#parent class: zoo animals in general
class zoo_animal:
    def __init__(self, species, name, gender, food):
        self.species = species
        self.name = name 
        self.gender = gender
        self.food = food

#two child classes, specific animals have extra attributes,
#but still inherit all the same attributes as the animal class
class bear(zoo_animal):
    def __init__(self, bear_type, claw_length):
        self.bear_type = bear_type
        self.claw_length = claw_length

class dolphin(zoo_animal):
    def __init__(self, dolphin_type, water_type):
        self.dolphin_type = dolphin_type
        self.water_type = water_type