import pygame
from sys import exit

pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption('player_char')
clock=pygame.time.Clock()
test_font=pygame.font.Font(None,50)

sky_surface=pygame.image.load('graphics\\sky.png').convert()
ground_surface=pygame.image.load('graphics\\ground.png').convert()

text_surface=test_font.render('my game',False,'Green')
text_rect=text_surface.get_rect(center=(400,50))

snail_surface=pygame.image.load('graphics\\snail1.png').convert_alpha()
snail_xpos=600
snail_rect=snail_surface.get_rect(midbottom=(600,300))

player_surf=pygame.image.load('graphics\\player_walk_1.png').convert_alpha()
x=80
y=300
player_rect=player_surf.get_rect(midbottom=(x,y))
player_gravity=0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        # any button was pressed
        # work with specific key
        # if event.type()==pygame.KEYDOWN:
        #     if event.key==pygame.K_SPACE:
        #         pass
        # if event.type()==pygame.KEYUP:
        #     pass
        if event.type==pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom>=300:
                player_gravity=-20
                
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and player_rect.bottom>=300:
                player_gravity=-20
 
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    # pygame.draw.line(screen,'Pink',(0,0),(800,400))
    pygame.draw.rect(screen,'Pink',text_rect)
    pygame.draw.rect(screen,'Pink',text_rect,10)
    
    screen.blit(text_surface,(text_rect))

    snail_rect.left-=4
    if snail_rect.right<=0:snail_rect.left=800
    screen.blit(snail_surface,snail_rect)
    
    player_gravity+=1
    player_rect.y+=player_gravity
    if player_rect.bottom>=300:
        player_rect.bottom=300
    screen.blit(player_surf,player_rect)

    # keys=pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     pass
    if snail_rect.colliderect(player_rect):
        pygame.quit()
        exit()
        
    pygame.display.update()
    clock.tick(60)

""" 
player charater:
keyboard input
-pygame.key
-event loop

jump+gravity
-gravity:expo fxn 
-gravit+=value
-player.y+=gravity

creating a floor
-check coll b/w player and floor>move player up if coll
-all we really neeed is to check the y pos of player player.bottom>300:player.bottom=300
"""