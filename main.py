import pygame, sys
from button import Button

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("StarrPoker")

background = pygame.image.load("imagens/background.png").convert()

start_button = Button()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            sys.exit()

    window.fill("black")
    window.blit(background, (0, 0))
    start_button.draw(window)



    pygame.display.flip()
    clock.tick(60)
