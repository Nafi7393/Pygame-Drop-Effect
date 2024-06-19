import pygame
import random

# Starting The pygame & Some common Variables
pygame.init()
game_run = True
fps = 60
clock = pygame.time.Clock()
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
snow_size = 3
snow_num = 200

# Main Window
screen_width = 500
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snow Animation")


# Snow list
snow_list = []


# Making Snow
for snow in range(snow_num):
    x = random.randint(0, screen_width)
    y = random.randint(-screen_height, screen_height)
    snow_list.append([x, y])


# Here is the Main Function
def main_function():
    for i in range(len(snow_list)):
        pygame.draw.circle(screen, WHITE, snow_list[i], snow_size)
        snow_list[i][1] += 3 # random.randint(1, 2)
        # snow_list[i][0] += 3 # random.randint(-3, 3)

        if snow_list[i][1] > 610:
            y = random.randint(-50, -10)
            x = random.randint(0, 600)

            snow_list[i][1] = y
            snow_list[i][0] = x


# Main Loop
while game_run:
    pygame.display.flip()
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False

    clock.tick(fps)
    main_function()

pygame.quit()
