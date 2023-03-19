from copy import deepcopy
from typing import List, Tuple
import sys

from rectangle import Rectangle
from score_count import get_score
from generate import generate_shifted_rectangles, generate_rectangle
from draw import draw_rectangles

EPS = 10 ** -6


def find_best_location(rectangles: List[Rectangle], max_iter: int = 1000) -> Tuple[List[Rectangle], float, float]:
    """find best relocation for rectangles
       get: list of rectangles, max_iteration=1000
       return: list of relocated rectangles, score, extra_space"""
    zero_rectangles = [rectangle.to_zero() for rectangle in rectangles]
    best_location = deepcopy(zero_rectangles)

    width, height, union_area = 0, 0, 0
    for rectangle in zero_rectangles:
        width += rectangle.width()
        height += rectangle.height()
        union_area += rectangle.width() * rectangle.height()
    best_score = width * height
    best_compact = width * height

    for _ in range(max_iter):
        cur_location, cur_compact = generate_shifted_rectangles(zero_rectangles, width, height)
        score = get_score(cur_location)
        if score + EPS < best_score:
            best_score = score
            best_location = cur_location
            best_compact = cur_compact
        elif abs(score - best_score) < EPS and cur_compact + EPS < best_compact:
            best_location = cur_location
            best_compact = cur_compact

    return best_location, best_score, best_compact - union_area


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            n = int(sys.argv[1])
            random_rectangles = [generate_rectangle(-20, -20, 20, 20, 10, 10) for _ in range(n)]
            relocated_rectangles, _, _ = find_best_location(random_rectangles)
            draw_rectangles(random_rectangles, relocated_rectangles)
        except Exception as ex:
            print(ex)
    else:
        try:
            n = int(input())
            rectangles = list()
            for _ in range(n):
                rectangles.append(Rectangle(*list(map(float, input().split()))))
            relocated_rectangles, _, _ = find_best_location(rectangles)
            draw_rectangles(rectangles, relocated_rectangles)
        except Exception as ex:
            print(ex)
