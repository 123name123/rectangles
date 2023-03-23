from random import random
from typing import List, Tuple, Optional

from rectangle import Rectangle


def generate_shifted_rectangles(rectangles: List[Rectangle],
                                width: float,
                                height: float) -> Optional[List[Rectangle]]:
    """shift each Rectangle in list to a random vector"""
    cur_location = list()
    for i, rectangle in enumerate(rectangles):
        shift_x = max(0, random() * (width - rectangle.width()))
        shift_y = max(0, random() * (height - rectangle.height()))
        probable_rectangle = rectangle.shift(shift_x, shift_y)
        for new_rectangle in cur_location:
            if probable_rectangle.intersection(new_rectangle):
                return None
        cur_location.append(probable_rectangle)
    return cur_location


def generate_rectangle(min_x: float = -10000, min_y: float = -10000, max_x: float = 10000,
                       max_y: float = 10000, max_width: float = 100, max_height: float = 100) -> Rectangle:
    """generate random Rectangle"""
    left_bottom_x = (random() - 0.5) * (max_x - min_x)
    left_bottom_y = (random() - 0.5) * (max_y - min_y)
    right_top_x = left_bottom_x + random() * max_width
    right_top_y = left_bottom_y + random() * max_height
    return Rectangle(left_bottom_x, left_bottom_y, right_top_x, right_top_y)
