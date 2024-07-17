import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and grid settings
screen_width = 800
screen_height = 600
grid_size = 20
grid_color = (200, 200, 200)
cell_color = (50, 50, 250)
cell_size = screen_width // grid_size

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Grid Generator")

# Create a 2D array to keep track of cell states
grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

# Function to draw the grid
def draw_grid():
    for row in range(grid_size):
        for col in range(grid_size):
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, grid_color, rect, 1)
            if grid[row][col] == 1:
                pygame.draw.rect(screen, cell_color, rect)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            col = x // cell_size
            row = y // cell_size
            grid[row][col] = 1 - grid[row][col]  # Toggle cell state

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the grid
    draw_grid()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
