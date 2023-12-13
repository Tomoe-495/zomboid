import pygame as pg


class Tilemap:
    def __init__(self, rects):
        self.rects = []
        if rects: self.set_data(rects)

    def set_data(self, rects):
        self.rects.clear()
        self.rects.extend(rects)

    def draw(self, surface, world_to_screen_rect):
        for rect in self.rects:
            pg.draw.rect(surface, 0xa0a0a0, world_to_screen_rect(rect))
