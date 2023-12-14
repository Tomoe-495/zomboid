import pygame as pg
import json
from spritesheet import Sprite

def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def get_obj(instance, find):
    for inst in instance:
        if inst["__identifier"] == find:
            return inst

def get_tile_layer(layer_instance, layer, csv_map, size, sprite):
    map_surface = pg.Surface((csv_map["__cWid"]*size, csv_map["__cHei"]*size))
    map_surface.set_colorkey((0, 0, 0))
    layer = get_obj(layer_instance, layer)
	# incoming data format
	# { "px": [0,0], "src": [64,64], "f": 0, "t": 132, "d": [0] },
    for tile in layer["gridTiles"]:
        s = sprite.get_sprite(tile["src"], size)
        map_surface.blit(pg.transform.flip(s, tile["f"], 0), (tile["px"][0], tile["px"][1]))

    return map_surface


class Tilemap:
    def __init__(self):
        self.rects = []
        self.scale = 1

        self.map = load_json("map/map.ldtk")
        layer_instance = self.map["levels"][0]["layerInstances"]
        self.spriteSheet = Sprite("map/map.png")
        csv_map = get_obj(layer_instance, "Grid_set")
        size = csv_map["__gridSize"]

        self.player_pos = get_obj(layer_instance, "Player")["entityInstances"][0]["px"]

        self.layerTiles = get_tile_layer(layer_instance, "Tiles", csv_map, size, self.spriteSheet)
        self.layerAssets = get_tile_layer(layer_instance, "Assets", csv_map, size, self.spriteSheet)
        self.layerTrees = get_tile_layer(layer_instance, "Trees", csv_map, size, self.spriteSheet)
        self.layerBackground = get_tile_layer(layer_instance, "Background", csv_map, size, self.spriteSheet)

        x = y = 0
        for block in csv_map["intGridCsv"]:
            if block == 1:
                self.rects.append(pg.Rect(x, y, size, size))
            x += size

            if x == csv_map["__cWid"] * size:
                y += size
                x = 0

    def scale_map(self, scale_factor):
        self.scale = scale_factor
        
        self.layerTiles = pg.transform.scale_by(self.layerTiles, scale_factor)
        self.layerAssets = pg.transform.scale_by(self.layerAssets, scale_factor)
        self.layerTrees = pg.transform.scale_by(self.layerTrees, scale_factor)
        self.layerBackground = pg.transform.scale_by(self.layerBackground, scale_factor)

        px, py = self.player_pos
        self.player_pos = px * scale_factor, py * scale_factor

        for rect in self.rects:
            rect.x *= scale_factor
            rect.y *= scale_factor
            rect.w *= scale_factor
            rect.h *= scale_factor

    def set_data(self, rects):
        self.rects.clear()
        self.rects.extend(rects)

    def draw(self, surface, player, camera):
        # for rect in self.rects:
        #     pg.draw.rect(surface, (0, 0, 0), world_to_screen_rect(rect))
        
        surface.blit(self.layerBackground, camera.offset)
        
        player.draw(surface, camera)
        
        surface.blit(self.layerTiles, camera.offset)
        surface.blit(self.layerTrees, camera.offset)
        surface.blit(self.layerAssets, camera.offset)
