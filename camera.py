

class Camera:
    def __init__(self, screen_size, start_pos=None):
        self.w, self.h = screen_size
        self.x, self.y = 0, 0
        self.look_at(*start_pos or (0,0))

    def move(self, x_offset, y_offset):
        self.x += x_offset
        self.y += y_offset

    def look_at(self, x, y):
        self.x = x
        self.y = y

    def look_at_centered(self, x, y):
        self.x = x - self.w // 2
        self.y = y - self.h // 2

    def world_to_screen_rect(self, rect):
        x, y, w, h = rect

        x = x - self.x
        y = y - self.y
        
        return x, y, w, h
