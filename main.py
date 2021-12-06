import pygame, sys
from pygame.locals import *
WIDTH, HEIGHT = 500, 500
TITLE = "Happy Birthday Mom"
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y):
        self.speed = 2
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(x,y,32,32)
        self.color = (250,120,60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False 
    def draw(self,win):
        pygame.draw.rect(win, self.color, self.rect)
    
    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed
        if not self.x + self.velX > WIDTH or not self.x + self.velX < WIDTH:
            self.x += self.velX
        if not self.y + self.velY > HEIGHT or not self.y + self.velY < HEIGHT:
            self.y += self.velY
        
        self.rect = pygame.Rect(self.x,self.y, 32, 32)
Player = Player(WIDTH/2, HEIGHT/2)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_LEFT:
                Player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                Player.right_pressed = True
            if event.key == pygame.K_UP:
                Player.up_pressed = True
            if event.key == pygame.K_DOWN:
                Player.down_pressed = True
        if event.type == KEYUP:
            if event.key == pygame.K_LEFT:
                Player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                Player.right_pressed = False
            if event.key == pygame.K_UP:
                Player.up_pressed = False
            if event.key == pygame.K_DOWN:
                Player.down_pressed = False
    display.fill((12,24,36))
    Player.draw(display)
    
    Player.update()
    pygame.display.flip()

    clock.tick(60)

