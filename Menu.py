import pygame

janela = pygame.display.set_mode([800, 600])

pygame.display.set_caption('StarrPark')

imagem_fundo = pygame.image.load('imagens/fundo_colette.png')


loop = True

while loop:

    for events in pygame.event.get():
        
        if events.type == pygame.QUIT:
            loop = False

    janela.blit(imagem_fundo, (0, 0))

    pygame.display.update()



