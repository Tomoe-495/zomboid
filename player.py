import pygame as pg

from entity import Entity


def get_sign(x):
    return int(-1 if x < 0 else x > 0)


class CollisionData:
    def __init__(self, collision, direction_x=0, direction_y=0):
        self.__collision = collision
        self.__dir_x = direction_x
        self.__dir_y = direction_y

    @property
    def Collision(self):
        return self.__collision

    @property
    def CollideDirection(self):
        return self.__dir_x, self.__dir_y

    @property
    def CollideLeft(self):
        return self.__dir_x == -1

    @property
    def CollideRight(self):
        return self.__dir_x == 1

    @property
    def CollideBottom(self):
        return self.__dir_y == -1

    @property
    def CollideTop(self):
        return self.__dir_y == 1


class Player(Entity):
    def __init__(self, rect, walk_speed, run_speed, jump_power, gravity):
        super().__init__(*rect)

        self.walk_speed = walk_speed
        self.run_speed = run_speed
        self.jump_power = jump_power
        self.gravity = gravity
        self.sprinting = False
        self.jumping = False

        self.collision_map = None

    @property
    def Speed(self):
        return self.run_speed if self.sprinting else self.walk_speed

    def set_collisionmap(self, collision_map):
        self.collision_map = collision_map

    def draw(self, surface, camera):
        pg.draw.rect(surface, 0xff00ff, camera.world_to_screen_rect(self.Rect), 2)

    def handle_event(self, event):
        if event.type == pg.KEYDOWN:
            self.vel_x += (event.key == pg.K_d) - (event.key == pg.K_a)
            
            if event.key == pg.K_SPACE:
                self.jumping = True
            elif event.key == pg.K_LSHIFT:
                self.sprinting = True
                
        elif event.type == pg.KEYUP:
            self.vel_x -= (event.key == pg.K_d) - (event.key == pg.K_a)

            if event.key == pg.K_SPACE:
                self.jumping = False
            elif event.key == pg.K_LSHIFT:
                self.sprinting = False
            

    def update(self, delta_time):
        self.vel_y -= self.gravity * delta_time

        if self.jumping and self.grounded:
            self.vel_y = -self.jump_power

        x_offset = self.vel_x * delta_time * self.Speed
        y_offset = self.vel_y * delta_time

        collision = self.collide_collision_map(x_offset, y_offset)

        self.grounded = False
        if collision.Collision:
            if collision.CollideBottom:
                self.vel_y = 0
                self.grounded = True
            elif collision.CollideTop:
                self.vel_y = 0

    def collide_collision_map(self, x_offset, y_offset):
        if self.collision_map:
            collide_x = 0
            collide_y = 0
            collision = False

            # Collide along x-axis
            self.x += x_offset
            if (index := self.collide_rects(self.collision_map.rects)) > -1:
                collision = True
                #self.x -= x_offset
                collide_x = get_sign(-self.vel_x)   # Get sign

                cx, cy, cw, ch = self.collision_map.rects[index]
                
                if collide_x > 0: self.x = cx + cw
                elif collide_x < 0: self.x = cx - self.w

            # Collide along y-axis
            self.y += y_offset
            if (index := self.collide_rects(self.collision_map.rects)) > -1:
                collision = True
                #self.y -= y_offset
                collide_y = get_sign(-self.vel_y)   # Get sign

                cx, cy, cw, ch = self.collision_map.rects[index]
                
                if collide_y > 0: self.y = cy + ch
                elif collide_y < 0: self.y = cy - self.h

            return CollisionData(collision, collide_x, collide_y)
        
        return CollisionData(False)
