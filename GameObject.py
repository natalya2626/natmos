from abc import ABC, abstractmethod


class GameObject(ABC):
    
    @abstractmethod
    def update(self, game):
        ...
        
    @abstractmethod
    def draw(self, game):
        ...
        
        
        
# game_object.py
class GameObject:
    def __init__(self):
        self.alive = True

    def destroy(self):
        self.alive = False