import pygame

class Road:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = pygame.image.load("road.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.y = 0

    def update(self):
        self.y += 5  # Move the road down for the scrolling effect
        if self.y > self.height:
            self.y = 0

    def draw(self, screen):
        screen.blit(self.image, (0, self.y))
        screen.blit(self.image, (0, self.y - self.height))