# This file was created by: Alex Chavez

#import modules
import pygame as pg 
from pygame.sprite import Sprite
from settings import *
from random import choice

vec =pg.math.Vector2

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
        self.moneybag = 0
        self.speed = 300
        self.hitpoints = 100
        self.weapon_drawn = False
        

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
            self.weapon_drawn = True
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071
    def draw_weapon(self):
        if self.weapon_drawn:
            Sword(self.game, self.rect.x+TILESIZE, self.rect.y-TILESIZE)
                    

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
    def collide_with_group(self, group, kill):
        hits = pg.sprite.spritecollide(self, group, kill)
        if hits:
            if str(hits[0].__class__.__name__) == "Coin":
                self.moneybag += 1
            if str(hits[0].__class__.__name__) == "PowerUp":
                print(hits[0].__class__.__name__)
                self.speed += 300

            
    def update(self):
        self.get_keys()
        self.draw_weapon()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')

        self.collide_with_group(self.game.coins, True)
        # if self.game.cooldown.cd < 1:
        #     self.cooling = False
        # if not self.cooling:
        #     self.collide_with_group(self.game.power_ups, True)
        # self.collide_with_group(self.game.mobs, False)

class Sword(pg.sprite.Sprite):
    def __init_(self, game,x,y,w,h,dir):
        self.groups = game.all_sprites, game.weapons
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = pg.Surface((w,h))
        self.image.fill(LIGHTBLUE)
        self.rect = self.image.get_rect()
        self.dir = dir
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.pos = vec(x,y)

        self.speed = 10
    def collide_with_group(self,group,kill):
        hits = pg.sprite.spritecollide(self,group,kill)
        if hits:
            if str(hits[0].__class__.__name__) == "Mob":
                hits[0].hitpoints -= 1
            if str(hits[0].__class__.__name__) == "Mob2":
                hits[0].hitpoints -= 1
    def update(self):
        
        self.pos = self.game.player.pos

        self.collide_with_groups(self.game.mobs, False)
        if not self.game.player.weaopon_drawn:
            self.kill




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

class Coin(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.coins
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
        # add powerup groups later....
        self.groups = game.all_sprites, game.power_ups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Mob(pg.sprite.Sprite):
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
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.speed = 1
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
    # def update(self):
    #     self.rect.x += 1
    #     self.x += self.vx * self.game.dt
    #     self.y += self.vy * self.game.dt
        
    #     if self.rect.x < self.game.player.rect.x:
    #         self.vx = 100
    #     if self.rect.x > self.game.player.rect.x:
    #         self.vx = -100    
    #     if self.rect.y < self.game.player.rect.y:
    #         self.vy = 100
    #     if self.rect.y > self.game.player.rect.y:
    #         self.vy = -100
    #     self.rect.x = self.x
    #     self.collide_with_walls('x')
    #     self.rect.y = self.y
    #     self.collide_with_walls('y')




