from cgitb import text
from turtle import color
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

class Tile:
    COLORS = [
        (179, 232, 238), #COLOR FOR 2
        (133, 224, 235), #COLOR FOR 4
        (84, 208, 223), #COLOR FOR 8
        (54, 178, 193), #COLOR FOR 16
        (37, 151, 165), #COLOR FOR 32
        (32, 134, 146), #COLOR FOR 64
        (49, 118, 126), #COLOR FOR 128
        (14, 75, 82), #COLOR FOR 256
        (15, 49, 54), #COLOR FOR 512
        (10, 38, 42), #COLOR FOR 1024
        (3, 15, 17), #COLOR FOR 2048
        (7, 54, 32), #COLOR FOR 4096
    ]

    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.x = col * RECT_WIDTH
        self.y = row * RECT_HEIGHT

    def get_color(self):
        color_index = int(math.log2(self.value)) - 1
        color = self.COLORS[color_index]
        return color
    
    def draw(self, window):
        color = self.get_color()
        pygame.draw.rect(window, color, (self.x, self.y, RECT_WIDTH, RECT_HEIGHT))

        text = FONT.render(str(self.value), 1, FONT_COLOR)
        window.blit(
            text, 
            (self.x + (RECT_WIDTH / 2 - text.get_width()/2), 
             self.y + (RECT_HEIGHT / 2 - text.get_height()/2))
        )

    def set_pos(self):
        pass

    def move(self, delta):
        if direction == "up":
            self.row -= 1
        elif direction == "down":
            self.row += 1
        elif direction == "left":
            self.col -= 1
        elif direction == "right":
            self.col += 1

# create a function to draw the grid lines

def draw_grid(window):
    for row in range(1, ROWS):
        y = row * RECT_HEIGHT
        pygame.draw.line(window, OUTLINE_COLOR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)

    for col in range(1, COLS):
        x = col * RECT_WIDTH
        pygame.draw.line(window, OUTLINE_COLOR, (x, 0), (x, HEIGHT), OUTLINE_THICKNESS)
            
    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICKNESS)
    
# function to display the window
def draw(window,  tiles):
    window.fill(BACKGROUND_COLOR)

    for tile in tiles.values():
        tile.draw(window)

    draw_grid(window)

    pygame.display.update()

# function to get a random position
def get_random_pos(tiles):
    row = None
    col = None
    while True:
        row = random.randrange(0, ROWS)
        col = random.randrange(0, COLS)
        
        if f"{row}{col}" not in tiles:
            break
    
    return row, col

# function to create a new tile
def generate_tiles():
    tiles = {}
    for _ in range(2):
        # generate a random row and column to place the tile
        row, col = get_random_pos(tiles)
        tiles[f"{row}{col}"] = Tile(2, row, col)

    return tiles

def main(window):
    clock = pygame.time.Clock()
    run = True

    tiles = generate_tiles()
    # "00": Tile(2, 0, 0), "20": Tile(4, 0, 1), "30": Tile(8, 0, 2), "40": Tile(16, 0, 3)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        draw(window, tiles)

    pygame.quit()
# what this does is it checks if the file is being run directly
if __name__ == "__main__":
    main(WINDOW)