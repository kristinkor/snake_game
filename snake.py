import pygame, sys, random
from pygame.math import Vector2


class Fruit:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x*cell_size),int(self.pos.y*cell_size),cell_size, cell_size)   
        #pygame.draw.rect(screen,((47,79,79)), fruit_rect) 
        screen.blit(orange, fruit_rect)

    def randomize(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x, self.y)   

      
class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
        #head
        self.head_up =pygame.image.load('sprites/head_up.png' ).convert_alpha()
        self.head_down =pygame. image.load('sprites/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('sprites/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('sprites/head_left.png').convert_alpha()
        #tail
        self.tail_up = pygame.image.load('sprites/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('sprites/tail_down.png' ).convert_alpha()
        self.tail_right = pygame.image.load('sprites/tail_right.png' ).convert_alpha()
        self.tail_left = pygame.image.load('sprites/tail_left.png').convert_alpha()
        #body
        self.body_bl = pygame.image.load('sprites/body_bl.png').convert_alpha()
        self.body_br = pygame.image.load('sprites/body_br.png' ).convert_alpha()
        self.body_tl = pygame.image.load('sprites/body_tl.png').convert_alpha()
        self.body_tr = pygame.image.load('sprites/body_tr.png' ).convert_alpha()
        self.body_horizontal = pygame.image.load('sprites/body_horizontal.png').convert_alpha()
        self.body_vertical = pygame.image.load('sprites/body_vertical.png').convert_alpha()

    def draw_snake(self):  
        self.update_head_graphics()
        self.update_tail_graphics()
        for index, block in enumerate(self.body):
            x_pos = int(block.x* cell_size)
            y_pos = int(block.y*cell_size)
            snake_rect = pygame.Rect(x_pos, y_pos ,cell_size, cell_size) 
            if index == 0:
                screen.blit(self.head, snake_rect)
            elif index == len(self.body) - 1: 
                screen.blit(self.tail, snake_rect) 
            else:
                prev_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block 
                if prev_block.x == next_block.x: 
                    screen.blit(self.body_vertical, snake_rect)
                elif prev_block.y == next_block.y: 
                    screen.blit(self.body_horizontal, snake_rect)  
                else:
                    if prev_block.x == -1 and next_block.y == -1 or prev_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, snake_rect)
                    elif prev_block.x == -1 and next_block.y == 1 or prev_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, snake_rect)
                    elif prev_block.x == 1 and next_block.y == -1 or prev_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, snake_rect)
                    elif prev_block.x == 1 and next_block.y == 1 or prev_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, snake_rect)                        
            #else:
                #pygame.draw.rect(screen,((224,255,255)), snake_rect) 


    def update_head_graphics(self):
        head_pos = self.body[1] - self.body[0]
        if(head_pos == Vector2(1,0)): self.head = self.head_left
        if(head_pos == Vector2(-1,0)): self.head = self.head_right
        if(head_pos == Vector2(0,1)): self.head = self.head_up
        if(head_pos == Vector2(0,-1)): self.head = self.head_down

    def update_tail_graphics(self):
        tail_pos = self.body[-2] - self.body[-1]
        if(tail_pos == Vector2(1,0)): self.tail = self.tail_left
        if(tail_pos == Vector2(-1,0)): self.tail = self.tail_right
        if(tail_pos == Vector2(0,1)): self.tail = self.tail_up
        if(tail_pos == Vector2(0,-1)): self.tail = self.tail_down

        # for block in self.body:
        #     x_pos = int(block.x* cell_size)
        #     y_pos = int(block.y*cell_size)
        #     snake_rect = pygame.Rect(x_pos, y_pos ,cell_size, cell_size)   
        #     pygame.draw.rect(screen,((224,255,255)), snake_rect) 

    def move_snake(self):
        if self.new_block == True:
            body_copy= self.body[:]   
            body_copy.insert(0, body_copy[0] + self.direction) 
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy= self.body[:-1]   
            body_copy.insert(0, body_copy[0] + self.direction) 
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True
    

    
class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self .snake.body[0]:
                self.game_over()   
   
    def game_over(self):
        pygame.quit()
        sys.exit()        

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
clock = pygame.time.Clock()
orange = pygame.image.load('orange.png').convert_alpha()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE: 
            main_game.update()   
        if event.type == pygame.KEYDOWN: 
            if event.key== pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key== pygame.K_RIGHT:
                if main_game.snake.direction.x !=- 1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key== pygame.K_DOWN:
                if main_game.snake.direction.y != - 1:  
                    main_game.snake.direction = Vector2(0,1)
            if event.key== pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
    screen.fill((255, 255, 255)) 
    main_game.draw_elements()
    #Here are gonna be our elements
    pygame.display.update()
    #the game runs at a consistent frame rate of 60 frames per second.
    clock.tick(60)