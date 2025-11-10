import pygame
from sys import exit

pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption('animation')
clock=pygame.time.Clock()

test_font=pygame.font.Font(None,50)
ground_surface=pygame.image.load('graphics\\ground.png').convert()
sky_surface=pygame.image.load('graphics\\sky.png').convert()
text_surface=test_font.render('my game',False,'Green')#text,anti alasiying,color
snail_surface=pygame.image.load('graphics\\snail1.png').convert_alpha()
snail_xpos=600
player_surf=pygame.image.load('graphics\\player_walk_1.png').convert_alpha()
# player_rect=pygame.Rect(left,top,width,height)
x=80
y=300

player_rect=player_surf.get_rect(midbottom=(x,y))
snail_rect=snail_surface.get_rect(midbottom=(600,y))
text_rect=text_surface.get_rect(center=(400,50))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type==pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):print('collision')
    
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    pygame.draw.line(screen,'Pink',(0,0),(800,400  ))
    pygame.draw.rect(screen,'Pink',text_rect)
    pygame.draw.rect(screen,'Pink',text_rect,6)
    # screen.blit(text_surface,(300,50))
    screen.blit(text_surface,(text_rect))
    # snail_xpos-=4 #left
    # snail_xpos+=4
    # create an if statement that places the snail on right if it goes too far left
    # if snail_xpos<0:
    #     snail_xpos=400
    # screen.blit(snail_surface,(snail_xpos,250))
    snail_rect.left-=1
    if snail_rect.right<=0:snail_rect.left=800
    screen.blit(snail_surface,snail_rect)
    player_rect.left+=1
    screen.blit(player_surf,player_rect)

    # if player_rect.colliderect(snail_rect):
    #     pass
    # mouse_pos=pygame.mouse.get_pos()
    # if player_rect.collidepoint((mouse_pos)):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)


'''
rectangles->precise pos,basic coll det,draw
surface for image info->placement via rectangle-- sprite class
--tuple(x,y),individual values 
surface->lefttop rect any pt

colliderect
0 no coll
1 coll

collidpoint   mouse pos->pygame.mouse,event loop

animating each just means changing pos slightly on each frame
'''