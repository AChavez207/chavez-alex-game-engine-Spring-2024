#This file was created by: Alex Chavez
#my first source control edit
# import necessary modules

# Player Levels, Weapons, Gain currency from enemies

import pygame as pg
import sys
from settings import *
from sprites import *
from random import randint 
from os import path
from time import sleep

def draw_health_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 32
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    pg.draw.rect(surf, GREEN, fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect, 2)
#Game Class
class Game:
    #initializing attributes
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()
    #load save game data etc.
    def load_data(self):
       game_folder = path.dirname(__file__)
       self.map_data = []
       with open(path.join(game_folder, 'map.txt'), 'rt')as f:
           for line in f:
                print(line)
                self.map_data.append(line)


    def new(self):
        # self.cooldown = Timer(self)
        # init all variables
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.power_ups = pg.sprite.Group()
        self.food = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        # self.player = Player(self,10,10)
        # for x in range(10,20):
        #  Wall(self,x,5)
        #defined run method
        for row, tiles in enumerate(self.map_data):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
                if tile == '1':
                     Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'U':
                    PowerUp(self, col,row)
                if tile == 'F':
                    Coin(self, col, row)
                if tile == 'M':
                    Mob(self, col, row)
                if tile == 'm':
                    Mob2(self,col,row)

            
                

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
    def quit(self):
        pg.quit
        sys.exit

    def update(self):
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x,y)
        surface.blit(text_surface, text_rect)

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.draw_text(self.screen, "Coins" + str(self.player.moneybag), 24, WHITE, WIDTH/2 -32, 2)
        pg.display.flip()

    def collide_with_mobs(self):
        hits = pg.sprite.spritecollide(self,self.game.mobs,False)
        if hits:
            self.hitpoints -=1
        if self.hitpoints <= 0:
            print("player has died")
            self.kill()
    
    def draw(self):
            self.screen.fill(BGCOLOR)
            # self.draw_grid()
            self.all_sprites.draw(self.screen)
            # self.player.draw_health_bar(self.screen, self.player.rect.x, self.player.rect.y, self.player.hitpoints)
            draw_health_bar(self.screen, self.player.rect.x, self.player.rect.y-8, self.player.hitpoints)
            pg.display.flip()
      #input method
    def events(self):
         for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()


            #     if event.key == pg.K_LEFT:
            #             self.player.move(dx=-1)
            #     if event.key == pg.K_RIGHT:
            #             self.player.move(dx=1)
            #     if event.key == pg.K_UP:
            #             self.player.move(dy=-1)
            #     if event.key == pg.K_DOWN:
            #         self.player.move(dy=1)
            
    def show_start_screen(self):
        self.screen.fill(LIGHTBLUE)
        self.draw_text(self.screen, "Press any button to begin.", 27, WHITE, WIDTH/2, HEIGHT/2)
        pg.display.flip()
        self.wait_for_key()


    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pg.KEYUP:
                    waiting = False
               
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen

    


        