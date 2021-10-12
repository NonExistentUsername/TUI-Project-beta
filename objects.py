import pygame
class Text:
    def __init__(self, center_x, center_y, text, size, color = (0, 0, 0), style = 'Bahnschrift', Center = True):
        self.x = center_x
        self.y = center_y
        self.text = text
        self.color = color
        self.myfont = pygame.font.SysFont(style, size)
        self.texture = self.myfont.render(text, True, color)
        if Center:
            info = self.texture.get_rect()
            self.x -= info.width // 2
            self.y -= info.height // 2
    def SetText(self, text):
        self.texture = self.myfont.render(text, True, self.color)
        self.text = text
    def draw(self, window):
        window.blit(self.texture, (self.x, self.y))
class Label:
    def __init__(self, x, y, width, height, texture, text = 'Label', size = 30):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.texture = pygame.transform.smoothscale(texture, (width, height))
        self.text = Text((2 * x + width) // 2,
                         (2 * y + height) // 2,
                         text,
                         size,
                         (0, 0, 0))
        self.pressed = False
    def SetTexture(self, texture, pressed = False, difference = 0):
        self.pressed = pressed
        self.difference = difference
        self.texture = pygame.transform.smoothscale(texture, (self.width, self.height))
    def draw(self, window):
        window.blit(self.texture, (self.x, self.y))
        if self.pressed:
            self.text.y += self.difference
        self.text.draw(window)
        if self.pressed:
            self.text.y -= self.difference
    def mouse_is_in(self, x, y):
        if self.x <= x and x <= self.x + self.width and self.y <= y and y <= self.y + self.height:
            return True
        else:
            return False
class Panel:
    def __init__(self, x, y, width, height, color = (0, 0, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
    def mouse_is_in(self, x, y):
        if self.x <= x and x <= self.x + self.width and self.y <= y and y <= self.y + self.height:
            return True
        else:
            return False
class TextBox:
    def __init__(self, center_x, center_y, text, size, color = (0, 0, 0), style = 'Bahnschrift'):
        self.text = Text(center_x, center_y, text, size, color, style)
        self.pressed = False
        self.last_key = '['
        self.timer = 20
    def Update(self, key):
        str = self.text.text
        if self.pressed:
            if key == '-':
                str = str[:len(str) - 1]
            else:
                if key == self.last_key:
                    if self.timer == 0:
                        str += key
                    else:
                        self.timer -= 1
                else:
                    str += key
                    self.last_key = key
                    self.timer = 20
            self.text.SetText(str)
    def draw(self, window):
        self.text.draw(window)
    def mouse_is_in(self, x, y):
        info = self.text.texture.get_rect()
        posx = self.text.x
        posy = self.text.y
        width = info.width
        height = info.height
        if posx <= x and x <= posx + width and posy <= y and y <= posy + height:
            return True
        else:
            return False
class Texture:
    def __init__(self, x, y, width, height, texture):
        self.x = x
        self.y = y
        if width != 0 or height != 0:
            self.texture = pygame.transform.smoothscale(texture, (width, height))
        else:
            self.texture = texture
    def draw(self, window):
        window.blit(self.texture, (self.x, self.y))
