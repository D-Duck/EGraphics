import pygame
import random
from PIL import Image
from math import cos, sin

# COLORS
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def combine_color(list_of_colors):
    r, g, b = 0, 0, 0
    for n in range(len(list_of_colors)):
        r += list_of_colors[n][0]
        g += list_of_colors[n][1]
        b += list_of_colors[n][2]
    color = (int(round(r / len(list_of_colors) ,0)), int(round(g / len(list_of_colors) ,0)), int(round(b / len(list_of_colors) ,0)))
    return color

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

def get_available_fonts():
    print(pygame.font.get_fonts())

# DRAW FUNCTIONS
def fill(window, rgb_color):
    window.fill(rgb_color)

def draw_circle(window, color, x, y, r, border_width=0):
    pygame.draw.circle(window, color, (x, y), r, border_width)

def draw_rectangle(window, color, x, y, length, height, border_width=0, rotate_deg=0):
    if rotate_deg != 0:
        rotate_deg = rotate_deg * 0.01745329
        px0, py0 = ((0 - (length / 2)) * cos(rotate_deg) + (0 - (height / 2)) * sin(rotate_deg)) + (x + length / 2), (-(0 - (length / 2)) * sin(rotate_deg) + (0 - (height / 2)) * cos(rotate_deg)) + (y + height / 2)
        px1, py1 = ((0 - (length / 2) + length) * cos(rotate_deg) + (0 - (height / 2)) * sin(rotate_deg)) + (x + length / 2), (-(0 - (length / 2) + length) * sin(rotate_deg) + (0 - (height / 2)) * cos(rotate_deg)) + (y + height / 2)
        px2, py2 = ((0 - (length / 2) + length) * cos(rotate_deg) + (0 + height - (height / 2)) * sin(rotate_deg)) + (x + length / 2), (-(0 - (length / 2) + length) * sin(rotate_deg) + (0 + height - (height / 2)) * cos(rotate_deg)) + (y + height / 2)
        px3, py3 = ((0 - (length / 2)) * cos(rotate_deg) + (0 + height - (height / 2)) * sin(rotate_deg)) + (x + length / 2), (-(0 - (length / 2)) * sin(rotate_deg) + (0 + height - (height / 2)) * cos(rotate_deg)) + (y + height / 2)

        pygame.draw.polygon(window, color, [(px0, py0), (px1, py1), (px2, py2), (px3, py3)], border_width)
    else:
        pygame.draw.rect(window, color, (x, y, length, height), border_width)

def draw_polygon(window, color, list_of_points, border_width=0, rotate_deg=0):
    if rotate_deg != 0:
        new_points = []
        rotate_deg = rotate_deg * 0.01745329

        x_coords = [p[0] for p in list_of_points]
        y_coords = [p[1] for p in list_of_points]
        _len = len(list_of_points)
        centroid_x = sum(x_coords) / _len
        centroid_y = sum(y_coords) / _len
        centroid_x, centroid_y
        for x, y in list_of_points:
            x, y = x - centroid_x, y - centroid_y

            px = x * cos(rotate_deg) + y * sin(rotate_deg)
            py = -x * sin(rotate_deg) + y * cos(rotate_deg)

            px, py = px + centroid_x, py + centroid_y

            new_points.append((px, py))

        pygame.draw.polygon(window, color, new_points, border_width)
    else:
        pygame.draw.polygon(window, color, list_of_points, border_width)

def draw_line(window, color, x0, y0, x1, y1, border_width=0):
    pygame.draw.line(window, color, (x0, y0), (x1, y1), border_width)

def draw_pixel(window, color, x, y):
    pygame.draw.rect(window, color, (x, y, 1, 1), 0)

def draw_text(window, color, x, y, text, size=30, font='Arial'):
    font = pygame.font.SysFont(font, size)
    textsurface = font.render(str(text), False, color)
    window.blit(textsurface, (x, y))

def draw_image(window, path, x, y, scale_by=0, scale_to=0, rotate_deg=0):
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
        window.blit(img,(x, y))