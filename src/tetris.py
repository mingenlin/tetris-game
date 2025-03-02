import pygame
import random
import argparse
from game import TetrisGame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

def main():
    parser = argparse.ArgumentParser(description="Tetris Game")
    parser.add_argument('--speed', type=int, default=6, help='Set the game speed (frames per second)')
    args = parser.parse_args()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    
    game = TetrisGame()
    
    move_delay = 200  # Initial delay in milliseconds
    move_interval = 50  # Interval for fast movement in milliseconds
    last_move_time = pygame.time.get_ticks()
    
    running = True
    while running:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move('left')
                    last_move_time = current_time + move_delay
                elif event.key == pygame.K_RIGHT:
                    game.move('right')
                    last_move_time = current_time + move_delay
                elif event.key == pygame.K_DOWN:
                    game.move('down')
                    last_move_time = current_time + move_delay
                elif event.key == pygame.K_UP:
                    game.rotate()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and current_time - last_move_time >= move_interval:
            game.move('left')
            last_move_time = current_time
        if keys[pygame.K_RIGHT] and current_time - last_move_time >= move_interval:
            game.move('right')
            last_move_time = current_time
        if keys[pygame.K_DOWN] and current_time - last_move_time >= move_interval:
            game.move('down')
            last_move_time = current_time

        game.update()
        screen.fill(BLACK)
        game.draw(screen)
        pygame.display.flip()
        clock.tick(args.speed)  # Use the speed set by the user

    pygame.quit()

if __name__ == "__main__":
    main()