import pygame as pg

from player import Player
from tilemap import Tilemap
from camera import Camera

import constants as c


pg.init()






def main():
    screen = pg.display.set_mode(c.SCREEN_SIZE)
    clock = pg.time.Clock()

    PIXELS_PER_UNIT = 64

    player = Player(
        (0, 1, 0.7, 1.8),
        c.PHYS_WALK_SPEED,
        c.PHYS_RUN_SPEED,
        c.PHYS_JUMP_POWER,
        c.PHYS_GRAVITY
    )
    
    camera = Camera(c.SCREEN_SIZE, PIXELS_PER_UNIT)
    
    tilemap = Tilemap([
        (-1, -1, 2  , 0.3),
        ( 1, -1, 0.1, 3),
        (-3,  0, 1  , 0.1),
        (-5, -3, 10 , 0.05)
    ])


    player.set_collisionmap(tilemap)

    
    while True:
        delta_time = clock.tick(60) / 1000
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            else:
                player.handle_event(event)

        player.update(delta_time)


        screen.fill(0)
        tilemap.draw(screen, camera.world_to_screen_rect)
        player.draw(screen, camera.world_to_screen_rect)


        pg.display.update()

main()
