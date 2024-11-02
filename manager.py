import organism
import numpy as np
import grid
import loss_function

CAMOUFLAGE = 30

def main():

    # INITIALITZE ORGANISMS
    number_of_organisms = 40

    # Create grid
    Grid = grid.Grid((CAMOUFLAGE, CAMOUFLAGE, CAMOUFLAGE))

    organisms = np.empty((number_of_organisms, number_of_organisms), dtype=organism.Organism)

    for x in range(number_of_organisms * number_of_organisms):
        organisms[x // number_of_organisms, x % number_of_organisms] = organism.Organism()
    
    Grid.drawGrid(organisms, 100)

    input("Press Enter to continue...")

    # GENETIC ALGORITHM
    while True:
       
        # Get organisms ordered by the camouflage
        organisms = loss_function.camouflage_ordered_organisms(organisms, CAMOUFLAGE)

        # Draw the sorted organisms on the grid
        Grid.drawGrid(organisms, 100)
        input("Press Enter to continue...")

        # Kill the weakest (50%) ones and reproduce the best (50%) ones
        for row in range(number_of_organisms // 2, number_of_organisms):
            for col in range(number_of_organisms):
                # Reproduce the best half to replace the weakest half
                organisms[row][col] = organisms[row - number_of_organisms // 2][col].reproduce()

        # Draw the updated organisms on the grid
        Grid.drawGrid(organisms, 100)

        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
