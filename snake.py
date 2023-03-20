import pygame, sys

pygame.init()
screen = pygame.display.set_mode((500,500))
#create clock object
#control the frame rate of a Pygame game or application.
clock = pygame.time.Clock()
test_surface =  pygame.Surface((100,200))
test_surface.fill((127,255,212)) 

x_pos = 200


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #ends any run code
            sys.exit()

    screen.fill((75,0,130, .5)) 
    x_pos += 1       
    screen.blit(test_surface,(200,250))
    #Here are gonna be our elements
    pygame.display.update()
    #the game runs at a consistent frame rate of 60 frames per second.
    clock.tick(60)