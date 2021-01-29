from time import sleep
from visual import visual
from random import random

track_up_left = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
track_up_right = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
track_down_left = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
track_down_right = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

crossroads_up = [0, 0, 0, 0]
crossroads_down = [0, 0, 0, 0]

#   [красный, жёлтый, зелёный]
tl = 1
tlt = [10, 3, 10]
#       0  1  2

temp = tlt[0]
start = 0
stop = 100

while start != stop:

    if (temp == 0):
        tl = (tl % 3) + 1
        temp = tlt[tl - 1]

    # tdl
    if 0 in track_down_left and random() > 0.5:
        track_down_left[0] = 1

    if 0 in track_up_right and random() > 0.5:
        track_up_right[-1] = 1

    # дорога 1
    if track_up_left[0] == 1:
        track_up_left[0] = 0
    for i in range(1, len(track_up_left)):
        if track_up_left[i] == 1:
            track_up_left[i] = 0
            track_up_left[i - 1] = 1

    # перекрёсток 1
    if crossroads_up[0] == 1:
        crossroads_up[0] = 0
        track_up_left[len(track_up_left) - 1] = 1
    for i in range(1, len(crossroads_up)):
        if crossroads_up[i] == 1:
            crossroads_up[i] = 0
            crossroads_up[i - 1] = 1

    # дорога 2
    if track_up_right[0] == 1 and tl == 3:
        track_up_right[0] = 0
        crossroads_up[len(crossroads_up) - 1] = 1
    for i in range(1, len(track_up_right)):
        if track_up_right[i] == 1:
            if tl == 3:
                track_up_right[i] = 0
                track_up_right[i - 1] = 1
            elif track_up_right[i - 1] == 0:
                track_up_right[i] = 0
                track_up_right[i - 1] = 1

    # дорога 3
    if track_down_right[-1] == 1:
        track_down_right[-1] = 0
    for i in range(len(track_down_right) - 2, -1, -1):
        if track_down_right[i] == 1:
            track_down_right[i] = 0
            track_down_right[i + 1] = 1

    # перекрёсток 2
    if crossroads_down[-1] == 1:
        crossroads_down[-1] = 0
        track_down_right[0] = 1
    for i in range(len(crossroads_down) - 2, -1, -1):
        if crossroads_down[i] == 1:
            crossroads_down[i] = 0
            crossroads_down[i + 1] = 1

    # дорога 4
    if track_down_left[-1] == 1 and tl == 3:
        track_down_left[-1] = 0
        crossroads_down[0] = 1
    for i in range(len(track_down_left) - 2, -1, -1):
        if track_down_left[i] == 1:
            if tl == 3:
                track_down_left[i] = 0
                track_down_left[i + 1] = 1
            elif track_down_left[i + 1] == 0:
                track_down_left[i] = 0
                track_down_left[i + 1] = 1

    temp -= 1
    print("RED yellow green" if tl == 1 else ("red YELLOW green" if tl == 2 else "red yellow GREEN"))
    print(visual(track_up_left, track_up_right, track_down_left, track_down_right, crossroads_up, crossroads_down))
    sleep(0.5)
    start += 1
