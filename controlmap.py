import pygame
import math
import objects
import getTheWay
class Point:
    def __init__(self, x, y, radius = 24, color = (0, 0, 0)):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
    def SetColor(self, color):
        self.color = color
    def draw(self, window, scale = 1):
        surf = pygame.Surface((round(2.0 * (self.radius / scale)), round(2.0 * (self.radius / scale)))).convert_alpha()
        surf.fill((0, 0, 0, 0))
        pygame.draw.circle(surf, self.color, (round(self.radius / scale), round(self.radius / scale)), round(self.radius / scale))
        surf = pygame.transform.smoothscale(surf, (round(self.radius / (2.0 * scale)), round(self.radius / (2.0 * scale))))
        window.blit(surf, (self.x - round(self.radius / (4.0 * scale)), self.y - round(self.radius / (4.0 * scale))))
class Field:
    points = []
    way = []
    images = []
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.center_x = (2 * x + width) // 2
        self.center_y = (2 * y + height) // 2
        self.width = width * 2
        self.height = height * 2
        self.scale = 0.5
        self.start_point = Point(10000, 10000, color=(255, 0, 0))
        self.xadd = 0
        self.yadd = 0
        self.pos = -1
        self.pos0 = [10000, 10000]
        self.pos1 = [10000, 10000]
    def set_pos0(self, mouse_pos):
        x = mouse_pos[0]
        y = mouse_pos[1]
        self.pos0 = [round((x - (self.center_x - (self.width * self.scale ) / 2) - self.xadd) / self.scale),
                     round((y - (self.center_y - (self.height * self.scale) / 2) - self.yadd) / self.scale)]
    def set_pos1(self, mouse_pos):
        x = mouse_pos[0]
        y = mouse_pos[1]
        self.pos1 = [round((x - (self.center_x - (self.width * self.scale ) / 2) - self.xadd) / self.scale),
                     round((y - (self.center_y - (self.height * self.scale) / 2) - self.yadd) / self.scale)]
    def set_start_point(self, x, y):
        if (x - (self.center_x - (self.width * self.scale) / 2) - self.xadd) / self.scale >= 0 and \
                (x - (self.center_x - (self.width * self.scale) / 2) - self.xadd) / self.scale <= self.width and \
                (y - (self.center_y - (self.height * self.scale) / 2) - self.yadd) / self.scale >= 0 and \
                (y - (self.center_y - (self.height * self.scale) / 2) - self.yadd) / self.scale <= self.height:
            if self.start_point.x == 10000 and self.start_point.y == 10000:
                self.start_point = Point(round((x - (self.center_x - (self.width * self.scale ) / 2) - self.xadd) / self.scale),
                                        round((y - (self.center_y - (self.height * self.scale) / 2) - self.yadd) / self.scale), color = (255, 0, 0))
                self.points.append(self.start_point)
            else:
                index = self.points.index(self.start_point)
                self.start_point = Point(
                    round((x - (self.center_x - (self.width * self.scale) / 2) - self.xadd) / self.scale),
                    round((y - (self.center_y - (self.height * self.scale) / 2) - self.yadd) / self.scale),
                    color=(255, 0, 0))
                if len(self.way) == len(self.points):
                    self.way.pop(index)
                self.points[index] = self.start_point
    def addpoint(self, x, y):
        if (x - (self.center_x - (self.width * self.scale) / 2) - self.xadd) / self.scale >= 0 and \
                (x - (self.center_x - (self.width * self.scale) / 2) - self.xadd) / self.scale <= self.width and \
                (y - (self.center_y - (self.height * self.scale) / 2) - self.yadd) / self.scale >= 0 and \
                (y - (self.center_y - (self.height * self.scale) / 2) - self.yadd) / self.scale <= self.height:
            if self.pos != -1:
                if self.pos < len(self.way):
                    del self.way[self.pos]
                try:
                    if self.pos == self.points.index(self.start_point):
                        self.start_point.x = 10000
                        self.start_point.y = 10000
                        # print("DELETED START POINT")
                except ValueError:
                    1
                    # print("CANT FIND START POINT")
                del self.points[self.pos]
                self.pos = -1
            else:
                self.points.append(Point(round((x - (self.center_x - (self.width * self.scale ) / 2) - self.xadd) / self.scale),
                                    round((y - (self.center_y - (self.height * self.scale) / 2) - self.yadd) / self.scale)))
    def addscale(self, difference):
        self.scale += difference
        self.scale = max(self.scale, 0.1)
        self.scale = min(self.scale, 1.2)
    def addposition(self, addx, addy):
        self.xadd += addx
        self.yadd += addy
    def addimage(self, x, y, path):
        try:
            self.images.append(objects.Texture(x, y, 0, 0, pygame.image.load(path).convert()))
            return False
        except pygame.error:
            return True
    def GetTheWay(self):
        self.way = getTheWay.getTheWay(self.points.copy())
        self.points = self.way.copy()
    def draw(self, window):
        screen_mouse_pos = pygame.mouse.get_pos()
        mouse_pos_x = round((screen_mouse_pos[0] - (self.center_x - (self.width * self.scale ) / 2) - self.xadd) / self.scale)
        mouse_pos_y = round((screen_mouse_pos[1] - (self.center_y - (self.height * self.scale) / 2) - self.yadd) / self.scale)
        self.center_x += self.xadd
        self.center_y += self.yadd
        surf = pygame.Surface((self.width, self.height))
        surf.fill((255, 255, 255))
        for image in self.images:
            image.draw(surf)
        i = 0
        self.pos = -1
        for point in self.points:
            if math.sqrt(((point.x - mouse_pos_x) ** 2) + ((point.y - mouse_pos_y) ** 2)) <= point.radius / (4.0 * self.scale):
                color = point.color
                point.SetColor((255, 0, 0))
                point.draw(surf, self.scale)
                self.pos = i
                point.SetColor(color)
            else:
                point.draw(surf, self.scale)
            i += 1
        #self.start_point.draw(surf, self.scale)
        pygame.draw.aaline(surf, (255, 0, 0), (self.pos0[0], self.pos0[1]), (self.pos0[0], self.pos1[1]))
        pygame.draw.aaline(surf, (255, 0, 0), (self.pos0[0], self.pos0[1]), (self.pos1[0], self.pos0[1]))
        pygame.draw.aaline(surf, (255, 0, 0), (self.pos1[0], self.pos0[1]), (self.pos1[0], self.pos1[1]))
        pygame.draw.aaline(surf, (255, 0, 0), (self.pos0[0], self.pos1[1]), (self.pos1[0], self.pos1[1]))
        if len(self.way) > 0:
            for i in range(len(self.way) - 1):
                pygame.draw.aaline(surf, (200, 0, 200), (self.way[i].x, self.way[i].y), (self.way[i + 1].x, self.way[i + 1].y))
            pygame.draw.aaline(surf, (200, 0, 200), (self.way[0].x, self.way[0].y), (self.way[len(self.way) - 1].x, self.way[len(self.way) - 1].y))
        surf = pygame.transform.smoothscale(surf, (round(self.width * self.scale), round(self.height * self.scale)))
        window.blit(surf, (round(self.center_x - (self.width * self.scale) / 2.0),
                           round(self.center_y - (self.height * self.scale) / 2.0)))
        self.center_x -= self.xadd
        self.center_y -= self.yadd

