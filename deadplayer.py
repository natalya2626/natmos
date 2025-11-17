from enum import Enum
import random
import math
from typing import TYPE_CHECKING
import pygame

from constants import Color, Display
from game_object import GameObject

if TYPE_CHECKING:
    from Asteroids import Game
    


# Create class for shattered ship
class Deadplayer(GameObject):
    ''' разрушенный корабль   '''

    def __init__(self, x: int, y: int, length: int, game: Game):
        self.angle = random.randrange(0, 360) * math.pi / 180
        self.dir = random.randrange(0, 360) * math.pi / 180
        self.rtspd = random.uniform(-0.25, 0.25)
        self.x = x
        self.y = y
        self.length = length
        self.speed = random.randint(2, 8)
        self.life = 60  # живёт 60 кадров (~1 секунда при 60 FPS)
        self.game = game


    def update(self):
        self.angle += self.rtspd
        self.x += self.speed * math.cos(self.dir)
        self.y += self.speed * math.sin(self.dir)
        self.life -= 1





        

    def draw(self): 
        if self.life > 0:
            pygame.draw.line(
                self.game.gameDisplay,
                Color.white,
                (self.x + self.length * math.cos(self.angle) / 2,
                self.y + self.length * math.sin(self.angle) / 2),
                (self.x - self.length * math.cos(self.angle) / 2,
                self.y - self.length * math.sin(self.angle) / 2))
        
        
        