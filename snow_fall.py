import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Beautiful Snowfall")

# Clock
clock = pygame.time.Clock()


class Snowflake:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)

        # Increase chance of larger size values (inside constructor)
        self.size_probabilities = [0.2, 0.5, 0.3]  # Probability for sizes 2, 3, 4
        self.size = random.choices([2, 3, 4], self.size_probabilities)[0]

        self.speed = random.uniform(0.5, 2.0)  # Adjust speed range
        self.wind = random.uniform(-1, 1)  # Wind effect (+/- 1 pixel)
        self.rotation = random.randint(0, 360)  # Initial rotation

    def fall(self):
        self.y += self.speed
        self.x += self.wind

        # Random chance for shrink and vanish (more likely further down)
        vanish_chance = min(1.0, (self.y - HEIGHT) / (HEIGHT * 2))
        if random.random() < vanish_chance:
            self.y = random.randint(-HEIGHT, 0)
            self.x = random.randint(0, WIDTH)
            self.size = random.choices([2, 3, 4], self.size_probabilities)[0]
            self.speed = random.uniform(0.5, 2.0)
            self.wind = random.uniform(-1, 1)
            self.rotation = random.randint(0, 360)

    def draw(self, screen):
        # Opacity based on depth and size (smaller = lower opacity)
        base_opacity = 255 - int((self.y / HEIGHT) * 150)
        opacity = abs(max(0, base_opacity - (self.size * 50)))
        if opacity > 255:
            opacity = 255

        # Draw rotated snowflake with adjusted opacity
        snowflake_surface = pygame.Surface((self.size * 4, self.size * 4), pygame.SRCALPHA)
        pygame.draw.circle(snowflake_surface, WHITE + (opacity,), (self.size * 2, self.size * 2), self.size * 2)
        rotated_surface = pygame.transform.rotate(snowflake_surface, self.rotation)

        # Get rect and scale/position based on depth
        scale = 2 - (self.y / HEIGHT)
        rotated_rect = rotated_surface.get_rect(center=(self.x, self.y))
        scaled_surface = pygame.transform.scale(rotated_surface,
                                                (int(self.size * 4 * scale), int(self.size * 4 * scale)))
        screen.blit(scaled_surface, rotated_rect)


def main():
    snowflakes = [Snowflake() for _ in range(500)]  # Increased snowflake count

    running = True
    while running:
        clock.tick(FPS)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for snowflake in snowflakes:
            snowflake.fall()
            snowflake.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
