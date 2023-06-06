class ItemAttrs:
    def __init__(self) -> None:
        pass


class Point(ItemAttrs):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = x
        self.y = y


pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10