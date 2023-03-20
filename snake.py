import pygame, sys, random
from pygame.math import Vector2


class Fruit():
    def __init__(self):
        self.x = random.randint(0,cell_number-1)
        self.y = 0
        self.pos =pygame.math.Vector2(self.x, self.y)
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x*cell_size),int(self.pos.y*cell_size),cell_size, cell_size)   
        pygame.draw.rect(screen,((47,79,79)), fruit_rect) 
      
class Snake():
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
    def draw_snake(self):  
        for block in self.body:
            x_pos = int(block.x* cell_size)
            y_pos = int(block.y*cell_size)
            snake_rect = pygame.Rect(x_pos, y_pos ,cell_size, cell_size)   
            pygame.draw.rect(screen,((224,255,255)), snake_rect) 
    def move_snake(self):
          body_copy= self.body[:-1]   
          body_copy.insert(0, body_copy[0] + self.direction) 
          self.body = body.copy[:]

class Main():
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
    def update(self):
        self.snake.move_snake()
        self.check_collision()
    def draw_elements(self):
        self.snake = draw_snake()
        self.fruit = draw_fruit()
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            print("hi")

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size,500))
clock = pygame.time.Clock()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #ends any run code
            sys.exit()
        if event.type == pygame.SCREEN_UPDATE: 
            main_game.update()   
        if event.type == pygame.KEYDOWN: 
            if event.key== pygame.K_UP:
                main_game.snake.direction = Vector(0,-1)
            if event.key== pygame.K_RIGHT:
                main_game.snake.direction = Vector(0,-1)
            if event.key== pygame.K_DOWN:
                main_game.snake.direction = Vector(0,-1)
            if event.key== pygame.K_LEFT:
                main_game.snake.direction = Vector(0,-1)
    screen.fill((75, 0, 130, .5)) 
    main_game.draw_elements()
    #Here are gonna be our elements
    pygame.display.update()
    #the game runs at a consistent frame rate of 60 frames per second.
    clock.tick(60)