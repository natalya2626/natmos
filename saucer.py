from enum import Enum
import random
import math
from typing import TYPE_CHECKING
import pygame

from constants import Color, Display
from game_object import GameObject
from bullet import BulletType


if TYPE_CHECKING:
    from Asteroids import Game


class SauserType(Enum):                   # блюдце  (сусэ)
    LARGE = 'Large'
    SMALL = 'Small'

SAUCER_SPEED = 5

# Create class saucer
class Saucer(GameObject):
    '''It is a saucer     представляет собой блюдце'''

    def __init__(self, x: int, y: int, state: str, size: int,type_: SaucerType, game: Game, 
                 bdir: int = 0):
        self.x = x
        self.y = y
        self.state = state                # состояние
        self.dirchoice = ()               # выбор направления
        self.bullets = []                 # список пуль
        self.cd = 0                       # shooting cooldown - перезарядка при стрельбе
        self.type = type_
        self.game = game
        self.size = size
        self.bdir = bdir                  # напрвление
        self.alive = True
        self.soundDelay = 0 
        
        if self.x == 0:
            self.dir = 0
            self.dirchoice = (0, 45, -45)
        else:
            self.dir = 180
            self.dirchoice = (180, 135, -135)
    
    def update(self):
        # Move player
        self.x += SAUCER_SPEED * math.cos(self.dir * math.pi / 180)
        self.y += SAUCER_SPEED * math.sin(self.dir * math.pi / 180)
        # Choose random direction
        if random.randrange(0, 100) == 1:
            self.dir = random.choice(self.dirchoice)

        # Wrapping
        if self.y < 0:
            self.y = Display.height
        elif self.y > Display.height:
            self.y = 0
        if self.x < 0 or self.x > Display.width:
            self.state = "Dead"

        # Shooting
        if self.type == SaucerType.LARGE:
            self.bdir = random.randint(0, 360)
        if self.cd == 0:
            self.game.game_objects.append(Bullet(self.x, self.y, self.bdir, BulletType.NORMAL, self.game))
            self.cd = 30
        else:
            self.cd -= 1

        if self.soundDelay <= 0:
            if self.type == SaucerType.LARGE:
                self.game.snd_saucerB.play()
            else:
                self.game.snd_saucerS.play()
            self.soundDelay = 30
        else:
            self.soundDelay -= 1


        # Play SFX
        # if self.type == "Large":
        #     pygame.mixer.Sound.play(snd_saucerB)
        # else:
        #     pygame.mixer.Sound.play(snd_saucerS)

    

    def draw(self):
        if self.state == "Dead":
            return
    
        # Draw saucer                               # нарисуйте блюдце
        pygame.draw.polygon(self.game.gameDisplay,
                             Color.white,
            ((self.x + self.size, self.y),
             (self.x + self.size / 2, self.y + self.size / 3),
             (self.x - self.size / 2, self.y + self.size / 3),
             (self.x - self.size, self.y),
             (self.x - self.size / 2, self.y - self.size / 3),
             (self.x + self.size / 2, self.y - self.size / 3)), 1)
        pygame.draw.line(self.game.gameDisplay,
                          Color.white,
            (self.x - self.size, self.y),
            (self.x + self.size, self.y))
        pygame.draw.polygon(self.game.gameDisplay,
                             Color.white,
            ((self.x - self.size / 2, self.y - self.size / 3),
             (self.x - self.size / 3, self.y - 2 * self.size / 3),
             (self.x + self.size / 3, self.y - 2 * self.size / 3),
             (self.x + self.size / 2, self.y - self.size / 3)), 1)

