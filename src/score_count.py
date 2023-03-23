from typing import List

from shapely.geometry import box
from shapely.ops import unary_union

from rectangle import Rectangle


def get_union_area(rectangles: List[Rectangle]) -> float:
    """calculate common union area for list of Rectangles"""

    boxes = [box(rectangle.left, rectangle.bottom, rectangle.right, rectangle.top) for rectangle in rectangles]
    union = unary_union(boxes)
    return union.area
