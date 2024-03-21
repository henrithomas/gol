import sys
import pygame
import numpy as np
import random

class Life:
    def __init__(self, surface, width=1920, height=1080, scale=10, offset=1, active_color=(255, 255, 255), inactive_color=(0, 0, 0)):
        self.surface = surface
        self.width = width
        self.height = height
        self.scale = scale  
        self.offset = offset
        self.active_color = active_color
        self.inactive_color = inactive_color

        self.columns = int(height / scale)
        self.rows = int(width / scale)

        self.grid = np.random.randint(0, 2, size=(self.rows, self.columns), dtype=bool)

    def rule(self):
        pass

    def update_env(self):
        pass

    def update_grid(self):
        updated_grid = self.grid.copy()
        for row in range(self.rows):
            for col in range(self.columns):
                updated_grid[row, col] = self.update_cell(row, col)

        self.grid = updated_grid


    def update_cell(self, x, y):
        current_state = self.grid[x, y]
        alive_neighbors = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if x + i < 0 or y + j < 0:
                        continue
                    if i == 0 and j == 0:
                        continue
                    elif self.grid[x + i, y + j]:
                        alive_neighbors += 1
                except:
                    continue

        if current_state and alive_neighbors < 2: # underpopulation
            return False
        elif current_state and (alive_neighbors == 2 or alive_neighbors == 3): # lives
            return True
        elif current_state and alive_neighbors > 3: # overpopulation
            return False
        elif ~current_state and alive_neighbors == 3: # reproduction
            return True
        else:
            return current_state

    def draw_env(self):
        for row in range(self.rows):
            for col in range(self.columns):
                if self.grid[row, col]:
                    pygame.draw.rect(self.surface, self.active_color, [row * self.scale, col * self.scale, self.scale - self.offset, self.scale - self.offset])
                else:
                    pygame.draw.rect(self.surface, self.inactive_color, [row * self.scale, col * self.scale, self.scale - self.offset, self.scale - self.offset])

    def run(self):
        self.draw_env()
        self.update_grid()

def main():
    pygame.init()

    WIDTH = 1000
    HEIGHT = 750
    SCALE = 5
    fps = 10

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    life = Life(screen, width=WIDTH, height=HEIGHT, scale=SCALE)

    while True:
        clock.tick(fps)
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        life.run()
        pygame.display.update()

main()