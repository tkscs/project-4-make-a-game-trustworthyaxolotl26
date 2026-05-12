import pygame, sys
from pygame.locals import *
import random, time

pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
NAVY = (0, 0, 70)

# Screen information
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
#score = coins

#background
start = pygame.image.load("start.png")
background = pygame.image.load("floor.png")
finish = pygame.image.load("end.png")

#fonts or something idk
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

DISPLAYSURF = pygame.display.set_mode((1470,600))
DISPLAYSURF.fill(NAVY)
pygame.display.set_caption("Flip Game")

 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("wall_cropped.png")
        self.rect = self.image.get_rect()
        self.rect.center=(100,100) 
 
      def move(self):
        self.rect.move_ip(0, 0)
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            self.rect.update(
                self.rect.left,
                150,
                self.rect.width,
                self.rect.height
            )
        if pressed_keys[K_DOWN] or pressed_keys[K_s]:
            self.rect.update(
                self.rect.left,
                450,
                self.rect.width,
                self.rect.height
            )
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            self.rect.move_ip(-5, 0)   
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            self.rect.move_ip(5, 0)
    def set_position(self, x, y):
        self.rect.update(
            x,
            y,
            self.rect.width,
            self.rect.height
        )

P1 = Player()
E1 = Enemy()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
 
while True:     
    for event in pygame.event.get():
    #     if event.type == INC_SPEED:
    #           SPEED += 0.5             
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



    DISPLAYSURF.blit(background, (400,0))
    DISPLAYSURF.blit(start, (-150,10))
    DISPLAYSURF.blit(finish, (1000, -47))
    # scores = font_small.render(str(SCORE), True, BLACK)
    # DISPLAYSURF.blit(scores, (10,10))


    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, (entity.rect))
        entity.move()

    # if P1<1000:
    #     P1.set_position(1000, 1000)

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        #   time.sleep(0.5)
          P1.set_position(300, 300)
           
        #   pygame.display.update()
        #   for entity in all_sprites:
        #         entity.kill() 
        #   time.sleep(2)
        #   pygame.quit()
        #   sys.exit()  
         
    pygame.display.update()
    FramePerSec.tick(FPS)

