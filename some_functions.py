import pygame
import cv2

def screenShotMake(img):
    image = img
    dst = cv2.GaussianBlur(image, (15, 15), cv2.BORDER_DEFAULT)
    return dst
def convert_and_screenShotMake(window):
    view = pygame.surfarray.array3d(window)
    view = view.transpose([1, 0, 2])
    img_bgr = cv2.cvtColor(view, cv2.COLOR_RGB2BGR)

    img_bgr = screenShotMake(img_bgr)

    view = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    view = view.transpose([1, 0, 2])
    return pygame.pixelcopy.make_surface(view)
def GetNumber(keys):
    if keys[pygame.K_0]:
        return '0'
    elif keys[pygame.K_1]:
        return '1'
    elif keys[pygame.K_2]:
        return '2'
    elif keys[pygame.K_3]:
        return '3'
    elif keys[pygame.K_4]:
        return '4'
    elif keys[pygame.K_5]:
        return '5'
    elif keys[pygame.K_6]:
        return '6'
    elif keys[pygame.K_7]:
        return '7'
    elif keys[pygame.K_8]:
        return '8'
    elif keys[pygame.K_9]:
        return '9'
    elif keys[pygame.K_BACKSPACE]:
        return '-'
    else:
        return  ''
def GetKey(keys):
    if keys[pygame.K_q]:
        return 'q'
    elif keys[pygame.K_w]:
        return 'w'
    elif keys[pygame.K_e]:
        return 'e'
    elif keys[pygame.K_r]:
        return 'r'
    elif keys[pygame.K_t]:
        return 't'
    elif keys[pygame.K_y]:
        return 'y'
    elif keys[pygame.K_u]:
        return 'u'
    elif keys[pygame.K_i]:
        return 'i'
    elif keys[pygame.K_o]:
        return 'o'
    elif keys[pygame.K_p]:
        return 'p'
    elif keys[pygame.K_a]:
        return 'a'
    elif keys[pygame.K_s]:
        return 's'
    elif keys[pygame.K_d]:
        return 'd'
    elif keys[pygame.K_f]:
        return 'f'
    elif keys[pygame.K_g]:
        return 'g'
    elif keys[pygame.K_h]:
        return 'h'
    elif keys[pygame.K_h]:
        return 'h'
    elif keys[pygame.K_j]:
        return 'j'
    elif keys[pygame.K_k]:
        return 'k'
    elif keys[pygame.K_l]:
        return 'l'
    elif keys[pygame.K_z]:
        return 'z'
    elif keys[pygame.K_x]:
        return 'x'
    elif keys[pygame.K_c]:
        return 'c'
    elif keys[pygame.K_v]:
        return 'v'
    elif keys[pygame.K_b]:
        return 'b'
    elif keys[pygame.K_n]:
        return 'n'
    elif keys[pygame.K_m]:
        return 'm'
    elif keys[pygame.K_BACKSPACE]:
        return '-'
    elif keys[pygame.K_SLASH]:
        return '\\'
    elif keys[pygame.K_PERIOD]:
        return '.'
    else:
        return ''
def get_info(x, y, focus, Height):
    d = Height
    Hx = x / 10.0
    Hy = y / 10.0
    focus = focus / 10.0
    hx = (Hx * d) / focus - Hx
    hy = (Hy * d) / focus - Hy
    return [hx, hy]