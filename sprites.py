# This file was created by: Alex Chavez

#import modules
import pygame as pg 
from pygame.sprite import Sprite
from settings import *
from random import choice
from random import randint

vec =pg.math.Vector2
# def collide_with_player(self):
#         hits = pg.sprite.spritecollide(self,self.game.player,False)
#         if hits:
#             self.hitpoints -=1
#         if self.hitpoints <= 0:
#             print("Finished level")
#             self.kill()
# def collide_with_player(self):
#         hits = pg.sprite.spritecollide(self,self.game.player,False)
#         if hits:
#             PowerUp.hitpoint -=1
#         if PowerUp.Hitpoints <=0:
#             PLAYER_SPEED = 500
#             print("Im fast")
def collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False)
        if hits:
            if hits[0].rect.centerx > sprite.rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.rect.width / 2
            if hits[0].rect.centerx < sprite.rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.rect.width / 2
            sprite.vel.x = 0
            sprite.rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False)
        if hits:
            if hits[0].rect.centery > sprite.rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.rect.height / 2
            if hits[0].rect.centery < sprite.rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.rect.height / 2
            sprite.vel.y = 0
            sprite.rect.centery = sprite.pos.y
    
#create a player class
    
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 300
        # self.max_speed = 500
        self.hitpoints = 100
        self.weapon_drawn = False
        self.pos = vec(0,0)
        self.dir = vec(0,0)
        self.material = True
        self.weapon = ""
    def set_dir(self,d):
        self.dir = d
    def get_dir(self):
        return dir
        

        # def move (self, dx=0, dy=0):
        #     self.x += dx
        #     self.y += dy

    def get_keys(self):
        self.vx, self.vy = 0, 0 
        self.weapon_drawn = False
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -self.speed
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = self.speed  
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -self.speed  
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = self.speed
        if keys[pg.K_e]:
            pg.quit()
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    previous_position = list(player_position)
    player_has_moved = previous_position != player_position

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y


    def collide_with_powerup(self):
        hits = pg.sprite.spritecollide(self,self.game.power_ups,False)
        if hits:
            self.speed +=5



    def collide_with_mobs(self):
        hits = pg.sprite.spritecollide(self,self.game.mobs,False)
        if hits:
            self.hitpoints -=1
        if self.hitpoints <= 0:
            print("player has died")
            self.kill()
            pg.quit()


    # def collide_with_group(self, group, kill):
    #     hits = pg.sprite.spritecollide(self, group, kill)

    #     if hits:
    #         if str(hits[0].__class__.__name__) == "Coin":
    #             self.moneybag += 1

    #         if str(hits[0].__class__.__name__) == "PowerUp":
    #             print(hits[0].__class__.__name__)
    #             self.speed += 200
    #         if str(hits[0].__class__.__name__) == "Mob":
    #             self.hitpoints -= 1
    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')
        self.collide_with_mobs()
        self.collide_with_powerup()







class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

 
class PowerUp(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.power_ups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.hitpoints = 100
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE



class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(LIGHTGREY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.vx, self.vy = 100,100
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 250
        self.hitpoints = 10
    def collide_with_walls(self, dir):
        if dir == 'x':
            # print('colliding on the x')
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                self.vx *= -1
                self.rect.x = self.x
        if dir == 'y':
            # print('colliding on the y')
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                self.vy *= -1
                self.rect.y = self.y
    def update(self):
        if self.hitpoints < 1:
            self.kill()

        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        
        if self.rect.x < self.game.player.rect.x:
            self.vx = 150
        if self.rect.x > self.game.player.rect.x:
            self.vx = -150    
        if self.rect.y < self.game.player.rect.y:
            self.vy = 150
        if self.rect.y > self.game.player.rect.y:
            self.vy = -150
        self.rect.x = self.x
        # self.collide_with_walls('x')
        self.rect.y = self.y
        # self.collide_with_walls('y')

class Mob2(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        # add powerup groups later....
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(LIGHTGREY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.vx, self.vy = 100,100
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = randint(1,10)
        self.hitpoints = 4
    def collide_with_walls(self, dir):
        if dir == 'x':
            # print('colliding on the x')
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                self.vx *= -1
                self.rect.x = self.x
        if dir == 'y':
            # print('colliding on the y')
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                self.vy *= -1
                self.rect.y = self.y
    def update(self):
        if self.hitpoints < 1:
            self.kill

        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        
        if self.rect.x < self.game.player.rect.x:
            self.vx = 150
        if self.rect.x > self.game.player.rect.x:
            self.vx = -150    
        if self.rect.y < self.game.player.rect.y:
            self.vy = 150
        if self.rect.y > self.game.player.rect.y:
            self.vy = -150
        self.rect.x = self.x
        # self.collide_with_walls('x')
        self.rect.y = self.y
        # self.collide_with_walls('y')

class Mob3(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        # add powerup groups later....
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE*2, TILESIZE*2))
        self.image.fill(LIGHTGREY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.vx, self.vy = 100,100
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 1
        self.hitpoints = 100
    def collide_with_walls(self, dir):
        if dir == 'x':
            # print('colliding on the x')
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                self.vx *= -1
                self.rect.x = self.x
        if dir == 'y':
            # print('colliding on the y')
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                self.vy *= -1
                self.rect.y = self.y
    def update(self):
        if self.hitpoints < 1:
            self.kill

        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        
        if self.rect.x < self.game.player.rect.x:
            self.vx = 50
        if self.rect.x > self.game.player.rect.x:
            self.vx = -50    
        if self.rect.y < self.game.player.rect.y:
            self.vy = 50
        if self.rect.y > self.game.player.rect.y:
            self.vy = -50
        self.rect.x = self.x
        # self.collide_with_walls('x')
        self.rect.y = self.y
        # self.collide_with_walls('y')






