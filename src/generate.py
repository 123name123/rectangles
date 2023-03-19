from random import random
from typing import List, Tuple

from rectangle import Rectangle


def generate_shifted_rectangles(rectangles: List[Rectangle],
                                width: float,
                                height: float) -> Tuple[List[Rectangle], float]:
    """shift each Rectangle in list to a random vector"""
    cur_location = list()
    min_x, min_y, max_x, max_y = 2 * width, 2 * height, 0, 0
    for rectangle in rectangles:
        shift_x = random() * (width - rectangle.width())
        shift_y = random() * (height - rectangle.height())
        cur_location.append(rectangle.shift(shift_x, shift_y))
        max_x = max(max_x, cur_location[-1].right)
        min_x = min(min_x, cur_location[-1].left)
        max_y = max(max_y, cur_location[-1].top)
        min_y = min(min_y, cur_location[-1].bottom)
    cur_compact = (max_x - min_x) * (max_y - min_y)
    return cur_location, cur_compact


def generate_rectangle(min_x: float = -10000, min_y: float = -10000, max_x: float = 10000,
                       max_y: float = 10000, max_width: float = 100, max_height: float = 100) -> Rectangle:
    """generate random Rectangle"""
    left_bottom_x = (random() - 0.5) * (max_x - min_x)
    left_bottom_y = (random() - 0.5) * (max_y - min_y)
    right_top_x = left_bottom_x + random() * max_width
    right_top_y = left_bottom_y + random() * max_height
    return Rectangle(left_bottom_x, left_bottom_y, right_top_x, right_top_y)
