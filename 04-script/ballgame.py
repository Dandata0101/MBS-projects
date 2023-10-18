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

# Paths and directory
current_directory = os.getcwd()
mosquito_path = os.path.join(current_directory, "05-images", "ball.png")

# Load the static image
static_ball_image = pygame.image.load(mosquito_path).convert_alpha()
scaled_static_ball_image = pygame.transform.scale(static_ball_image, (60, 60))
static_ball_rect = scaled_static_ball_image.get_rect(topleft=(10, 10))

# Create font for points display
my_font = pygame.font.SysFont(None, 36)

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
        self.rect.x += random.choice([-1, 0, 1]) * 10
        self.rect.y += random.choice([-1, 0, 1]) * 10
        self.rect.x = max(0, min(self.window_width - self.width, self.rect.x))
        self.rect.y = max(0, min(self.window_height - self.height, self.rect.y))

def get_random_position(window_width, window_height, image_width, image_height):
    random_x = random.randint(0, window_width - image_width)
    random_y = random.randint(0, window_height - image_height)
    return random_x, random_y

mosquito = Mosquito(50, 50, SCREEN_WIDTH, SCREEN_HEIGHT)
points = 0


mosquito_hit = False
hit_text_timer = 0
HIT_TEXT_DURATION = 1000  # 1 second in milliseconds

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    elapsed_time = clock.tick(60)  # This returns the time in milliseconds since the last frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if mosquito.rect.collidepoint(mouse_x, mouse_y):
                mosquito.reset_position()
                hit_text_surface = my_font.render('Hit!!', True, (0, 0, 0))
                points += 5
                mosquito_hit = True
                hit_text_timer = HIT_TEXT_DURATION

    if mosquito_hit:
        hit_text_timer -= elapsed_time
        if hit_text_timer <= 0:
            mosquito_hit = False

    mosquito.update()

    screen.fill(WHITE)
    screen.blit(mosquito.image, mosquito.rect)
    
    # Draw the static ball image
    screen.blit(scaled_static_ball_image, static_ball_rect.topleft)

    # Display the points next to the static ball image
    points_display = my_font.render(f'Points: {points}', True, (0, 0, 0))
    screen.blit(points_display, (static_ball_rect.right + 10, 10))
    
    # Display "Hit!!" if the mosquito was clicked
    if mosquito_hit:
        screen.blit(hit_text_surface, (SCREEN_WIDTH // 2 - hit_text_surface.get_width() // 2, SCREEN_HEIGHT // 2 - hit_text_surface.get_height() // 2))

    pygame.display.flip()


# Cleanup to prevent screen freeze
del screen
pygame.time.wait(300)
pygame.quit()
sys.exit()
