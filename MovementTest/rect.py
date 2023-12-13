

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
    def Down(self):
        return self.y

    @property
    def Up(self):
        return round(self.y + self.h, 15)    # Rounding because of floating point precision error causing bad collision detection

    def collide_rect(self, rect):
        x, y, w, h = rect.Rect if isinstance(rect, Rect) else rect
        return (self.x < x < self.Right or x < self.x < (x + w)) and (self.y < y < self.Up or y < self.y < (y + h))

    def collide_rects(self, rects):
        for i, rect in enumerate(rects):
            if self.collide_rect(rect):
                return i
        return -1
