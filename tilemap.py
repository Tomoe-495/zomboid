import pygame as pg
import json

def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def get_obj(instance, find):
    for inst in instance:
        if inst["__identifier"] == find:
            return inst

class Tilemap:
    def __init__(self):
        self.rects = []

        self.map = load_json("map/map.ldtk")
        self.layer_instance = self.map["levels"][0]["layerInstances"]

        csv_map = get_obj(self.layer_instance, "Grid_set")
        size = csv_map["__gridSize"]

        self.map_surface = pg.Surface((csv_map["__cWid"]*size, csv_map["__cHei"]*size))

        x = y = 0
        for block in csv_map["intGridCsv"]:
            if block == 1:
                self.rects.append(pg.Rect(x, y, size, size))
            x += size

            if x == csv_map["__cWid"] * size:
                y += size
                x = 0

    def set_data(self, rects):
        self.rects.clear()
        self.rects.extend(rects)

    def draw(self, surface, player, world_to_screen_rect):
        for rect in self.rects:
            pg.draw.rect(surface, (0, 0, 0), world_to_screen_rect(rect))

        pg.draw.rect(surface, 0x00ff00, world_to_screen_rect(player.Rect), 2)
