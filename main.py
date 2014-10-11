import time
import random
from tkinter import Tk, Canvas, BOTH

# 1й вариант
from drawing import draw_array
# использование:
# draw_array(canvas, randoms)

# 2й вариант
# import drawing
# использование:
# drawing.draw_array(canvas, randoms)
# drawing.print,

from sorting import sort_array


def main():
    NUMBER_COUNT = 400
    MAX_VALUE = 400

    # то же самое, что
    # numbers = []
    # for _ in range(NUMBER_COUNT):
    #     numbers.append(random.randrange(0, MAX_VALUE)
    randoms = [random.randrange(0, MAX_VALUE) for _ in range(NUMBER_COUNT)]

    root = Tk()
    root.title = "Random Array"
    root.geometry("{}x{}".format(NUMBER_COUNT, MAX_VALUE))
    canvas = Canvas(root)
    canvas.pack(fill=BOTH, expand=1)

    # arr = [1, 5, -4, 'a', None]
    # enumerate(arr) => ((0, 1), (1, 5), (2, -4), (3, 'a'), (4, None))
    draw_array(canvas, randoms)

    # 2 числа: 1 проход и сравнить первое и второе
    # 3 числа: 2 прохода, в первой итерации сравнить 1 и 2е, затем 2е и третье

    # сортировка пузырьком:
    # a[0] ? a[1], a[1] ? a[2], a[2] ? a[3], .... a[n-2] ? a[n-1]
    # 2 итерация
    # a[0] ? a[1], a[1] ? a[2], ... , a[n-3], a[n-2]
    # ...
    # в самом конце
    # a[0] ? a[1]
    # i = 399, 398, 397, ..., 1

    def callback(array):
        draw_array(canvas, array)

        time.sleep(0.10)

    sort_array(randoms, callback)

    root.mainloop()


main()