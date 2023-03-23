from copy import deepcopy
from typing import List, Tuple
import sys

from rectangle import Rectangle
from score_count import get_union_area
from generate import generate_shifted_rectangles, generate_rectangle
from draw import draw_rectangles

EPS = 10 ** -6


def find_best_location(rectangles: List[Rectangle], max_iter: int = 1000) -> List[Rectangle]:
    """find best relocation for rectangles
       get: list of rectangles, max_iteration=1000
       return: list of relocated rectangles, score, extra_space"""
    zero_rectangles = [rectangle.to_zero() for rectangle in rectangles]
    best_location = deepcopy(zero_rectangles)

    width, height, max_union_area = 0, 0, 0
    for rectangle in zero_rectangles:
        width += rectangle.width()
        height += rectangle.height()
        max_union_area += rectangle.width() * rectangle.height()
    for _ in range(max_iter):
        cur_location, cur_compact = generate_shifted_rectangles(zero_rectangles, width, height)
        score = max_union_area - get_union_area(cur_location)
        if score < EPS:
            best_location = cur_location
            width *= 0.9
            height *= 0.9

    return best_location


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            n = int(sys.argv[1])
            random_rectangles = [generate_rectangle(-20, -20, 20, 20, 10, 10) for _ in range(n)]
            relocated_rectangles = find_best_location(random_rectangles)
            draw_rectangles(random_rectangles, relocated_rectangles)
        except Exception as ex:
            print(ex)
    else:
        try:
            n = int(input())
            rectangles = list()
            for _ in range(n):
                rectangles.append(Rectangle(*list(map(float, input().split()))))
            relocated_rectangles = find_best_location(rectangles)
            draw_rectangles(rectangles, relocated_rectangles)
        except Exception as ex:
            print(ex)
