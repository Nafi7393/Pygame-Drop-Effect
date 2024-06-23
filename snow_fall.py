import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
SNOW_SIZE = 10
SNOW_NUM = 200

# Create a Snowflake class
class Snowflake:
    def __init__(self, screen):
        self.screen = screen
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(-SCREEN_HEIGHT, SCREEN_HEIGHT)
        self.size = random.randint(5, SNOW_SIZE)  # Varying sizes
        self.speed = random.randint(1, 4)  # Varying speeds
        self.angle = random.uniform(0, math.pi * 2)  # Random initial angle for tilt

    def update(self):
        self.y += self.speed
        self.x += math.sin(self.angle) * 0.5  # Small random tilt
        if self.y > SCREEN_HEIGHT:
            self.y = random.randint(-50, -10)
            self.x = random.randint(0, SCREEN_WIDTH)

    def draw(self):
        pygame.draw.circle(self.screen, WHITE, (int(self.x), int(self.y)), self.size)


# Snowfall class to manage the simulation
class Snowfall:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snowfall Simulation")
        self.clock = pygame.time.Clock()
        self.snowflakes = [Snowflake(self.screen) for _ in range(SNOW_NUM)]

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(BLACK)  # Clear the screen before drawing

            for snowflake in self.snowflakes:
                snowflake.update()
                snowflake.draw()

            pygame.display.flip()

        pygame.quit()


# Entry point
if __name__ == "__main__":
    snowfall_simulation = Snowfall()
    snowfall_simulation.run()
