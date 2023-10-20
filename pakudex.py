from pakuri import *


class Pakudex:  # pakudex class
    # Pakudex has a list of pakuri
    def __init__(self, capacity=20):  # allows pakudex to contain exactly capacity objects when completely full
        self.pakuris = []
        self.capacity = capacity
        self.size = 0
        self.species_array = []

    def get_size(self):  # returns the number of pakuri in the pakudex
        self.size = len(self.pakuris)
        return self.size

    def get_capacity(self):  # returns the capacity
        return self.capacity

    def get_species_array(self):  # same thing as get_stats and evolve_species
        self.species_array = []
        if len(self.pakuris) == 0:
            return []

        else:
            for pakuri in self.pakuris:
                species = pakuri.get_species()
                self.species_array.append(species)
        return self.species_array
        # self pakuris = [p1, p2, p3, p4]
        # for pakuri in self.pakuris
        # sp = get species of pakuri
        # append sp to final result list

    def get_stats(self, species):  # gets stats of each pakuri
        # attributes at 0,1,2 indices
        stats = []  # stats list
        for item in self.pakuris:
            if item.get_species() == species:
                stats.append(item.get_attack())
                stats.append(item.get_defense())
                stats.append(item.get_speed())
                return stats

        return None

    def sort_pakuri(self):  # sorts the pakudex
        self.pakuris.sort(key=lambda pakuri: pakuri.species)
        #self.species_array.sort()  # inbuilt python sort function

    def add_pakuri(self, species):  # adds pakuri to pakuris list
        # 1. check duplicates => unsuccessful
        if species in self.get_species_array():  # how to find duplicates
            print("Error: Pakudex already contains this species!")
            return False
        elif len(self.pakuris) == self.capacity:  # 2. when the list is full => unsuccessful
            print("Error: Pakudex is full!")
            return False

        else:
            new_species = Pakuri(species)
            self.pakuris.append(new_species)  # add pakuri into self.pakuri
            self.size += 1  # increment self.size by 1
            print(f"Pakuri species {new_species.species} successfully added!")
            return True

    def evolve_species(self, species):  # evolves the species within the pakudex
        if species in self.get_species_array():
            for pakuri in self.pakuris:
                if pakuri.get_species() == species:
                    pakuri.evolve()
            return True
        else:
            return False
