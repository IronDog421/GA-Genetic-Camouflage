# Grid Simulation with Pygame

A dynamic grid-based simulation using Pygame, where each cell represents an organism with a unique DNA value displayed in grayscale. The simulation updates and displays the current generation in real-time.

## Features

- **Grid Visualization**: Each organism's DNA is represented by a grayscale cell within the grid.
- **Real-Time Generation Tracking**: Displays the current generation number on the screen.
- **Adjustable Frame Delay**: Control the speed of the simulation by setting the delay between frames.

## Requirements

This project requires Python 3.x and the pygame library. Ensure both are installed before running the project.

### Installing Pygame

Install Pygame using pip:

pip install pygame

## Usage

1. **Clone the Repository**:

   Clone the repository to your local machine:

   git clone https://github.com/yourusername/your-repository.git
   cd your-repository

2. **Set Up the Environment**:

   Ensure all dependencies are installed. You can install Pygame as follows:

   pip install pygame

3. **Configure Parameters**:

   In the code, you can adjust several parameters for the simulation:

   - `camouflage_color`: RGB tuple that sets the background color for the grid.
   - `organisms`: A NumPy array representing each organism’s DNA value, which determines the grayscale color of each cell.
   - `delay_ms`: Integer specifying the delay between frames in milliseconds, allowing control over the simulation speed.

4. **Run the Simulation**:

   Execute the main Python file to start the simulation:

   python main.py

   The program will display a grid, where each cell represents an organism with a grayscale color based on its DNA value. The current generation number will update in real-time on the right side of the window.

## Example Code

Below is an example demonstrating how to initialize and run the `Grid` simulation.

import numpy as np
from grid import Grid

# Define the organism matrix with random DNA values
organisms = np.random.randint(0, 256, size=(50, 50))

# Initialize the grid with a camouflage color and a delay of 100ms
grid = Grid(camouflage_color=(50, 50, 50), organisms=organisms, delay_ms=100)

# Run the simulation for 100 generations
for generation in range(100):
    grid.draw(organisms=organisms, delay_ms=100, epoc=generation)

This code snippet will initialize a `Grid` object and render the simulation for 100 generations, with a 100-millisecond delay between frames.

## Set Up the Environment on macOS

After creating the virtual environment, you’ll need to activate it to install dependencies and run the project in an isolated environment on macOS.

1. **Create the Virtual Environment**:

   If you haven’t created the virtual environment yet, do so by running:
   ```
   python3 -m venv env
   ```

2. **Activate the Environment**:

   To activate the virtual environment on macOS, use the following command:
   ```
   source env/bin/activate
   ```
   Once activated, you should see `(env)` appear at the beginning of your terminal prompt, indicating that the environment is active.

3. **Install Dependencies**:

   Now that the environment is active, you can install required dependencies such as Pygame:
   ```
   pip install pygame
   ```
4. **Deactivate the Environment**:

   When you’re done working, deactivate the virtual environment with:
   ```
   deactivate
   ```
This returns your terminal to the global Python environment.

By following these steps, you’ll be able to manage dependencies in an isolated environment on macOS, keeping them separate from other projects and the system’s default Python packages.

## Contributing

We welcome contributions from the community! If you’d like to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

Please ensure your code adheres to PEP 8 standards and includes relevant documentation and comments.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions, feedback, or suggestions, feel free to reach out:

- **Email**: your.email@example.com
- **GitHub**: yourusername
