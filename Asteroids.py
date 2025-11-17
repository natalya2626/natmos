import pygame
import math
import random
from asteroid import Asteroid
from bullet import Bullet
from saucer import Saucer
from deadplayer import Deadplayer
from player import Player
from constants import (
    Color, Display, PLAYER_SIZE, PLAYER_MAX_SPEED,
    PLAYER_MAX_RTSPD, FD_FRIC, BD_FRIC, BULLET_SPEED,
    SAUCER_SPEED, SMALL_SAUCER_ACCURACY
)
from asteroid import AsteroidType
from saucer import SaucerType
from bullet import BulletType



# Загрузка звуков (глобально или в Game — ваш выбор)
snd_fire = pygame.mixer.Sound("Sounds/fire.wav")
snd_bangL = pygame.mixer.Sound("Sounds/bangLarge.wav")
snd_bangM = pygame.mixer.Sound("Sounds/bangMedium.wav")
snd_bangS = pygame.mixer.Sound("Sounds/bangSmall.wav")
snd_extra = pygame.mixer.Sound("Sounds/extra.wav")
snd_saucerB = pygame.mixer.Sound("Sounds/saucerBig.wav")
snd_saucerS = pygame.mixer.Sound("Sounds/saucerSmall.wav")


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.gameDisplay = pygame.display.set_mode((Display.width, Display.height))
        pygame.display.set_caption("Asteroids")
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_state = "Menu"  # "Menu", "Playing", "Game Over"
        self.reset_game()
        self.snd_saucerB = pygame.mixer.Sound("Sounds/saucerBig.wav")
        self.snd_saucerS = pygame.mixer.Sound("Sounds/saucerSmall.wav")


    def reset_game(self):
        """Сброс игры к начальному состоянию"""
        self.game_objects = []
        self.score = 0
        self.lives = 3
        self.stage = 1
        self.intensity = 0
        self.next_level_delay = 0
        self.player_invincible = 0
        self.hyperspace = 0
        self.bullet_capacity = 4
        self.one_up_multiplier = 1
        self.play_extra_sfx = 0

        # Создаём игрока
        self.player = Player(Display.width // 2, Display.height // 2, self)
        self.game_objects.append(self.player)

        # Создаём начальные астероиды
        self.spawn_asteroids(self.stage)

    def spawn_asteroids(self, count):
        for _ in range(count):
            # Генерируем позицию подальше от центра
            while True:
                x = random.randint(0, Display.width)
                y = random.randint(0, Display.height)
                dx = x - Display.width // 2
                dy = y - Display.height // 2
                if math.hypot(dx, dy) > 150:  # минимум 150 пикселей от центра
                    break
            asteroid = Asteroid(x, y, AsteroidType.LARGE, self)
            self.game_objects.append(asteroid)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if self.game_state == "Menu":
                    self.game_state = "Playing"
                    return

                if self.game_state == "Game Over":
                    if event.key == pygame.K_r:
                        self.reset_game()
                        self.game_state = "Playing"
                    return

                # Управление кораблём (только в игре)
                if self.game_state == "Playing":
                    if event.key == pygame.K_UP:
                        self.player.thrust = True
                    if event.key == pygame.K_LEFT:
                        self.player.rtspd = -PLAYER_MAX_RTSPD
                    if event.key == pygame.K_RIGHT:
                        self.player.rtspd = PLAYER_MAX_RTSPD
                    if event.key == pygame.K_SPACE:
                        self.try_shoot()
                    if event.key == pygame.K_LSHIFT:
                        self.activate_hyperspace()

            if event.type == pygame.KEYUP:
                if self.game_state == "Playing":
                    if event.key == pygame.K_UP:
                        self.player.thrust = False
                    if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                        self.player.rtspd = 0

    def try_shoot(self):
        # Подсчитываем текущие пули игрока
        player_bullets = sum(1 for obj in self.game_objects if isinstance(obj, Bullet))
        if self.player_invincible <= 0 and player_bullets < self.bullet_capacity:
            bullet = Bullet(self.player.x, self.player.y, self.player.dir, BulletType.NORMAL, self)
            self.game_objects.append(bullet)
            snd_fire.play()

    def activate_hyperspace(self):
        self.hyperspace = 30

    def update(self):
        if self.game_state != "Playing":
            return

        # Обновляем все объекты
        for obj in self.game_objects[:]:
            obj.update()

        # Обработка гиперпространства
        if self.hyperspace > 0:
            self.hyperspace -= 1
            if self.hyperspace == 1:
                self.player.x = random.randint(0, Display.width)
                self.player.y = random.randint(0, Display.height)
                self.player_invincible = 120

        # Уменьшаем неуязвимость
        if self.player_invincible > 0:
            self.player_invincible -= 1

        # Проверка столкновений (упрощённо)
        self.check_collisions()
        self.game_objects = [obj for obj in self.game_objects if getattr(obj, 'alive', True)]
        # Проверка конца уровня
        self.check_level_complete()

        # Обновление интенсивности
        if self.intensity < self.stage * 450:
            self.intensity += 1

        # Появление НЛО
        self.update_saucer()

        # Дополнительная жизнь
        if self.score > self.one_up_multiplier * 10000:
            self.lives += 1
            self.one_up_multiplier += 1
            self.play_extra_sfx = 60

        if self.play_extra_sfx > 0:
            self.play_extra_sfx -= 1

    def check_collisions(self):
        # Простая проверка: перебираем все пары
        n = len(self.game_objects)
        for i in range(n):
            for j in range(i + 1, n):
                obj1 = self.game_objects[i]
                obj2 = self.game_objects[j]
                if self.is_colliding_objects(obj1, obj2):
                    self.handle_collision(obj1, obj2)

    def is_colliding_objects(self, a, b):
        # Пример: если у объекта есть `x`, `y`, и `size`
        if hasattr(a, 'x') and hasattr(b, 'x'):
            dx = a.x - b.x
            dy = a.y - b.y
            distance = math.hypot(dx, dy)
            radius_a = getattr(a, 'size', 5)
            radius_b = getattr(b, 'size', 5)
            return distance < (radius_a + radius_b)
        return False

    def handle_collision(self, obj1, obj2):
        # Определяем типы объектов
        types = (type(obj1).__name__, type(obj2).__name__)
    
        # Столкновение: Player + Asteroid
        if (isinstance(obj1, Player) and isinstance(obj2, Asteroid)) or \
            (isinstance(obj1, Asteroid) and isinstance(obj2, Player)):
            player = obj1 if isinstance(obj1, Player) else obj2
            asteroid = obj2 if isinstance(obj2, Asteroid) else obj1
        
            if self.player_invincible <= 0:
                self.kill_player()
                self.split_asteroid(asteroid)
                self.play_asteroid_sound(asteroid)
    
        # Столкновение: Player + Saucer
        elif (isinstance(obj1, Player) and isinstance(obj2, Saucer)) or \
            (isinstance(obj1, Saucer) and isinstance(obj2, Player)):
            player = obj1 if isinstance(obj1, Player) else obj2
            saucer = obj2 if isinstance(obj2, Saucer) else obj1
        
            if self.player_invincible <= 0:
                self.kill_player()
                self.destroy_saucer(saucer)
                snd_bangL.play()
    
        # Столкновение: Bullet + Asteroid
        elif (isinstance(obj1, Bullet) and isinstance(obj2, Asteroid)) or \
            (isinstance(obj1, Asteroid) and isinstance(obj2, Bullet)):
            bullet = obj1 if isinstance(obj1, Bullet) else obj2
            asteroid = obj2 if isinstance(obj2, Asteroid) else obj1
        
        # Удаляем пулю
            bullet.alive = False
        # Дробим астероид
            self.split_asteroid(asteroid)
            self.update_score(asteroid)
            self.play_asteroid_sound(asteroid)
    
        # Столкновение: Bullet + Saucer
        elif (isinstance(obj1, Bullet) and isinstance(obj2, Saucer)) or \
            (isinstance(obj1, Saucer) and isinstance(obj2, Bullet)):
            bullet = obj1 if isinstance(obj1, Bullet) else obj2
            saucer = obj2 if isinstance(obj2, Saucer) else obj1
        
            bullet.alive = False
            self.destroy_saucer(saucer)
            self.score += 200 if saucer.type == SaucerType.LARGE else 1000
            snd_bangL.play()
    
        # Столкновение: Saucer + Asteroid
        elif (isinstance(obj1, Saucer) and isinstance(obj2, Asteroid)) or \
            (isinstance(obj1, Asteroid) and isinstance(obj2, Saucer)):
            saucer = obj1 if isinstance(obj1, Saucer) else obj2
            asteroid = obj2 if isinstance(obj2, Asteroid) else obj1
        
            self.destroy_saucer(saucer)
            self.split_asteroid(asteroid)
            self.play_asteroid_sound(asteroid)

     # Добавляем вспомогательные методы 
     #       
    def kill_player(self):
        """Убивает игрока и создаёт обломки"""
        if self.lives <= 0:
            self.game_state = "Game Over"
            return
    
        self.lives -= 1
        self.player_invincible = 120
    
        # Создаём обломки
        for _ in range(3):
            length = PLAYER_SIZE if _ == 2 else (5 * PLAYER_SIZE / (2 * math.cos(math.atan(1/3))))
            piece = Deadplayer(self.player.x, self.player.y, length, self)
            self.game_objects.append(piece)
    
        # Сбрасываем позицию игрока
        self.player.x = Display.width // 2
        self.player.y = Display.height // 2
        self.player.hspeed = 0
        self.player.vspeed = 0
        self.player.dir = -90


    def split_asteroid(self, asteroid):
        """Дробит астероид на меньшие"""
        asteroid.alive = False
        if asteroid.type == AsteroidType.LARGE:
            for _ in range(2):
                self.game_objects.append(Asteroid(asteroid.x, asteroid.y, AsteroidType.NORMAL, self))
        elif asteroid.type == AsteroidType.NORMAL:
            for _ in range(2):
                self.game_objects.append(Asteroid(asteroid.x, asteroid.y, AsteroidType.SMALL, self))
        # SMALL — просто исчезает


    def update_score(self, asteroid):
        if asteroid.type == AsteroidType.LARGE:
            self.score += 20
        elif asteroid.type == AsteroidType.NORMAL:
            self.score += 50
        else:
            self.score += 100


    def play_asteroid_sound(self, asteroid):
        if asteroid.type == AsteroidType.LARGE:
            snd_bangL.play()
        elif asteroid.type == AsteroidType.NORMAL:
            snd_bangM.play()
        else:
            snd_bangS.play()


    def destroy_saucer(self, saucer):
        saucer.state = "Dead"
        saucer.alive = False  





    def check_level_complete(self):
        # Считаем астероиды
        asteroids = [obj for obj in self.game_objects if isinstance(obj, Asteroid)]
        saucers = [obj for obj in self.game_objects if isinstance(obj, Saucer) and obj.state != "Dead"]
        if not asteroids and not saucers:
            if self.next_level_delay < 30:
                self.next_level_delay += 1
            else:
                self.stage += 1
                self.next_level_delay = 0
                self.spawn_asteroids(self.stage)

    def update_saucer(self):
        # Проверяем, есть ли живой Saucer
        saucers = [obj for obj in self.game_objects if isinstance(obj, Saucer) and obj.state != "Dead"]
        if not saucers:
            if self.next_level_delay == 0 and random.randint(0, 6000) <= (self.intensity * 2) / (self.stage * 9):
                # Создаём НЛО
                x = 0 if random.choice([True, False]) else Display.width
                y = random.randint(0, Display.height)
                saucer_type = SaucerType.SMALL if self.score >= 40000 else SaucerType.LARGE
                saucer = Saucer(x, y, "Alive", 0, 20 if saucer_type == SaucerType.LARGE else 10, saucer_type, self)
                self.game_objects.append(saucer)

    def draw(self):
        self.gameDisplay.fill(Color.black)

        if self.game_state == "Menu":
            self.draw_text("ASTEROIDS", Display.width // 2, Display.height // 2, 100)
            self.draw_text("Press any key to START", Display.width // 2, Display.height // 2 + 100, 50)
        elif self.game_state == "Game Over":
            self.draw_text("Game Over", Display.width // 2, Display.height // 2, 100)
            self.draw_text("Press 'R' to restart!", Display.width // 2, Display.height // 2 + 100, 50)
        else:
            # Отрисовка всех игровых объектов
            for obj in self.game_objects:
                # Мигание при неуязвимости
                if isinstance(obj, Player) and self.player_invincible > 0 and self.player_invincible % 6 < 3:
                    continue  # пропускаем отрисовку для мигания
                obj.draw()

            # Отрисовка HUD
            self.draw_text(str(self.score), 60, 20, 40)
            # Жизни
            for i in range(self.lives):
                live_player = Player(75 + i * 25, 75, self)
                live_player.draw()

        pygame.display.flip()

    def draw_text(self, text, x, y, size, center=True):
        font = pygame.font.SysFont(None, size)
        img = font.render(text, True, Color.white)
        if center:
            rect = img.get_rect(center=(x, y))
            self.gameDisplay.blit(img, rect)
        else:
            self.gameDisplay.blit(img, (x, y))

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()