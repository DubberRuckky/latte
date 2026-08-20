import pygame
import random as rand

pygame.init()

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("latte")

icon = pygame.image.load(r"game\assets\Icon.png")
pygame.display.set_icon(icon)

melon = pygame.image.load(r"game\assets\divexfre-red-fruit-9741345_640.png").convert_alpha()
melon = pygame.transform.scale(melon , (100,100))

load = True

clock = pygame.time.Clock()


melon_w, melon_h = melon.get_size()
screen_w, screen_h = screen.get_size()

x = (screen_w + screen_h)/2
y = (screen_w + screen_h)/2

min_w_touch = 0
min_h_touch = 0

max_w_touch = screen_w - melon_w
max_h_touch = screen_h - melon_h

while load:

    x = rand.randint(min_w_touch, max_w_touch)
    y = rand.randint(min_h_touch, max_h_touch)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            load = False

    #screen.fill((0, 0, 0))
    screen.blit(melon , (x,y))
    pygame.display.flip()

    clock.tick(24)

pygame.quit()