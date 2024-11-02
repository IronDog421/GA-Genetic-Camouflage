import math
import sys
import pygame

class Grid:
    def __init__(self, CAMOUFLAGE):
        self.CAMOUFLAGE = CAMOUFLAGE
        pygame.init()
        display_info = pygame.display.Info()
        self.WINDOW_SIZE = min(display_info.current_w, display_info.current_h) - 20  # Usa el tamaño menor para hacer una cuadrícula cuadrada

    def drawGrid(self, organisms, milliseconds):
        num_cells = organisms.shape[0]
        cell_size = round(self.WINDOW_SIZE / num_cells)
        self.WINDOW_SIZE = cell_size * num_cells

        SCREEN = pygame.display.set_mode((self.WINDOW_SIZE, self.WINDOW_SIZE))
        SCREEN.fill(self.CAMOUFLAGE)

        margin = 1

        # Recorre filas y luego columnas
        for row in range(num_cells):
            for col in range(num_cells):
                x = col * cell_size
                y = row * cell_size

                # Si el organismo está en un borde, ajustamos el margen
                left_margin = margin if col > 0 else 0
                right_margin = margin if col < num_cells - 1 else 0
                top_margin = margin if row > 0 else 0
                bottom_margin = margin if row < num_cells - 1 else 0

                # Ajusta el rectángulo considerando los márgenes
                rect = pygame.Rect(
                    x + left_margin,
                    y + top_margin,
                    cell_size - (left_margin + right_margin),
                    cell_size - (top_margin + bottom_margin)
                )

                color = organisms[row, col].dna
                pygame.draw.rect(SCREEN, (color, color, color), rect, 0)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

        pygame.time.delay(milliseconds)
