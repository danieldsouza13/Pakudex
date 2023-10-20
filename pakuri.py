class Pakuri:

    def __init__(self, species):  # constructor class
        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13

    def get_species(self):  # returns species
        return self.species

    def get_attack(self):  # returns attack
        return self.attack

    def get_defense(self):  # returns defense
        return self.defense

    def get_speed(self):  # returns speed
        return self.speed

    # setter: update the attribute's value
    def set_attack(self, new_attack):
        self.attack = new_attack

    def evolve(self):
        # update self.attack, self.defense, self.speed
        # don't need to return anything
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3




