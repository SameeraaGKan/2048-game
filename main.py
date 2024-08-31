import pygame
import random
import math

pygame.init()

# declare constants
FPS = 60

WIDTH, HEIGHT = 700, 700
ROWS = 4
COLS = 4

RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS

OUTLINE_COLOR = (203, 212, 233)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (231, 230, 240)
FONT_COLOR = (1, 0, 8)

FONT = pygame.font.SysFont("comicsans", 60, bold = True)
MOVE_VELOCITY = 20

# create a pygame window

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

def draw_grid(window):
    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICKNESS)
    

def draw(window):
    window.fill(BACKGROUND_COLOR)

    draw_grid(window)

    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        draw(window)

    pygame.quit()

# what this does is it checks if the file is being run directly
if __name__ == "__main__":
    main(WINDOW)