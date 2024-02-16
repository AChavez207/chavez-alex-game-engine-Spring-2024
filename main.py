#This file was created by: Alex Chavez

# import necessary modules
import pygame as pg
import sys
from settings import *
from sprites import *
from random import randint 
from os import path
from time import sleep

#Game Class
class Game:
    #initializing attributes
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500,100)
        self.load_data()
    #load save game data etc.
    def load_data(self):
       game_folder = path.dirname(__file__)
       self.map_data = []
       with open(path.join(game_folder, 'map.txt'), 'rt')as f:
           for line in f:
               self.map_data.append(line)
               print(self.map_data)
               # print(eneumerate(self.map_data))

    def new(self):
       # init all variables
       self.all_sprites = pg.sprite.Group()
       self.walls = pg.sprite.Group()
       self.power_ups = pg.sprite.Group()
       self.food = pg.sprite.Group()
       self.mobs = pg.sprtie.Group()
       # self.player = Player(self,10,10)
       # for x in range(10,20):
        #  Wall(self,x,5)
    #defined run method
    for row, tiles in enumerate(self.map_data):
        for col, tile in enumerate(tiles):
            #print(col)
            #print(tiles)
            if tile == '1':
                Wall(self, col, row)
            if tile == 'P':
                self.player = Player(self, col, row)
            if tile == 'U':
                Powerup(self, col,row)
            if tile == 'F':
                Food(self, col, row)
            if tile == 'M':
                Mob(self, col, row)
            
                

def run (self):
    self.playing = True
    while self.running:
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
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)

        pg.display.flip()

    
      #input method
def events(self):
     for event in pg.event.get():
        if event.type == pg.QUIT:
          self.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                     self.player.move(dx=-1)
            if event.key == pg.K_RIGHT:
                     self.player.move(dx=1)
            if event.key == pg.K_UP:
                     self.player.move(dy=-1)
            if event.key == pg.K_DOWN:
                   self.player.move(dy=1)
def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x*TILESIZE,y*TILESIZE)
        surface.blit(text_surface, text_rect)                  

def show_start_screen(self):
        pass

def show_go_screen(self):
        pass
g = Game()
while True:
    g.new()
    g.run()
    


        