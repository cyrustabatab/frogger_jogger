import pygame,sys
from player import Player
from settings import *




WINDOW = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Frogger')


clock = pygame.time.Clock()



sprites = pygame.sprite.Group()


player = Player((10,10),sprites)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    

    
    dt  = clock.tick()/1000

    sprites.update(dt)


    WINDOW.fill('black')

    sprites.draw(WINDOW)
    pygame.display.update()
