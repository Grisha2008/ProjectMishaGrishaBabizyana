import pygame

all_sprites = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
class wall(pygame.sprite.Sprite):
    image = pygame.transform.scale(pygame.image.load('Map/Set 1.png'), (200, 200))

    def __init__(self):
        super().__init__(all_sprites)
        self.add(wall_group)
        self.image = wall.image
        self.rect = self.image.get_rect()

walla = wall()
print(walla.rect)