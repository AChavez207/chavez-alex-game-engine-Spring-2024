#This file was created by : Alex Chavez
#Loop through a list

import pygame as pg

FPS = 30

clock = pg.time.Clock()

frames = ["frame1", "frame2", "frame3", "frame4"]

# print(len(frames))

current_frame = 0

frames_length = len(frames)

then = 0


while True:
    # print("forever....")
    now = pg.time.get_ticks()
    clock.tick(FPS)
    if now - then > 1000:
        print(now)
        then = now
        current_frame += 1
        print(frames[current_frame%frames_length])