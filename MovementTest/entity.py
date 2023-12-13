import pygame as pg

from rect import Rect


class Entity(Rect):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

        self.vel_x = 0
        self.vel_y = 0

        self.visible = True
        self.active = True

    def handle_event(self, event):
        pass

    def update(self, delta_time):
        pass

    def draw(self, surface, world_to_screen_rect_method):
        if self.active and self.visible:
            pg.draw.rect(surface, 0x00ff00, world_to_screen_rect_method(self.Rect), 2)

    def collide_entity(self, entity):
        x, y, w, h = entity.Rect
        Right, Up = x + w, y + h

        #x_overlap = 

        return (self.x <= x <= self.Right or x <= self.x <= Right) and (self.y <= y <= self.Up or y <= self.y <= Up)

    def collide_entities(self, entities):
        for i, entity in enumerate(entities):
            if self.collide_entity(entity):
                return i
        return -1

