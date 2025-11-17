from enum import Enum
import random
import math
from typing import TYPE_CHECKING
import pygame

from constants import Color, Display
from game_object import GameObject

if TYPE_CHECKING:
    from Asteroids import Game

class BulletType(Enum):
    NORMAL = 'Normal'

BULLET_SPEED = 15

# Create class bullet
class Bullet(GameObject):
    '''is a bullet   представляет собой пулю'''


    def __init__(self, x: int, y: int, dir: int, type_: BulletType, game: Game ):
        self.x = x
        self.y = y 
        self.dir = dir
        self.life = 30
        self.type = type_
        self.game = game
        self.alive = True

    def update(self):
        
        self.x += BULLET_SPEED * math.cos(self.dir * math.pi / 180)
        self.y += BULLET_SPEED * math.sin(self.dir * math.pi / 180)
        
             
                      
        if self.x > Display.width:
            self.x = 0
        elif self.x < 0:
            self.x = Display.width
        elif self.y > Display.height:
            self.y = 0
        elif self.y < 0:
            self.y = Display.height
        self.life -= 1
        if self.life <= 0:
            self.alive = False


    def draw(self):   
        pygame.draw.circle(self.game.gameDisplay,
                            Color.white, (int(self.x), int(self.y)), 3)
        