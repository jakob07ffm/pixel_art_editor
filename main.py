import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and grid settings
screen_width = 800
screen_height = 600
grid_size = 20
grid_color = (200, 200, 200)
cell_size = screen_width // grid_size

# Define colors
colors = [
    (255, 255, 255),  # White (for erasing)
    (50, 50, 250),    # Blue
    (250, 50, 50),    # Red
    (50, 250, 50),    # Green
    (250, 250, 50)    # Yellow
]

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pixel Art Editor")

# Initialize grid
grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

# Current color index
current_color = 1

def draw_grid():
    for row in range(grid_size):
        for col in range(grid_size):
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, grid_color, rect, 1)
            color_index = grid[row][col]
            if color_index != 0:
                pygame.draw.rect(screen, colors[color_index], rect)

def draw_palette():
    palette_height = 50
    palette_rect = pygame.Rect(0, screen_height - palette_height, screen_width, palette_height)
    pygame.draw.rect(screen, (150, 150, 150), palette_rect)

    for i, color in enumerate(colors):
        rect = pygame.Rect(i * (cell_size + 10), screen_height - palette_height + 10, cell_size, cell_size)
        pygame.draw.rect(screen, color, rect)
        if i == current_color:
            pygame.draw.rect(screen, (0, 0, 0), rect, 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if y < screen_height - 50:
                col = x // cell_size
                row = y // cell_size
                if event.button == 1:  # Left mouse button
                    grid[row][col] = current_color
                elif event.button == 3:  # Right mouse button
                    current_color = (current_color + 1) % len(colors)
            else:
                # Clicked in the palette area
                palette_index = x // (cell_size + 10)
                if 0 <= palette_index < len(colors):
                    current_color = palette_index

    screen.fill((255, 255, 255))
    draw_grid()
    draw_palette()
    pygame.display.flip()

pygame.quit()
sys.exit()
