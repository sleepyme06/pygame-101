import pygame
from sys import exit
from random import randint, choice

def display_score():
    current_time=int(pygame.time.get_ticks()/1000)-start_time
    score_surf=test_font.render(f'{current_time}',False,(64,64,64))
    score_rect=score_surf.get_rect(center=(400,50))
    # print(current_time)
    screen.blit(score_surf,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x-=5
            if obstacle_rect.bottom==300:
                screen.blit(snail_surface,obstacle_rect)
                pygame.draw.rect(screen, 'Red', obstacle_rect, 2)
            else:
                screen.blit(fly_surf,obstacle_rect)
                pygame.draw.rect(screen, 'Red', obstacle_rect, 2)

        obstacle_list=  [obstacle for obstacle in obstacle_list if obstacle.x>-100] 
        return obstacle_list
    else:return[]

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):return False
    return True

def player_animation():
    global player_surf,player_index
    #<300 in air
    if player_rect.bottom<300:
        player_surf=player_jump
    else:
        player_index+=0.1# chnage like in dion after a particular scroe inc this
        # print(player_index)
        if player_index>=len(player_walk):player_index=0
        player_surf=player_walk[int(player_index)]

pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption('diff_lev')
clock=pygame.time.Clock()
test_font=pygame.font.Font(None,50)

game_acive=False
start_time=0
score=0
obstacle_rect_list=[]
player_gravity=0

sky_surface=pygame.image.load('graphics\\sky.png').convert()
ground_surface=pygame.image.load('graphics\\ground.png').convert()

snail_1=pygame.image.load('graphics\\snail1.png').convert_alpha()
snail_2=pygame.image.load('graphics\\snail2.png').convert_alpha()
snail_frame=[snail_1,snail_2]
snail_index=0
snail_surface=snail_frame[snail_index]

fly_1=pygame.image.load('graphics\\Fly1.png').convert_alpha()
fly_2=pygame.image.load('graphics\\Fly2.png').convert_alpha()
fly_frame=[fly_1,fly_2]
fly_index=0
fly_surf=fly_frame[fly_index]

player_walk1=pygame.image.load('graphics\\player_walk_1.png').convert_alpha()
player_walk2=pygame.image.load('graphics\\player_walk_2.png').convert_alpha()
player_walk=[player_walk1,player_walk2]
player_index=0
player_jump=pygame.image.load('graphics\\jump.png').convert_alpha()
player_surf=player_walk[player_index]
player_rect=player_surf.get_rect(midbottom=(80,300))

player_stand=pygame.image.load('graphics\\player_stand.png').convert_alpha()
player_stand=pygame.transform.scale2x(player_stand)
player_stand_rect=player_stand.get_rect(center=(400,200))

title_s=test_font.render('game',False,'Pink')

game_message=test_font.render('press space',False,"Pink")
game_message_rect=game_message.get_rect(center=(400,350))

obstcale_timer=pygame.USEREVENT+1
pygame.time.set_timer(obstcale_timer,1500)

snail_ani_timer=pygame.USEREVENT+2
pygame.time.set_timer(snail_ani_timer,500)

fly_ani_timer=pygame.USEREVENT+3
pygame.time.set_timer(fly_ani_timer,200)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

        if game_acive:
            if event.type==pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom>=300:
                    player_gravity=-20
                        
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and player_rect.bottom>=300:
                    player_gravity=-20
        else:
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                game_acive=True
                # snail_rect.left=800
                start_time=int(pygame.time.get_ticks()/1000)

        if game_acive:
            if event.type==obstcale_timer:
                if randint(0,2):
                    obstacle_rect_list.append(snail_surface.get_rect(bottomright=(randint(900,1100),300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright=(randint(900,1100),210)))

            if event.type ==snail_ani_timer:
                if snail_index==0:snail_index=1
                else:snail_index=0
                snail_surface=snail_frame[snail_index]
            if event.type == fly_ani_timer:
                if fly_index==0:fly_index=1
                else:fly_index=0
                fly_surf=fly_frame[fly_index]
        
                              
    if game_acive:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        score=display_score()

        """     
            Why we always add gravity
            It’s about keeping physics consistent.
            You want one rule for vertical movement:
            "Everything falls unless the ground stops it."
            That way, you don’t have to write separate logic for “in air” vs “on ground.”
            The code naturally handles both situations smoothly

            if we write both code sep then remove 151-152
        """
        player_gravity+=1
        # print(player_gravity)
        player_rect.y+=player_gravity
        if player_rect.bottom>=300:
            player_rect.bottom=300
        player_animation()
        screen.blit(player_surf,player_rect)
        pygame.draw.rect(screen, 'Blue', player_rect, 2)
        obstacle_rect_list=obstacle_movement(obstacle_rect_list)

        # if snail_rect.colliderect(player_rect):
        #     # pygame.quit()
        #     # exit()
        #     game_acive=False
        game_acive=collisions(player_rect,obstacle_rect_list)
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom=(80,300)
        player_gravity=0
        score_mess=test_font.render(f'your score:{score}',False,'Pink')
        score_mess_rect=score_mess.get_rect(center=(400,350))
        screen.blit(title_s,(350,300))
        if score==0:
            screen.blit(game_message,game_message_rect)
        else:
            screen.blit(score_mess,score_mess_rect)

    pygame.display.update()
    clock.tick(60)

""" 
game    game over
state mngmt in game
if game_active:
 current game
else:
 game over

 display score
 -update score every frame
 -put that on surface
 -display that surface
 pygame.time.get_ticks()->time in millisec

 display scroe in game over screen
 -we store in fxn score
 -current time need sto be global

 timers:creat ea custom event that is triggered in certain time intervals
 -create custom event
 -tell pygame to trigger that event cont
 -add code in event loop

 -we create a list of obstacles
 -everytime the timer triggers we add a new rect to list
 -we move every rect to left on every frame
 -we del rect too far left

 coll donot work
 we dont del the rect that leaves screen
 only one enemy

 animate player ,obstacles

 playe->our own timer that updates surface
 obstacle->rely on inbuilt timers to updtae surfaces

"""