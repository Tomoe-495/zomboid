

class Camera:
    def __init__(self, screen_size, pixels_per_unit, start_pos=None):
        self.w, self.h = screen_size
        self.ppu = pixels_per_unit
        self.x, self.y = start_pos or (0,0)

        self.x -= self.w / self.ppu / 2
        self.y -= self.h / self.ppu / 2

    def move(self, x_offset, y_offset):
        self.x += x_offset
        self.y += y_offset

    def world_to_screen_rect(self, rect):
        x, y, w, h = rect
        w = int(w * self.ppu) + 1
        h = int(h * self.ppu) + 1

        x = int((x - self.x) * self.ppu)
        y = int(self.h - (y - self.y) * self.ppu) - h    # Subtract from height to flip y-axis

        return x, y, w, h
