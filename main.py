import pygame as pg

from player import Player
from tilemap import Tilemap
from camera import Camera

import constants as c


pg.init()



def main():
    screen = pg.display.set_mode(c.SCREEN_SIZE)
    clock = pg.time.Clock()

    player = Player(
        (500, 200, 20, 50),
        c.PHYS_WALK_SPEED,
        c.PHYS_RUN_SPEED,
        c.PHYS_JUMP_POWER,
        c.PHYS_GRAVITY
    )
    
    camera = Camera(c.SCREEN_SIZE)
    
    tilemap = Tilemap()

    player.set_collisionmap(tilemap)

    
    while True:
        delta_time = clock.tick(60) / 1000
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            else:
                player.handle_event(event)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    return

        player.update(delta_time)
        camera.look_at_centered(*player.Center)

        screen.fill((144, 244, 200))
        tilemap.draw(screen, player, camera.world_to_screen_rect)
        #player.draw(screen, camera.world_to_screen_rect)


        pg.display.update()

if __name__ == "__main__":
    main()
