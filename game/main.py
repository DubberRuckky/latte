import pygame

pygame.init()

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("latte")

load = True

while load:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            load = False

pygame.quit()