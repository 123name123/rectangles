from typing import List
import matplotlib.pyplot as plt

from rectangle import Rectangle


def draw_rectangles(before_rectangles: List[Rectangle], after_rectangles: List[Rectangle]) -> None:
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

    ax1.set_title('Before relocating')
    for rectangle in before_rectangles:
        x = [rectangle.left, rectangle.left, rectangle.right, rectangle.right, rectangle.left]
        y = [rectangle.bottom, rectangle.top, rectangle.top, rectangle.bottom, rectangle.bottom]
        ax1.plot(x, y)

    ax2.set_title('After relocating')
    for rectangle in after_rectangles:
        x = [rectangle.left, rectangle.left, rectangle.right, rectangle.right, rectangle.left]
        y = [rectangle.bottom, rectangle.top, rectangle.top, rectangle.bottom, rectangle.bottom]
        ax2.plot(x, y)

    plt.show()
