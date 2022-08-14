import random
import pygame

pygame.init()

win = pygame.display.set_mode((600, 600))

pygame.display.set_caption("Serpensky triangle")

Triangle = [[400, 50], [100, 550], [500, 550]]

x, y = random.randint(0, 600), random.randint(0, 600)

RUN = True
while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    A = random.randint(0, 2)
    x, y = .5 * (x + Triangle[A][0]), .5 * (y + Triangle[A][1])

    pygame.draw.line(win, (255, 255, 255), (x, y), (x, y), 1)
    pygame.display.update()

pygame.QUIT





















