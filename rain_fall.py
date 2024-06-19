import pygame, random

pygame.init()

# Common variables
run = True
FPS = 60
clock = pygame.time.Clock()
WIDTH = 500
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
all_rains = []


# Main Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Making Rain fall
for rain in range(200):
    x_pos = random.randint(-5, WIDTH + 10)
    y_pos = random.randint(-5, HEIGHT - 10)
    rain_height = random.randint(1, 3)
    rain_width = random.randint(6, 16)
    all_rains.append([x_pos, y_pos, rain_height, rain_width])


def rain_drop():
    for i in range(len(all_rains)):
        pygame.draw.rect(screen, WHITE, all_rains[i])

        all_rains[i][1] += 5

        if all_rains[i][1] >= 600:
            x = random.randint(-5, WIDTH + 5)
            y = random.randint(-5, -2)

            all_rains[i][0] = x
            all_rains[i][1] = y


while run:
    clock.tick(FPS)
    pygame.display.flip()
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    rain_drop()
    pygame.display.update()

pygame.quit()
