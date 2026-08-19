import pygame

pygame.init()

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("latte")

melon = pygame.image.load(r"game\images\divexfre-red-fruit-9741345_640.png").convert()

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

    clock.tick(60)

pygame.quit()