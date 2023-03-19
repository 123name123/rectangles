class Rectangle:
    """Rectangle class"""

    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        self.left = x1
        self.bottom = y1
        self.right = x2
        self.top = y2

    def width(self):
        """get width"""

        return self.right - self.left

    def height(self):
        """get height"""

        return self.top - self.bottom

    def to_zero(self):
        """shift Rectangle to (0, 0) coordinates"""

        return Rectangle(0, 0, self.width(), self.height())

    def shift(self, shift_x: float, shift_y: float):
        """shift Rectangle to a vector"""
        return Rectangle(shift_x + self.left, shift_y + self.bottom,
                         shift_x + self.right, shift_y + self.top)

    def intersection(self, other) -> float:
        """calculate intersection area for two Rectangles"""

        left_x = max(self.left, other.left)
        right_x = min(self.right, other.right)
        bottom_y = max(self.bottom, other.bottom)
        top_y = min(self.top, other.top)
        if left_x > right_x or bottom_y > top_y:
            return 0
        return (right_x - left_x) * (top_y - bottom_y)

    def __str__(self):
        return f"min_x: {self.left} min_y: {self.bottom} " \
               f"max_x: {self.right} max_y: {self.top}"
