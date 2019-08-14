import turtle

SIDE_LEN_UNIT = 60


class Drawer:
    def __init__(self, depth):
        self.depth = depth
        self.cur_pos = self.get_init_point()
        turtle.right(300)

    @staticmethod
    def get_init_point():
        from simulator import Point
        return Point(12, 100)

    def get_init_side_len(self):
        return self.depth * SIDE_LEN_UNIT

    def draw_triangle(self, side_len):
        # turtle.right(30)
        turtle.forward(side_len)
        turtle.right(120)
        turtle.forward(side_len)
        turtle.right(120)
        turtle.forward(side_len)
        turtle.right(120)
        pass

    def freeze(self):
        turtle.mainloop()

    def move_to(self, distance, rotate=False):
        if rotate:
            turtle.right(rotate)
        turtle.forward(distance)
        if rotate:
            turtle.left(rotate)
