# Pygame Template
# Use this to start a new Pygame project
# KidsCanCode 2015
import pygame
import random
import os

# define some colors (R, G, B)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)       
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
LIME = (0, 128, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
CYAN = (0, 255, 255)

# basic constants to set up your game
WIDTH = 640
HEIGHT = 480
FPS = 30
BGCOLOR = WHITE

# initialize pygame
pygame.init()
# initialize sound - uncomment if you're using sound
# pygame.mixer.init()
# create the game window and set the title
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
# start the clock
clock = pygame.time.Clock()

# set the 'running' variable to False to end the game
running = True
# start the game loop

font = pygame.font.SysFont(None, 24)
hello_paul = font.render('Hello Paul :)', True, BLUE)

sad_baby = pygame.image.load(os.path.join('assets/images', 'baby.jpg'))

guitar = pygame.mixer.Sound(os.path.join('assets/sounds', 'guitar.wav'))

pygame.mixer.Sound.play(guitar)

i = 0
while running:
    # keep the loop running at the right speed
    clock.tick(FPS)
    # Game loop part 1: Events #####
    for event in pygame.event.get():
        # this one checks for the window being closed
        if event.type == pygame.QUIT:
            pygame.quit()
        # add any other events here (keys, mouse, etc.)

    # Game loop part 2: Updates #####

    # Game loop part 3: Draw #####
    screen.fill(BGCOLOR)

    pygame.draw.circle(screen, BLACK, [50, 50], 10)

    pygame.draw.aalines(screen, BLUE, False, [[0, 80], [50, 90], [200, 80], [220, 30]])

    screen.blit(hello_paul, (20, 20))

    screen.blit(sad_baby, (-450 + (i * 3), -450 + (i * 3)))
    # after drawing, flip the display
    pygame.display.flip()

    if i < 270:
      i += 1
    else:
      i = 0

# close the window
pygame.quit()