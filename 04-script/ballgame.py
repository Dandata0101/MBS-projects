import os
import sys
import pygame
import random
from pygame.sprite import Sprite

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)

# Create a screen/window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mosquito Game")

# Paths
current_directory = os.getcwd()
mosquito_path = os.path.join(current_directory, "05-images", "ball.png")

class Mosquito(Sprite):
    def __init__(self, width, height, window_width, window_height):
        super().__init__()
        self.raw_image = pygame.image.load(mosquito_path).convert_alpha()
        self.image = pygame.transform.scale(self.raw_image, (width, height))
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.window_width = window_width
        self.window_height = window_height
        self.reset_position()

    def reset_position(self):
        random_x, random_y = get_random_position(self.window_width, self.window_height, self.width, self.height)
        self.rect.topleft = (random_x, random_y)

    def update(self):
        self.rect.x += random.choice([-1, 0, 1]) * 5
        self.rect.y += random.choice([-1, 0, 1]) * 5
        self.rect.x = max(0, min(self.window_width - self.width, self.rect.x))
        self.rect.y = max(0, min(self.window_height - self.height, self.rect.y))

def get_random_position(window_width, window_height, image_width, image_height):
    random_x = random.randint(0, window_width - image_width)
    random_y = random.randint(0, window_height - image_height)
    return random_x, random_y

mosquito = Mosquito(50, 50, SCREEN_WIDTH, SCREEN_HEIGHT)

points = 0
font = pygame.font.SysFont(None, 36)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if mosquito.rect.collidepoint(mouse_x, mouse_y):
                mosquito.reset_position()
                points += 5

    mosquito.update()

    screen.fill(WHITE)
    screen.blit(mosquito.image, mosquito.rect)
    point_text = font.render(f"Points: {points}", True, (0, 0, 0))
    screen.blit(point_text, (10, 10))
    pygame.display.flip()

# Cleanup
del screen
pygame.time.wait(300)
pygame.quit()
sys.exit()
