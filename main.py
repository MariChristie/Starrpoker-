import pygame, sys
from button import Button

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("StarrPoker")

background = pygame.image.load("imagens/background.png").convert()
bg_rect = background.get_rect(center=(800 // 2, 600 // 2))

start_button = Button("imagens/start_button.png", (300, 150), 0.65)
exit_button = Button("imagens/exit_button.png", (300, 280), 0.65)


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if start_button.is_pressed():
        print("Start Button pressed")

    if exit_button.is_pressed():
        pygame.quit()
        sys.exit()

    window.fill("black")
    window.blit(background, bg_rect)
    start_button.draw(window)
    exit_button.draw(window)

    pygame.display.flip()
    clock.tick(60)

!