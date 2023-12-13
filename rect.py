

class Rect:
    def __init__(self, x, y, w, h):
        self.x, self.y = x, y
        self.w, self.h = w, h

    @property
    def Rect(self):
        return self.x, self.y, self.w, self.h

    @property
    def Left(self):
        return self.x

    @property
    def Right(self):
        return round(self.x + self.w, 15)    # Rounding because of floating point precision error causing bad collision detection

    @property
    def Up(self):
        return self.y

    @property
    def Down(self):
        return round(self.y + self.h, 15)    # Rounding because of floating point precision error causing bad collision detection

    @property
    def Center(self):
        return self.x + self.w / 2, self.y + self.h / 2

    def collide_rect(self, rect):
        x, y, w, h = rect.Rect if isinstance(rect, Rect) else rect
        Left, Right, Up, Down = x, x + w, y, y + h
        
        collide_x = self.x < x < self.Right or x < self.x < Right or self.x < Right < self.Right or x < self.Right < Right
        collide_y = self.y < y < self.Down or y < self.y < Down or self.y < Down < self.Down or y < self.Down < Down

        return collide_x and collide_y

    def collide_rects(self, rects):
        for i, rect in enumerate(rects):
            if self.collide_rect(rect):
                return i
        return -1
