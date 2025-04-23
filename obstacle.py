import pygame
import random

class Obstacle:
    def __init__(self, x, y):
        self.image = pygame.image.load("barrier.png")
        self.image = pygame.transform.scale(self.image, (50, 100))  # Resize
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = random.randint(3, 8)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 600:  # Reset if it goes out of screen
            self.rect.y = random.randint(-600, -50)
            self.rect.x = random.randint(100, 700)

    def draw(self, screen):
        screen.blit(self.image, self.rect)