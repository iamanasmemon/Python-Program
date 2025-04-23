import pygame
import random
from vehicle import Vehicle
from obstacle import Obstacle
from road import Road # type: ignore

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 734, 823
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vehicle Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Load assets
road = Road(WIDTH, HEIGHT)
player = Vehicle(x=WIDTH//2, y=HEIGHT-120, image_path="car.png")
obstacles = [Obstacle(x=random.randint(100, WIDTH-100), y=random.randint(-600, -50)) for _ in range(5)]

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear the screen
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update road
    road.update()
    road.draw(screen)
    
    # Update player
    keys = pygame.key.get_pressed()
    player.update(keys)
    player.draw(screen)

    # Update obstacles
    for obstacle in obstacles:
        obstacle.update()
        obstacle.draw(screen)
        # Collision detection
        if player.rect.colliderect(obstacle.rect):
            print("Collision detected!")
            running = False  # End the game on collision

    # Refresh the screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()