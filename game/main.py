import pygame
import random as rand
from time import sleep

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

x = (screen_w - melon_w)//2
y = (screen_h - melon_h)//2

min_w_touch = 0 + melon_w
min_h_touch = 0 + melon_h

max_w_touch = screen_w - melon_w
max_h_touch = screen_h - melon_h

screen.fill((255, 255, 255))
icon_loading = pygame.transform.scale(icon, (100, 100))
screen.blit(icon_loading, icon_loading.get_rect(center=(screen_w // 2, screen_h // 2)))
pygame.display.flip()
sleep(5)

while load:

    x = rand.randint(min_w_touch, max_w_touch)
    y = rand.randint(min_h_touch, max_h_touch)
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            load = False

    screen.fill((0, 0, 0))
    screen.blit(melon , (x,y))
    pygame.display.flip()

    clock.tick(24)

pygame.quit()