import pygame
import random
from PIL import Image
from math import cos, sin
from PIL import ImageColor

# COLORS
class color:
    black = (0, 0, 0)
    white = (255, 255, 255)
    gray = (150, 150, 150)
    red = (255, 0, 0)
    lime = (0, 255, 0)
    green = (50,205,50)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    magenta = (255, 0, 255)
    light_blue = (0, 255, 255)
    hot_pink = (255,29,142)
    brown = (139,69,19)
    dark_violet = (148,0,211)
    sky_blue = (135,206,235)

def random_color(seed=None):
    random.seed(seed)
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def combine_colors(list_of_colors):
    r, g, b = 0, 0, 0
    for n in range(len(list_of_colors)):
        r += list_of_colors[n][0]
        g += list_of_colors[n][1]
        b += list_of_colors[n][2]
    color = (int(round(r / len(list_of_colors) ,0)), int(round(g / len(list_of_colors) ,0)), int(round(b / len(list_of_colors) ,0)))
    return color

# CONVERTERS
def deg_to_rad(deg):
    return deg * 0.01745329

def rad_to_deg(rad):
    return rad / 0.01745329

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % (rgb[0], rgb[1], rgb[2])

def hex_to_rgb(hex):
    if hex[0] != "#":
        hex = "#" + hex
    return ImageColor.getrgb(hex)

def pos_to_point(x, y):
    return (x, y)

# MAIN FUNCTIONS
def create_window(screen_size=(500, 500), window_title=None):
    pygame.init()
    if window_title != None:
        pygame.display.set_caption(window_title)
    return pygame.display.set_mode(screen_size)

def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()

# GET FUNCTIONS
def get_mouse_poz():
    return pygame.mouse.get_pos()

def get_mouse_click():
    ml, mm, mr = pygame.mouse.get_pressed()

    if ml == 1:
        ml = True
    else:
        ml = False
    if mm == 1:
        mm = True
    else:
        mm = False
    if mr == 1:
        mr = True
    else:
        mr = False

    return ml, mm, mr

def get_pixel_color(window, x, y):
    return window.get_at((x, y))

def get_available_fonts():
    print(pygame.font.get_fonts())

# DRAW FUNCTIONS
def fill(window, color):
    window.fill(color)

def draw_circle(window, color, x, y, r, border_width=0, draw_offset=(0, 0)):
    x += draw_offset[0]
    y += draw_offset[1]
    pygame.draw.circle(window, color, (x, y), r, border_width)

def draw_rectangle(window, color, x, y, length, height, border_width=0, rotate_deg=0, rotate_origin=None,draw_offset=(0, 0)):
    try:
        if draw_offset[0] == "center":
            x = x - int(round(length / 2))
        if draw_offset[1] == "center":
            y = y - int(round(height / 2))

        if draw_offset[0] != "center":
            x = x + draw_offset[0]
        if draw_offset[1] != "center":
            y = y + draw_offset[1]
    except:
        if draw_offset == "center":
            x = x - int(round(length / 2))
            y = y - int(round(height / 2))

    if rotate_deg != 0 or rotate_origin == "left" or rotate_origin == "right":
        if rotate_origin  == "right":
            x, y = cos(deg_to_rad(-rotate_deg)) * -length/2 + x, sin(deg_to_rad(-rotate_deg)) * -length/2 + y

        if rotate_origin  == "left":
            x, y = cos(deg_to_rad(-rotate_deg)) * length/2 + x, sin(deg_to_rad(-rotate_deg)) * length/2 + y

        rotate_deg = rotate_deg * 0.01745329
        px0, py0 = ((0 - (length / 2)) * cos(rotate_deg) + (0 - (height / 2)) * sin(rotate_deg)) + (x + length / 2), (-(0 - (length / 2)) * sin(rotate_deg) + (0 - (height / 2)) * cos(rotate_deg)) + (y + height / 2)
        px1, py1 = ((0 - (length / 2) + length) * cos(rotate_deg) + (0 - (height / 2)) * sin(rotate_deg)) + (x + length / 2), (-(0 - (length / 2) + length) * sin(rotate_deg) + (0 - (height / 2)) * cos(rotate_deg)) + (y + height / 2)
        px2, py2 = ((0 - (length / 2) + length) * cos(rotate_deg) + (0 + height - (height / 2)) * sin(rotate_deg)) + (x + length / 2), (-(0 - (length / 2) + length) * sin(rotate_deg) + (0 + height - (height / 2)) * cos(rotate_deg)) + (y + height / 2)
        px3, py3 = ((0 - (length / 2)) * cos(rotate_deg) + (0 + height - (height / 2)) * sin(rotate_deg)) + (x + length / 2), (-(0 - (length / 2)) * sin(rotate_deg) + (0 + height - (height / 2)) * cos(rotate_deg)) + (y + height / 2)

        pygame.draw.polygon(window, color, [(px0, py0), (px1, py1), (px2, py2), (px3, py3)], border_width)
    else:
        pygame.draw.rect(window, color, (x, y, length, height), border_width)

def draw_polygon(window, color, list_of_points, border_width=0, rotate_deg=0, draw_offset=(0, 0)):
    if draw_offset[0] == "center":
        _len = len(list_of_points)
        x_coords = [p[0] for p in list_of_points]
        centroid_x = sum(x_coords) / _len
        draw_offset = (centroid_x - list_of_points[0][0], draw_offset[1])
    if draw_offset[1] == "center":
        _len = len(list_of_points)
        y_coords = [p[1] for p in list_of_points]
        centroid_y = sum(y_coords) / _len
        draw_offset = (draw_offset[0], centroid_y - list_of_points[0][1])
    if draw_offset == "center":
        x_coords = [p[0] for p in list_of_points]
        y_coords = [p[1] for p in list_of_points]
        _len = len(list_of_points)
        centroid_x = sum(x_coords) / _len
        centroid_y = sum(y_coords) / _len
        draw_offset = (centroid_x - list_of_points[0][0], centroid_y - list_of_points[0][1])

    new_list_of_points = []
    for points in list_of_points:
        new_list_of_points.append((points[0] + draw_offset[0], points[1] + draw_offset[1]))
    list_of_points = new_list_of_points

    if rotate_deg != 0:
        new_points = []
        rotate_deg = rotate_deg * 0.01745329

        x_coords = [p[0] for p in list_of_points]
        y_coords = [p[1] for p in list_of_points]
        _len = len(list_of_points)
        centroid_x = sum(x_coords) / _len
        centroid_y = sum(y_coords) / _len
        new_list = []
        for x, y in list_of_points:
                x, y = x - centroid_x, y - centroid_y

                px = x * cos(rotate_deg) + y * sin(rotate_deg)
                py = -x * sin(rotate_deg) + y * cos(rotate_deg)

                px, py = px + centroid_x, py + centroid_y

                new_points.append((px, py))

        pygame.draw.polygon(window, color, new_points, border_width)
    else:
        pygame.draw.polygon(window, color, list_of_points, border_width) # #

def draw_line(window, color, x0, y0, x1, y1, border_width=1):
    pygame.draw.line(window, color, (x0, y0), (x1, y1), border_width)

def draw_pixel(window, color, x, y):
    pygame.draw.rect(window, color, (x, y, 1, 1), 0)

def draw_text(window, color, x, y, text, size=30, font='Arial', draw_offset=(0, 0)):
    font = pygame.font.SysFont(font, size)
    textsurface = font.render(str(text), False, color)
    try:
        if draw_offset[0] == "center":
            x = x - int(round(textsurface.get_rect()[2] / 2))
        else:
            x = x + draw_offset[0]
        if draw_offset[1] == "center":
            y = y - int(round(textsurface.get_rect()[3] / 2))
        else:
            y = y + draw_offset[1]
    except:
        if draw_offset == "center":
            x = x - int(round(textsurface.get_rect()[2] / 2))
            y = y - int(round(textsurface.get_rect()[3] / 2))
        else:
            x = x + draw_offset[0]
            y = y + draw_offset[1]

    window.blit(textsurface, (x, y))

def draw_image(window, path, x, y, scale_by=0, scale_to=0, rotate_deg=0, draw_offset=(0, 0)):
    img = Image.open(path)

    if scale_by != 0:
        scale = int(round(img.size[0] / scale_by, 0))
        img = img.resize((scale, int((float(img.size[1]) * float((scale / float(img.size[0])))))))
    if scale_to != 0:
        img = img.resize((scale_to, int((float(img.size[1]) * float((scale_to / float(img.size[0])))))))

    if rotate_deg != 0:
        width, height = img.size
        img = img.rotate(rotate_deg, resample=0, expand=True, center=None, translate=None, fillcolor=None)

    mode, size, data = img.mode, img.size, img.tobytes()
    img = pygame.image.fromstring(data, size, mode)

    if scale_to != 0 and scale_by != 0:
        print("Can not scale_by and scale_to at the same time !!")
    else:
        try:
            if draw_offset[0] == "center":
                x = x - int(round(img.get_rect()[2] / 2))
            else:
                x = x + draw_offset[0]
            if draw_offset[1] == "center":
                y = y - int(round(img.get_rect()[3] / 2))
            else:
                y = y + draw_offset[1]
        except:
            if draw_offset == "center":
                x = x - int(round(img.get_rect()[2] / 2))
                y = y - int(round(img.get_rect()[3] / 2))

        window.blit(img,(x, y))