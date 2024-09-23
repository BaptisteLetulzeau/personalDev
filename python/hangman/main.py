import pygame
import sys
import os

pygame.init()

screen = pygame.display.set_mode((600, 600))

# screen.fill((255, 255, 255))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        # quit bouton
        if event.type == pygame.QUIT:
            running = False

        # img = pygame.image.load(os.path.join('hangman/img', 'img.png'))
        # screen.blit(img, (0,0))
        
        # if the key is touched
        if event.type == pygame.KEYDOWN:
            print(f"touched key: {pygame.key.name(event.key)}")
            
            if event.key == pygame.K_ESCAPE:
                running = False
    
    pygame.display.update()

pygame.quit()
sys.exit()

