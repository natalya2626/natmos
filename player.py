from enum import Enum
import random
import math
from typing import TYPE_CHECKING
import pygame
from constants import Color, Display, PLAYER_SIZE, PLAYER_MAX_SPEED, FD_FRIC, BD_FRIC
from game_object import GameObject

if TYPE_CHECKING:
    from Asteroids import Game

class PlayerType(Enum):
    NORMAL = 'Normal'



#Class player    класс игрок
class Player(GameObject):
    def __init__(self, x: int, y: int, game: Game, hspeed: int = 0, vspeed: int = 0, rtspd: int = 0, dir: int = -90):
        self.x = x
        self.y = y
        self.hspeed = hspeed
        self.vspeed = vspeed
        self.dir = dir
        self.rtspd = rtspd
        self.thrust = False
        self.game = game
        self.alive = True

    def update(self):
        # Move player
        speed = math.sqrt(self.hspeed**2 + self.vspeed**2)
        if self.thrust:
            if speed + FD_FRIC < PLAYER_MAX_SPEED:
                self.hspeed += FD_FRIC * math.cos(self.dir * math.pi / 180)
                self.vspeed += FD_FRIC * math.sin(self.dir * math.pi / 180)
            else:
                self.hspeed = PLAYER_MAX_SPEED * \
                    math.cos(self.dir * math.pi / 180)
                self.vspeed = PLAYER_MAX_SPEED * \
                    math.sin(self.dir * math.pi / 180)
        else:
            if speed - BD_FRIC > 0:
                move_angle = math.atan2(self.vspeed, self.hspeed)
                new_speed = max(0, speed - BD_FRIC)
                self.hspeed = new_speed * math.cos(move_angle)
                self.vspeed = new_speed * math.sin(move_angle)
                
            else:
                self.hspeed = 0
                self.vspeed = 0
        self.x += self.hspeed
        self.y += self.vspeed

        # Check for wrapping
        if self.x > Display.width:
            self.x = 0
        elif self.x < 0:
            self.x = Display.width
        elif self.y > Display.height:
            self.y = 0
        elif self.y < 0:
            self.y = Display.height

        # Rotate player
        self.dir += self.rtspd

    def draw(self):
        a = math.radians(self.dir)
        x = self.x
        y = self.y
        s = PLAYER_SIZE
        t = self.thrust
        # Draw player
        pygame.draw.line(self.game.gameDisplay,
            Color.white,
            (x - (s * math.sqrt(130) / 12) * math.cos(math.atan(7 / 9) + a),
             y - (s * math.sqrt(130) / 12) * math.sin(math.atan(7 / 9) + a)),
            (x + s * math.cos(a), y + s * math.sin(a)))

        pygame.draw.line(self.game.gameDisplay,
            Color.white,
            (x - (s * math.sqrt(130) / 12) * math.cos(math.atan(7 / 9) - a),
             y + (s * math.sqrt(130) / 12) * math.sin(math.atan(7 / 9) - a)),
            (x + s * math.cos(a), y + s * math.sin(a)))

        pygame.draw.line(self.game.gameDisplay,
            Color.white,
            (x - (s * math.sqrt(2) / 2) * math.cos(a + math.pi / 4),
             y - (s * math.sqrt(2) / 2) * math.sin(a + math.pi / 4)),
            (x - (s * math.sqrt(2) / 2) * math.cos(-a + math.pi / 4),
             y + (s * math.sqrt(2) / 2) * math.sin(-a + math.pi / 4)))
        if t:
            pygame.draw.line(self.game.gameDisplay,
                Color.white,
                (x - s * math.cos(a),
                 y - s * math.sin(a)),
                (x - (s * math.sqrt(5) / 4) * math.cos(a + math.pi / 6),
                 y - (s * math.sqrt(5) / 4) * math.sin(a + math.pi / 6)))
            pygame.draw.line(self.game.gameDisplay,
                Color.white,
                (x - s * math.cos(-a),
                 y + s * math.sin(-a)),
                (x - (s * math.sqrt(5) / 4) * math.cos(-a + math.pi / 6),
                 y + (s * math.sqrt(5) / 4) * math.sin(-a + math.pi / 6)))

    def killPlayer(self):
        # Reset the player
        self.x = Display.width / 2
        self.y = Display.height / 2
        self.thrust = False
        self.dir = -90
        self.hspeed = 0
        self.vspeed = 0
