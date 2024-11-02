import numpy as np

def error(CAMOUFLAGE_COLOR, ORGANISM_COLOR):
    return abs(CAMOUFLAGE_COLOR - ORGANISM_COLOR)

def camouflage_ordered_organisms(organisms, CAMOUFLAGE):
     # Calculate the error of each organism
    flatten_organisms = organisms.flatten()

    # Calculate the error for each organism and store it in error_organisms
    error_values = np.array([error(CAMOUFLAGE, org.dna) for org in flatten_organisms])

    # Get sorted indices based on error values
    sorted_indices = np.argsort(error_values)
    sorted_organisms = flatten_organisms[sorted_indices].reshape(organisms.shape)

    return sorted_organisms