import pygame
import cv2
import sys
import ctypes

import objects
import main_menu
import control_menu
import quadcopter_menu
import some_functions

pygame.init()
pygame.font.init()

user32 = ctypes.windll.user32
pygame.display.set_caption("Quadcopter Control v0.5")

window = pygame.display.set_mode((user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)), pygame.FULLSCREEN)
window = pygame.display.set_mode((user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)), pygame.FULLSCREEN)

window_height = user32.GetSystemMetrics(1)
window_width = user32.GetSystemMetrics(0)
kx = window_width / 1920.0
ky = window_height / 1080.0
UserInMenu = True
UserInQuadcopterMenu = False
ToolAddPoint = True
last_mouse_pos_x = 0
last_mouse_pos_y = 0
MovingMap = False
timer = 2

MainMenu = main_menu.menu(kx, ky)
ControlMenu = control_menu.menu(kx, ky)
QuadCopterMenu = quadcopter_menu.menu(kx, ky)

while True:
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                ControlMenu.UserMap.addscale(0.015 * min(kx, ky))
            if event.button == 5:
                ControlMenu.UserMap.addscale(-0.015 * min(kx, ky))
            if event.button == 1:
                if UserInMenu:
                    MainMenu.mouseButtonDown(mouse_pos, ky)
                elif UserInQuadcopterMenu:
                    QuadCopterMenu.mouseButtonDown(mouse_pos, ky)
                else:
                    MovingMap = ControlMenu.mouseButtonDown(mouse_pos, ky, ToolAddPoint, MovingMap)
                    if MovingMap:
                        last_mouse_pos_x = mouse_pos[0]
                        last_mouse_pos_y = mouse_pos[1]
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if UserInMenu:
                    user = MainMenu.mouseButtomUp(mouse_pos)
                    UserInMenu = user[0]
                    UserInQuadcopterMenu = user[1]
                    timer = 2
                elif UserInQuadcopterMenu:
                    QuadCopterMenu.mouseButtonUp(mouse_pos)
                else:
                    q = ControlMenu.mouseButtomUp(mouse_pos, ToolAddPoint, MovingMap, timer)
                    ToolAddPoint = q[0]
                    MovingMap = q[1]
                    timer = 2

    if UserInQuadcopterMenu:
        QuadCopterMenu.Update(some_functions.GetNumber(keys))
    if not(UserInMenu) and not(UserInQuadcopterMenu) and ControlMenu.InAddImageMenu:
        ControlMenu.AddImageMenu.Update(keys)

    if mouse_pressed[0] and MovingMap:
        ControlMenu.UserMap.addposition(mouse_pos[0] - last_mouse_pos_x, mouse_pos[1] - last_mouse_pos_y)
        last_mouse_pos_x = mouse_pos[0]
        last_mouse_pos_y = mouse_pos[1]
    elif mouse_pressed[0] and ControlMenu.set_area:
        ControlMenu.UserMap.set_pos1(mouse_pos)

    if timer > 0:
        timer -= 1

    if keys[pygame.K_ESCAPE] and not(UserInMenu):
        UserInMenu = True
        UserInQuadcopterMenu = False

    window.fill((198, 196, 183))

    if UserInMenu:
        MainMenu.draw(window)
    elif UserInQuadcopterMenu:
        QuadCopterMenu.draw(window)
    else:
        ControlMenu.draw(window)

    pygame.display.update()
    pygame.time.delay(10)