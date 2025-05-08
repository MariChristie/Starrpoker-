import pygame

class button:
    def _init_(self, image_path):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get.rect()

        def draw(self, window):
            window.blit(self.image, self.rect)
            