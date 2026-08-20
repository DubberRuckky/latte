import pygame

pygame.init()

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("latte")

icon = pygame.image.load(r"game\assets\Icon.png")
pygame.display.set_icon(icon)

melon = pygame.image.load(r"game\assets\divexfre-red-fruit-9741345_640.png").convert_alpha()
melon = pygame.transform.scale(melon , (50,50))

load = True

clock = pygame.time.Clock()

x = 0

while load:

    screen.blit(melon , (x,30))
    x+=1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            load = False

    pygame.display.flip()

    clock.tick(24)

pygame.quit()