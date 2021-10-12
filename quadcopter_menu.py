import pygame
import objects
import some_functions
class menu:
    def __init__(self, kx, ky):
        self.h = objects.TextBox(round(1220.0 * kx), round(311.0 * ky), '0', round(30.0 * kx))
        self.focus = objects.TextBox(round(1220.0 * kx), round(411.0 * ky), '0', round(30.0 * kx))
        self.battery = objects.TextBox(round(1220.0 * kx), round(511.0 * ky), '0', round(30.0 * kx))
        self.battery_photo = objects.TextBox(round(1220.0 * kx), round(611.0 * ky), '0', round(30.0 * kx))
        self.battery_fly = objects.TextBox(round(1220.0 * kx), round(711.0 * ky), '0', round(30.0 * kx))
        self.h_background = objects.Panel(round(1200.0 * kx), round(295.0 * ky), round(90.0 * kx), round(35.0 * ky),
                                (222, 222, 222))
        self.focus_background = objects.Panel(round(1200.0 * kx), round(395.0 * ky), round(90.0 * kx), round(35.0 * ky),
                                (222, 222, 222))
        self.battery_background = objects.Panel(round(1200.0 * kx), round(495.0 * ky), round(90.0 * kx), round(35.0 * ky),
                                (222, 222, 222))
        self.battery_photo_background = objects.Panel(round(1200.0 * kx), round(595.0 * ky), round(90.0 * kx), round(35.0 * ky),
                                (222, 222, 222))
        self.battery_fly_background = objects.Panel(round(1200.0 * kx), round(695.0 * ky), round(90.0 * kx), round(35.0 * ky),
                                (222, 222, 222))
        self.TopPanel = objects.Panel(0, 0, round(1920.0 * kx), round(30.0 * ky),
                                (39, 38, 34))
        self.BottomPanel = objects.Panel(0, round(1050.0 * ky), round(1920.0 * kx), round(30.0 * ky),
                                (39, 38, 34))
        self.height_text = objects.Text(round(620.0 * kx), round(300.0 * ky), 'Maximum flight altitude(m)', round(30.0 * kx), Center = False)
        self.focus_text = objects.Text(round(620.0 * kx), round(400.0 * ky), 'The focal length of the lens(mm)', round(30.0 * kx), Center = False)
        self.battery_text = objects.Text(round(620.0 * kx), round(500.0 * ky), 'Battery charge(mAh)', round(30.0 * kx), Center = False)
        self.battery_photo_text = objects.Text(round(620.0 * kx), round(600.0 * ky), 'Battery charge for photo creation(mAh)', round(30.0 * kx), Center = False)
        self.battery_move_text = objects.Text(round(620.0 * kx), round(700.0 * ky),  'Battery charge for flying(mAh / m)', round(30.0 * kx), Center = False)
        self.BG2 = objects.Panel(round(610.0 * kx), round(30.0 * ky), round(700.0 * kx), round(1020.0 * ky),
                                (39, 38, 34))
        self.BG1 = objects.Panel(round(580.0 * kx), round(30.0 * ky), round(760.0 * kx), round(1020.0 * ky),
                                (116, 105, 75))
        self.Save = objects.Label(round(780.0 * kx), round(800.0 * ky), round(360.0 * kx), round(80.0 * ky),
                                pygame.image.load("textures/Label.png").convert_alpha(),
                                "Save", round(35.0 * min(kx, ky)))
        self.Photos = objects.Texture(round(38.0 * kx), round(134.0 * ky), round(623.0 * kx), round(819.0 * ky),
                                pygame.image.load("textures/Photos.png").convert_alpha())
        self.Camera = objects.Texture(round(79.0 * kx), round(101.0 * ky), round(214.0 * kx), round(214.0 * ky),
                                pygame.image.load("textures/Camera.png").convert_alpha())
        self.load()
    def mouseButtonDown(self, mouse_pos, ky):
        if self.Save.mouse_is_in(mouse_pos[0], mouse_pos[1]):
            self.Save.SetTexture(pygame.image.load("textures/Label_pressed.png").convert_alpha(), True,
                                         round(10.0 * ky))
            self.last_mouse_pos = mouse_pos
    def Update(self, key):
        self.h.Update(key)
        self.focus.Update(key)
        self.battery.Update(key)
        self.battery_photo.Update(key)
        self.battery_fly.Update(key)
    def removeFlags(self):
        self.h.pressed = False
        self.focus.pressed = False
        self.battery.pressed = False
        self.battery_photo.pressed = False
        self.battery_fly.pressed = False
    def mouseButtonUp(self, mouse_pos):
        self.removeFlags()
        self.Save.SetTexture(pygame.image.load("textures/Label.png").convert_alpha())
        if self.Save.mouse_is_in(mouse_pos[0], mouse_pos[1]) and \
            self.Save.mouse_is_in(self.last_mouse_pos[0], self.last_mouse_pos[1]):
            self.save(self.h, self.focus, self.battery, self.battery_photo, self.battery_fly)
        if self.h.mouse_is_in(mouse_pos[0], mouse_pos[1]):
            self.h.pressed = True
        if self.focus.mouse_is_in(mouse_pos[0], mouse_pos[1]):
            self.focus.pressed = True
        if self.battery.mouse_is_in(mouse_pos[0], mouse_pos[1]):
            self.battery.pressed = True
        if self.battery_photo.mouse_is_in(mouse_pos[0], mouse_pos[1]):
            self.battery_photo.pressed = True
        if self.battery_fly.mouse_is_in(mouse_pos[0], mouse_pos[1]):
            self.battery_fly.pressed = True
    def draw(self, window):
        self.Camera.draw(window)
        self.Photos.draw(window)
        window.blit(some_functions.convert_and_screenShotMake(window.copy()), (0, 0))
        self.BG1.draw(window)
        self.BG2.draw(window)
        self.height_text.draw(window)
        self.focus_text.draw(window)
        self.battery_text.draw(window)
        self.battery_photo_text.draw(window)
        self.battery_move_text.draw(window)
        self.h_background.draw(window)
        self.focus_background.draw(window)
        self.battery_background.draw(window)
        self.battery_photo_background.draw(window)
        self.battery_fly_background.draw(window)
        self.h.draw(window)
        self.focus.draw(window)
        self.battery.draw(window)
        self.battery_photo.draw(window)
        self.battery_fly.draw(window)
        self.TopPanel.draw(window)
        self.BottomPanel.draw(window)
        self.Save.draw(window)
    def load(self):
        f = open('info/settings.qs', 'r')
        a = []
        for line in f:
            if line[len(line) - 1] == '\n':
                line = line[:len(line) - 1]
            a.append(line)
        self.h.text.SetText(a[0])
        self.focus.text.SetText(a[1])
        self.battery.text.SetText(a[2])
        self.battery_photo.text.SetText(a[3])
        self.battery_fly.text.SetText(a[4])
        f.close()
    def save(self, h, focus, battery, battery_photo, battery_fly):
        f = open('info/settings.qs', 'w')
        f.write(h.text.text + '\n' + focus.text.text + '\n' + battery.text.text + '\n' + battery_photo.text.text + '\n' + battery_fly.text.text)
        f.close()