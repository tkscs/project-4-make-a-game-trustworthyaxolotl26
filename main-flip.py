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

# #fonts or something idk
# font = pygame.font.SysFont("Verdana", 60)
# font_small = pygame.font.SysFont("Verdana", 20)
# game_over = font.render("You win!", True, BLACK)

DISPLAYSURF = pygame.display.set_mode((1470,600))
DISPLAYSURF.fill(NAVY)
played = 1
pygame.display.set_caption(f"Flip Game - Level {played}")

button = pygame.image.load("button.png")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("wall_cropped.png")
        self.rect = self.image.get_rect()
        self.rect.center=(100,100) 
 
    def move(self):
        self.rect.move_ip(0, 0)

    def set_position(self, x, y):
        self.rect.update(
            x,
            y,
            self.rect.width,
            self.rect.height)
    
    def switch(self):
        while True:
            self.set_position(300, 420)
            time.sleep(0.1)
            self.set_position(300, 140)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP] or pressed_keys[K_w]:
                if self.rect.x <= 400:
                    self.rect.update(426, 150, 
                                 self.rect.width, 
                                 self.rect.height)
                else:
                    self.rect.update(self.rect.left, 150, 
                                     self.rect.width, self.rect.height)
        if pressed_keys[K_DOWN] or pressed_keys[K_s]:
            if self.rect.x <= 400:
                    self.rect.update(426, 450, 
                                 self.rect.width, 
                                 self.rect.height)
            else:
                self.rect.update(self.rect.left, 450,
                                self.rect.width, self.rect.height)
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            if self.rect.x >=426 and self.rect.y != 300:
                self.rect.move_ip(-4, 0)   
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            if self.rect.x >=426 and self.rect.y != 300:
                self.rect.move_ip(4, 0)

    def set_position(self, x, y):
        self.rect.update(
            x,
            y,
            self.rect.width,
            self.rect.height
        )

P1 = Player()
E1 = Enemy()
E2 = Enemy()
E3 = Enemy()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1, E2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1, E2)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

e1x = 1
e2x = 1

def playable():
    global e1x
    global e2x
    if abs(e1x - e2x) <=126:
        e2x = random.randint(415, 1000)
        playable()

def level():
    global e1x
    global e2x
    e1x = random.randint(415, 1000)
    e2x = random.randint(415, 1000)
    playable()
    E1.set_position(e1x, 420)
    E2.set_position(e2x, 140)

level()
P1.set_position(100,300)

while True:     
    for event in pygame.event.get():
    #     if event.type == INC_SPEED:
    #           SPEED += 0.5             
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(start, (-120,10))
    DISPLAYSURF.blit(finish, (960, 0))
    DISPLAYSURF.blit(background, (420,0))
    # scores = font_small.render(str(SCORE), True, BLACK)
    # DISPLAYSURF.blit(scores, (10,10))

###########OH AND MAYBE THERE IS A WALL THINGY THAT FLIPS BACK ANF FORTHS!! LIKE< IT PILSES AN THE N SWITHCHES@!! KINDA LIKE THW T)ONE STRIPPE LED GSAME THING IN THE ECPLORITORIAM!!!!!!

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, (entity.rect))
        entity.move()

    if P1.rect.x > 330 and P1.rect.y == 300:
        P1.set_position(330, 300) 
    if P1.rect.x < 26 and P1.rect.y == 300:
        P1.set_position(26, 300) 

    if P1.rect.x > 1000:
        P1.set_position(1111, 300)
        # P1.set_position(1121, 300)
        # time.sleep(0.5)
        # P1.set_position(1131, 300)
        # P1.set_position(1141, 300)
        level()
        played += 1
        pygame.display.set_caption(f"Flip Game - Level {played}")
        #show button 
        # pygame.quit()
        # sys.exit() 

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          P1.set_position(300, 300)
           
    pygame.display.update()
    FramePerSec.tick(FPS)
