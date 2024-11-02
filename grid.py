import sys
import pygame

class Grid:
    def __init__(self, camouflage_color, organisms, delay_ms):
        self.CAMOUFLAGE_COLOR = camouflage_color
        pygame.init()
        display_info = pygame.display.Info()
        self.WINDOW_SIZE = min(display_info.current_w, display_info.current_h) - 20 

        self.TEXT_WIDTH = 200
        self.SCREEN_WIDTH = self.WINDOW_SIZE + self.TEXT_WIDTH
        self.SCREEN_HEIGHT = self.WINDOW_SIZE

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

    def draw(self, organisms, delay_ms, epoc):

        num_cells = organisms.shape[0]
        cell_size = round(self.WINDOW_SIZE / num_cells)
        self.WINDOW_SIZE = cell_size * num_cells 

        self.screen.fill(self.CAMOUFLAGE_COLOR)


        font = pygame.font.Font(None, 36)
        margin = 1

        for row in range(num_cells):
            for col in range(num_cells):
                x = col * cell_size
                y = row * cell_size

                left_margin = margin if col > 0 else 0
                right_margin = margin if col < num_cells - 1 else 0
                top_margin = margin if row > 0 else 0
                bottom_margin = margin if row < num_cells - 1 else 0

                rect = pygame.Rect(
                    x + left_margin,
                    y + top_margin,
                    cell_size - (left_margin + right_margin),
                    cell_size - (top_margin + bottom_margin)
                )

                color_value = organisms[row, col].dna
                pygame.draw.rect(self.screen, (color_value, color_value, color_value), rect)

        text_surface = font.render("Generation" + str(epoc), True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.WINDOW_SIZE + self.TEXT_WIDTH // 2, self.SCREEN_HEIGHT // 2))
        self.screen.blit(text_surface, text_rect)

        pygame.display.update()
        pygame.time.delay(delay_ms)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
