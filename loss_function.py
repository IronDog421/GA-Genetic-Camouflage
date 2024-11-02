import numpy as np

def error(CAMOUFLAGE_COLOR, ORGANISM_COLOR):
    return abs(CAMOUFLAGE_COLOR - ORGANISM_COLOR)

def camouflage_ordered_organisms(organisms, CAMOUFLAGE):

    flatten_organisms = organisms.flatten()

    error_values = np.array([error(CAMOUFLAGE, org.dna) for org in flatten_organisms])

    sorted_indices = np.argsort(error_values)
    sorted_organisms = flatten_organisms[sorted_indices].reshape(organisms.shape)

    return sorted_organisms