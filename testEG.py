import EGraphics as eg
from EGraphics import color
import time

window = eg.create_window()

x, y = 0, 0
root_x, root_y = 100, 100
while True:
    if eg.get_mouse_click()[0]:
        x, y = eg.get_mouse_poz()
        x, y = x - root_x, y - root_y
    else:
        x, y = 0, 0

    eg.fill(window, color.white)
    for yg in range(-25, 525, 50):
        for xg in range(-25, 525, 50):
            eg.draw_rectangle(window, color.red, xg, yg, 50, 50, 1)
    for yg in range(0, 500, 50):
        for xg in range(0, 500, 50):
            eg.draw_rectangle(window, color.black, xg, yg, 50, 50, 1)

    eg.draw_text(window, color.black, 100, 100, "Hello World!!!", draw_offset="center")

    eg.update()