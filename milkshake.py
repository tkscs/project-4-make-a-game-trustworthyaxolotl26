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
WHITE = (255, 255, 255)

# Screen information
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
#score = coins

#background
background = pygame.image.load("Background.png")

#fonts or something idk
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

DISPLAYSURF = pygame.display.set_mode((600,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
 
# class Enemy(pygame.sprite.Sprite):
#       def __init__(self):
#         super().__init__() 
#         self.image = pygame.image.load("Enemy.png")
#         self.rect = self.image.get_rect()
#         self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 
 
#       def move(self):
#         global SCORE
#         self.rect.move_ip(0,SPEED)
#         if (self.rect.top > 600):
#             SCORE += 1
#             self.rect.top = 0
#             self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.height != SCREEN_HEIGHT:
            if pressed_keys[K_UP] or pressed_keys[K_w]:
                self.rect.move_ip(0, -5)
        if self.rect.height != SCREEN_HEIGHT:
            if pressed_keys[K_DOWN] or pressed_keys[K_s]:
                self.rect.move_ip(0,5)
        if self.rect.left > 0:
              if pressed_keys[K_LEFT] or pressed_keys[K_a]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
                  self.rect.move_ip(5, 0)

milkshakes = ["strawberry", "vanilla", "mixed"]
class Milkshake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.order = random.choice(milkshakes)
        self.image = pygame.image.load(f"{self.order}.png")
        self.rect = self.image.get_rect()
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE]:
            self.rect == Player.rect

P1 = Player()
# E1 = Enemy()
M1 = Milkshake()

##Creating Sprites Groups
# enemies = pygame.sprite.Group()
# enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(M1)
# all_sprites.add(E1)
foods = pygame.sprite.Group()
foods.add(M1)

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
     
    DISPLAYSURF.blit(background, (0,0))
    # scores = font_small.render(str(SCORE), True, BLACK)
    # DISPLAYSURF.blit(scores, (10,10))


    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    # #To be run if collision occurs between Player and Enemy
    # if pygame.sprite.spritecollideany(P1, enemies):
    #       time.sleep(0.5)
                    
    #       DISPLAYSURF.fill(RED)
    #       DISPLAYSURF.blit(game_over, (30,250))
    #       DISPLAYSURF.blit(scores, (200, 200))
           
    #       pygame.display.update()
    #       for entity in all_sprites:
    #             entity.kill() 
    #       time.sleep(2)
    #       pygame.quit()
    #       sys.exit()  
         
    pygame.display.update()
    FramePerSec.tick(FPS)

