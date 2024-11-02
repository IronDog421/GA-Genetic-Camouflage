import numpy as np
import organism
import loss_function
from grid import Grid

CAMOUFLAGE = 30
NUM_ORGANISMS = 40

def initialize_organisms(num_organisms):
    organisms = np.empty((num_organisms, num_organisms), dtype=organism.Organism)
    for i in range(num_organisms * num_organisms):
        organisms[i // num_organisms, i % num_organisms] = organism.Organism()
    return organisms

def run_genetic_algorithm(grid, organisms, camouflage_color):
    epoc = 0
    while True:
        organisms = loss_function.camouflage_ordered_organisms(organisms, camouflage_color)

        grid.draw(organisms, 100, epoc)

        input("Press Enter to continue...")

        num_organisms = organisms.shape[0]
        for row in range(num_organisms // 2, num_organisms):
            for col in range(num_organisms):
                # Reproduce los organismos más aptos
                organisms[row][col] = organisms[row - num_organisms // 2][col].reproduce()

        grid.draw(organisms, 100, epoc)
        input("Press Enter to continue...")

        epoc +=1

def main():

    organisms = initialize_organisms(NUM_ORGANISMS)

    grid = Grid((CAMOUFLAGE, CAMOUFLAGE, CAMOUFLAGE), organisms, 1000)

    grid.draw(organisms, 100, 0)
    input("Press Enter to continue...")

    run_genetic_algorithm(grid, organisms, CAMOUFLAGE)

if __name__ == "__main__":
    main()
