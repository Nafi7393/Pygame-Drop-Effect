import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 500
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (193, 193, 193)
FPS = 63


class RainDrop:
    def __init__(self):
        self.color = None
        self.width = None
        self.speed = None
        self.length = None
        self.depth = None
        self.y = None
        self.x = None
        self.reset()

    def reset(self, start_y_range=(-HEIGHT, 0)):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(start_y_range[0], start_y_range[1])
        self.depth = random.uniform(0.1, 1.0)
        self.length = int(self.depth * 20)
        self.speed = self.depth * 10
        self.width = max(1, int(self.depth * 3))  # Width ranges from 1 to 3
        self.color = (WHITE[0], WHITE[1], WHITE[2], int(self.depth * 255))  # Transparency based on depth

    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.reset(start_y_range=(-20, 0))  # Reset within a smaller range once on screen

    def draw(self, surface):
        end_y = self.y + self.length
        pygame.draw.line(surface, self.color, (self.x, self.y), (self.x, end_y), self.width)


class Rain:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Cool Rain Effect")
        self.clock = pygame.time.Clock()
        self.raindrops = [RainDrop() for _ in range(200)]
        for raindrop in self.raindrops:
            raindrop.reset(start_y_range=(-HEIGHT, HEIGHT))  # Initialize raindrops across the entire height
        self.overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)  # For transparency

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)
            self.screen.fill(BLACK)
            self.overlay.fill(BLACK)  # Clear the overlay

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for raindrop in self.raindrops:
                raindrop.fall()
                raindrop.draw(self.overlay)

            self.screen.blit(self.overlay, (0, 0))
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    rain = Rain()
    rain.run()
