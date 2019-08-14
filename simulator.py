from drawer.turtle import Drawer

DEFAULT_DEPTH = 5


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class SierpinskiSimulation:
    def __init__(self, drawer, max_depth):
        self.drawer = drawer
        self.depth = 0
        self.max_depth = max_depth

    def show_simulation(self):
        self.draw_triangle(
            self.drawer.get_init_side_len()
        )
        self.drawer.freeze()

    def draw_triangle(self, side_len):
        if self.depth >= self.max_depth:
            return

        self.depth += 1

        self.drawer.draw_triangle(side_len / 2)
        self.draw_triangle(side_len / 2)
        self.drawer.move_to(side_len / 2)
        self.drawer.draw_triangle(side_len / 2)
        self.draw_triangle(side_len / 2)
        self.drawer.move_to(side_len / 2, 120)
        self.drawer.draw_triangle(side_len / 2)
        self.draw_triangle(side_len / 2)
        self.drawer.move_to(side_len / 2, -120)

        self.depth -= 1
