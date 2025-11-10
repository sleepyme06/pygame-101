import pygame
from sys import exit

pygame.init()
width=800
height=400
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("game")
#change icon too
clock=pygame.time.Clock()

#screen loop
while True:
    #draw all elements
    #update everything

    #to check for user inputs
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
            
    pygame.display.update()
    clock.tick(60)

#clock telling while true loop not to run faster that 60fps or abt one while loop for 17 millisec
#max frame rate set

#.init()->initializes every thing like an car engine 
#but .quit()->uninisalizes


#framerate->60fps
#ceiling and floor for framerate to run consistenty irrespect of the kind of pc(weak/strong)
#ceiling: easy to tell comp to pause between frame
#floor: hard to get comp to run faster u need to change game so it runs well
#--->clock obejct  helps with time and  controlling frame rate