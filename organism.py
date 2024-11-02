import random
from functools import total_ordering
import copy

@total_ordering
class Organism:
    def __init__(self, dna=None):
        if(dna is None):
            self.dna = random.randint(0, 255)
        else: self.dna = dna

    def reproduce(self):
        new_organism = copy.deepcopy(self)
        
        aux = random.randint(1, 100)  # mutation chance
        if aux == 1:
            print("Organism mutated!!")
            new_organism.dna = random.randint(0, 255)
        return new_organism

    def __eq__(self, other):
        if isinstance(other, Organism):
            return self.dna == other.dna
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Organism):
            return self.dna < other.dna
        return NotImplemented
    
    def __str__(self):
        return str(self.dna)
    
    def __repr__(self):
        return str(self.dna)
