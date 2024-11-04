import pygame
import numpy as np
from constants import Constants

# Dimensiunile ferestrei și dimensiunea fiecărui tile
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
TILE_SIZE = 20

class Viewer:
    def __init__(self, maze):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Maze Viewer")

        # Setări labirint și agenți
        self.maze = maze

        # Variabile pentru zoom și scroll
        self.zoom = 1.0
        self.scroll_x = 0
        self.scroll_y = 0

    def draw_maze(self):
        rows, cols = len(self.maze.matrix[0]), len(self.maze.matrix[1])
       # print(rows, cols)
        tile_size = TILE_SIZE * self.zoom

        # Calculăm marginile vizibile ale viewport-ului
        start_col = max(0, int(-self.scroll_x / tile_size))
        end_col = min(cols, int((SCREEN_WIDTH - self.scroll_x) / tile_size) + 1)
        start_row = max(0, int(-self.scroll_y / tile_size))
        end_row = min(rows, int((SCREEN_HEIGHT - self.scroll_y) / tile_size) + 1)

        for y in range(start_row, end_row):
            for x in range(start_col, end_col):
                # Calculăm poziția celulei în funcție de scroll și zoom
                tile_x = x * tile_size + self.scroll_x
                tile_y = y * tile_size + self.scroll_y

                cell = self.maze.matrix[y][x]
                color = self.get_tile_color(cell.value)
                pygame.draw.rect(self.screen, color, (tile_x, tile_y, tile_size, tile_size))

    def get_tile_color(self, cell_value):
        if cell_value == Constants.WALL:
            return (0, 0, 0)        # Black for walls
        elif cell_value == Constants.PATH:
            return (255, 255, 255)  # White for path
        elif cell_value == Constants.ENTRANCE:
            return (0, 255, 0)      # Green for entrance
        elif cell_value == Constants.EXIT:
            return (255, 0, 0)      # Red for exit
        else:
            return (64, 64, 64)     # Gray for traps/others

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    self.zoom = min(self.zoom + 0.1, 5)
                elif event.key == pygame.K_MINUS:
                    self.zoom = max(self.zoom - 0.1, 0.5)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll up
                    self.zoom = min(self.zoom + 0.1, 5)
                elif event.button == 5:  # Scroll down
                    self.zoom = max(self.zoom - 0.1, 0.5)
            elif event.type == pygame.MOUSEMOTION:
                if event.buttons[0]:  # Dacă apăsăm butonul stânga al mouse-ului
                    self.scroll_x += event.rel[0]
                    self.scroll_y += event.rel[1]
                    
                    # Limităm scroll-ul pentru a evita ieșirea labirintului din ecran
                    max_scroll_x = -TILE_SIZE * self.zoom * len(self.maze.matrix[0]) + SCREEN_WIDTH
                    max_scroll_y = -TILE_SIZE * self.zoom * len(self.maze.matrix) + SCREEN_HEIGHT
                    self.scroll_x = min(0, max(self.scroll_x, max_scroll_x))
                    self.scroll_y = min(0, max(self.scroll_y, max_scroll_y))
        return True

    def run(self):
        running = True
        while running:
            self.screen.fill((255, 255, 255))  # Background alb
            running = self.handle_events()

        ## O solutie nu tocmai buna, afiseaza imaginea, dar este impractica
            # Afișează imaginea labirintului cu zoom și scroll
            # img_width, img_height = self.image_surface.get_size()
            # scaled_surface = pygame.transform.scale(
            #     self.image_surface, (int(img_width * self.zoom), int(img_height * self.zoom))
            # )
            # self.screen.blit(scaled_surface, (self.scroll_x, self.scroll_y))
        ##
            # Desenăm labirintul
            self.draw_maze()

            pygame.display.flip()
            pygame.time.Clock().tick(30)  # FPS limit

        pygame.quit()
