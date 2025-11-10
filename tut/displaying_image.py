'''
surface
-dispaly:game window anything displayed goes on here (unique)
-regular:essntialy a single image need to be put on display surface to be visible

plain color
image
text->image of text->display on screen
create font;write text on surface;blit the text surface
'''
import pygame
from sys import exit

pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption('images')
clock=pygame.time.Clock()

# w=100
# h=200
# test_surface=pygame.Surface((w,h))
# test_surface.fill('Red')
#think of it like coordinate sys topleft 0,0( ->x++ down y++)
test_font=pygame.font.Font(None,50)
ground_surface=pygame.image.load('graphics\\ground.png')
sky_surface=pygame.image.load('graphics\\sky.png')
text_surface=test_font.render('my game',False,'Green')#text,anti alasiying,color

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    
    # screen.blit(test_surface,(0,0))
    # screen.blit(test_surface,(200,100))
    #specific method to place later
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    pygame.display.update()
    clock.tick(60)
