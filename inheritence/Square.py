from inheritence.Shape import Shape


class Square(Shape):
    def __init__(self, side=1, x=0, y=0):
        super().__init__(x, y)
        self.side = side

    def area(self):
        return self.side * self.side
