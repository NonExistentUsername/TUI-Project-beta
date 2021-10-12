import objects
import pygame
import sys
class menu:
    def __init__(self, kx, ky):
        self.last_mouse_pos = [-1, -1]
        self.Exit = objects.Label(round(780.0 * kx), round(640.0 * ky), round(360.0 * kx), round(80.0 * ky),
                                pygame.image.load("textures/Label.png").convert_alpha(),
                                "Exit", round(35.0 * min(kx, ky)))
        self.ControlPanel = objects.Label(round(780.0 * kx), round(400.0 * ky), round(360.0 * kx), round(80.0 * ky),
                                pygame.image.load("textures/Label.png").convert_alpha(),
                                "Control Panel", round(35.0 * min(kx, ky)))
        self.Settings = objects.Label(round(780.0 * kx), round(520.0 * ky), round(360.0 * kx), round(80.0 * ky),
                                pygame.image.load("textures/Label.png").convert_alpha(),
                                "quadrocopter settings", round(35.0 * min(kx, ky)))
        self.TopPanel = objects.Panel(0, 0, round(1920.0 * kx), round(30.0 * ky),
                                (39, 38, 34))
        self.BottomPanel = objects.Panel(0, round(1050.0 * ky), round(1920.0 * kx), round(30.0 * ky),
                                (39, 38, 34))
        self.BG2 = objects.Panel(round(760.0 * kx), round(30.0 * ky), round(400.0 * kx), round(1020.0 * ky),
                                (39, 38, 34))
        self.BG1 = objects.Panel(round(730.0 * kx), round(30.0 * ky), round(460.0 * kx), round(1020.0 * ky),
                                (116, 105, 75))
        self.Photos = objects.Texture(round(38.0 * kx), round(134.0 * ky), round(623.0 * kx), round(819.0 * ky),
                                pygame.image.load("textures/Photos.png").convert_alpha())
        self.Camera = objects.Texture(round(79.0 * kx), round(101.0 * ky), round(214.0 * kx), round(214.0 * ky),
                                pygame.image.load("textures/Camera.png").convert_alpha())
    def mouseButtonDown(self, mouse_pos, ky):
        if self.ControlPanel.mouse_is_in(mouse_pos[0], mouse_pos[1]):
            self.ControlPanel.SetTexture(pygame.image.load("textures/Label_pressed.png").convert_alpha(), True,
                                         round(10.0 * ky))
            self.last_mouse_pos = mouse_pos
        if self.Settings.mouse_is_in(mouse_pos[0], mouse_pos[1]):
            self.Settings.SetTexture(pygame.image.load("textures/Label_pressed.png").convert_alpha(), True,
                                         round(10.0 * ky))
            self.last_mouse_pos = mouse_pos
        if self.Exit.mouse_is_in(mouse_pos[0], mouse_pos[1]):
            self.Exit.SetTexture(pygame.image.load("textures/Label_pressed.png").convert_alpha(), True,
                                         round(10.0 * ky))
            self.last_mouse_pos = mouse_pos
    def mouseButtomUp(self, mouse_pos):
        self.ControlPanel.SetTexture(pygame.image.load("textures/Label.png").convert_alpha())
        self.Settings.SetTexture(pygame.image.load("textures/Label.png").convert_alpha())
        self.Exit.SetTexture(pygame.image.load("textures/Label.png").convert_alpha())
        user = [True, False]
        if self.Exit.mouse_is_in(mouse_pos[0], mouse_pos[1]) and \
                self.Exit.mouse_is_in(self.last_mouse_pos[0], self.last_mouse_pos[1]):
            pygame.quit()
            sys.exit()
        if self.ControlPanel.mouse_is_in(mouse_pos[0], mouse_pos[1]) and \
            self.ControlPanel.mouse_is_in(self.last_mouse_pos[0], self.last_mouse_pos[1]):
            user[0] = False
        if self.Settings.mouse_is_in(mouse_pos[0], mouse_pos[1]) and \
                self.Settings.mouse_is_in(self.last_mouse_pos[0], self.last_mouse_pos[1]):
            user[0] = False
            user[1] = True
        return user
    def draw(self, window):
        self.BG1.draw(window)
        self.BG2.draw(window)
        self.Photos.draw(window)
        self.Camera.draw(window)
        self.Exit.draw(window)
        self.ControlPanel.draw(window)
        self.Settings.draw(window)
        self.TopPanel.draw(window)
        self.BottomPanel.draw(window)