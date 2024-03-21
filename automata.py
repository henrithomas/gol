import sys
import pygame
import numpy as np
import random

class Automata:
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

        self.grid = self.new_grid()

    def new_grid(self):
        grid = np.zeros(shape=(self.rows, self.columns),dtype=bool)
        starter = random.randrange(self.columns)
        grid[0][self.columns - 1] = True
        return grid

    def rule30(self, iteration):
        left = False
        center = False
        right = False 
        if iteration > 0:
            for i in range(self.columns):
                if i == 0:
                    left = False
                    center = self.grid[iteration - 1, i]
                    right = self.grid[iteration - 1, i + 1]
                elif i == (self.columns - 1):
                    left = self.grid[iteration - 1, i - 1]
                    center = self.grid[iteration - 1, i]
                    right = False
                else:
                    left = self.grid[iteration - 1, i - 1]
                    center = self.grid[iteration - 1, i]
                    right = self.grid[iteration - 1, i + 1]

                self.grid[iteration, i] = (left ^ (center | right))

    def rule110(self, iteration):
        left = False
        center = False
        right = False 
        if iteration > 0:
            for i in range(self.columns):
                if i == 0:
                    left = False
                    center = self.grid[iteration - 1, i]
                    right = self.grid[iteration - 1, i + 1]
                elif i == (self.columns - 1):
                    left = self.grid[iteration - 1, i - 1]
                    center = self.grid[iteration - 1, i]
                    right = False
                else:
                    left = self.grid[iteration - 1, i - 1]
                    center = self.grid[iteration - 1, i]
                    right = self.grid[iteration - 1, i + 1]

                self.grid[iteration, i] = ((left and center and (not right)) 
                                            or (left and (not center) and right)
                                            or ((not left) and center and right)
                                            or ((not left) and center and (not right))
                                            or ((not left) and (not center) and right))

    def draw_grid(self):
        for row in range(self.rows):
            for col in range(self.columns):
                if self.grid[row, col]:
                    pygame.draw.rect(self.surface, self.active_color, [row * self.scale, col * self.scale, self.scale - self.offset, self.scale - self.offset])
                else:
                    pygame.draw.rect(self.surface, self.inactive_color, [row * self.scale, col * self.scale, self.scale - self.offset, self.scale - self.offset])

    def draw_grid_row(self, iteration):
        for col in range(self.columns):
            if self.grid[iteration, col]:
                pygame.draw.rect(self.surface, self.active_color, [col * self.scale, iteration * self.scale, self.scale - self.offset, self.scale - self.offset])
            else:
                pygame.draw.rect(self.surface, self.inactive_color, [col * self.scale, iteration * self.scale, self.scale - self.offset, self.scale - self.offset])
 

    def update_grid(self):
        self.grid = np.random.randint(0, 2, size=(self.rows, self.columns), dtype=bool)

    def run(self, iteration):
        self.rule30(iteration)
        self.draw_grid_row(iteration)
        # self.draw_grid()
        # self.update_grid()

    def reset_grid(self):
        self.grid = self.new_grid()

pygame.init()

WIDTH = 300
HEIGHT = 300
SCALE = 5
fps = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

automata = Automata(screen, width=WIDTH, height=HEIGHT, scale=SCALE)

screen.fill((0, 0, 0))

for i in range(int(HEIGHT / SCALE)):
    if i == int(HEIGHT / SCALE):
        i = 0
        screen.fill((0, 0, 0))
        automata.reset_grid()
        # pygame.display.update()

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    automata.run(i)
    pygame.display.update()

    pygame.image.save(screen , f'.\\exports\\img\\iter{i}.jpg')