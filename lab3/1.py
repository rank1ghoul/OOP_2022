import pygame
from pygame.draw import *
pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))

circle(screen, (255, 255, 0), (200, 175), 100)
circle(screen, (0, 0, 0), (200, 175), 100, 1)

circle(screen, (255, 0, 0), (150, 155), 20)
circle(screen, (255, 0, 0), (250, 155), 15)

circle(screen, (0, 0, 0), (150, 155), 8)
circle(screen, (0, 0, 0), (250, 155), 8)

polygon(screen, (0, 0, 0), ((105, 111), (110, 100), (175,135), (170, 142)))
line(screen, (0,0,0), (218, 140), (300, 126), 10)

rect(screen, (0, 0, 0), (150, 220, 100, 20))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
