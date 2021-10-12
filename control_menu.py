import pygame
import objects
import controlmap
import some_functions
import undo_redo
class menu:
    def __init__(self, kx, ky):
        self.UndoRedo = undo_redo.UndoRedo()
        self.last_mouse_pos = [-1, -1]
        self.set_start_point = False
        self.set_area = False
        self.CreateTheWay = objects.Label(0, round(30.0 * ky), round(400.0 * kx), round(69.0 * ky),
                                pygame.image.load("textures/Label.png").convert_alpha(),
                                "Create Way", round(35.0 * min(kx, ky)))
        # self.SwapTool = objects.Label(0, round(130.0 * ky), round(400.0 * kx), round(99.0 * ky),
        #                         pygame.image.load("textures/Label.png").convert_alpha(),
        #                         "Swap Tool", round(35.0 * min(kx, ky)))
        self.MoveMap = objects.Label(0, round(100.0 * ky), round(400.0 * kx), round(69.0 * ky),
                                pygame.image.load("textures/Label.png").convert_alpha(),
                                "Move map", round(35.0 * min(kx, ky)))
        self.AddImage = objects.Label(0, round(170.0 * ky), round(400.0 * kx), round(69.0 * ky),
                                pygame.image.load("textures/Label.png").convert_alpha(),
                                "Add Image", round(35.0 * min(kx, ky)))
        self.Clear = objects.Label(0, round(240.0 * ky), round(400.0 * kx), round(69.0 * ky),
                                pygame.image.load("textures/Label.png").convert_alpha(),
                                "Clear", round(35.0 * min(kx, ky)))
        self.SetStartPoint = objects.Label(0, round(310.0 * ky), round(400.0 * kx), round(69.0 * ky),
                                pygame.image.load("textures/Label.png").convert_alpha(),
                                "Set Start Point", round(35.0 * min(kx, ky)))
        self.SetArea = objects.Label(0, round(380.0 * ky), round(400.0 * kx), round(69.0 * ky),
                                pygame.image.load("textures/Label.png").convert_alpha(),
                                "KeKYZ", round(35.0 * min(kx, ky)))
        self.Undo = objects.Label(0, round(450.0 * ky), round(400.0 * kx), round(69.0 * ky),
                                pygame.image.load("textures/Label.png").convert_alpha(),
                                "Undo", round(35.0 * min(kx, ky)))
        self.Redo = objects.Label(0, round(520.0 * ky), round(400.0 * kx), round(69.0 * ky),
                                pygame.image.load("textures/Label.png").convert_alpha(),
                                "Redo", round(35.0 * min(kx, ky)))
        self.AddRemovePoints = objects.Label(0, round(590.0 * ky), round(400.0 * kx), round(69.0 * ky),
                                pygame.image.load("textures/Label.png").convert_alpha(),
                                "Add/Remove points", round(35.0 * min(kx, ky)))
        self.LoadMap = objects.Label(0, round(660.0 * ky), round(400.0 * kx), round(69.0 * ky),
                                pygame.image.load("textures/Label.png").convert_alpha(),
                                "Load Map", round(35.0 * min(kx, ky)))
        self.SaveMap = objects.Label(0, round(730.0 * ky), round(400.0 * kx), round(69.0 * ky),
                                pygame.image.load("textures/Label.png").convert_alpha(),
                                "Save Map", round(35.0 * min(kx, ky)))
        self.UserMap = controlmap.Field(round(400.0 * kx), round(30.0 * ky), round(1520.0 * kx), round(1020.0 * ky))
        self.UserMapPanel = objects.Panel(round(400.0 * kx), round(30.0 * ky), round(1520.0 * kx), round(1020.0 * ky))
        self.ToolsPanel = objects.Panel(0, round(30.0 * ky), round(400.0 * kx), round(1020.0 * ky),
                                (116, 105, 75))
        self.TopPanel = objects.Panel(0, 0, round(1920.0 * kx), round(30.0 * ky),
                                (39, 38, 34))
        self.BottomPanel = objects.Panel(0, round(1050.0 * ky), round(1920.0 * kx), round(30.0 * ky),
                                (39, 38, 34))
        self.InAddImageMenu = False
        self.AddImageMenu = AddImageMenu(kx, ky)
        self.UndoRedo.add([self.UserMap.pos0.copy(),
                           self.UserMap.pos1.copy(),
                           self.UserMap.way.copy(),
                           self.UserMap.points.copy(),
                           self.UserMap.start_point,
                          self.UserMap.images.copy()])
    def mouseButtonDown(self, mouse_pos, ky, ToolAddPoint, MovingMap):
        if self.set_area:
            self.UserMap.set_pos0(mouse_pos)
        if self.InAddImageMenu:
            if self.AddImageMenu.Error:
                if self.AddImageMenu.ErrorOk.mouse_is_in(mouse_pos[0], mouse_pos[1]):
                    self.AddImageMenu.ErrorOk.SetTexture(pygame.image.load("textures/Label_pressed.png").convert_alpha(), True, round(10 * ky))
                    self.last_mouse_pos = mouse_pos

            else:
                if self.AddImageMenu.Exit.mouse_is_in(mouse_pos[0], mouse_pos[1]):
                    self.AddImageMenu.Exit.SetTexture(pygame.image.load("textures/Label_pressed.png").convert_alpha(), True, round(10 * ky))
                    self.last_mouse_pos = mouse_pos
                if self.AddImageMenu.Ok.mouse_is_in(mouse_pos[0], mouse_pos[1]):
                    self.AddImageMenu.Ok.SetTexture(pygame.image.load("textures/Label_pressed.png").convert_alpha(), True, round(10 * ky))
                    self.last_mouse_pos = mouse_pos
        else:
            if self.CreateTheWay.mouse_is_in(mouse_pos[0], mouse_pos[1]):
                self.CreateTheWay.SetTexture(pygame.image.load("textures/Label_pressed.png").convert_alpha(), True, round(10 * ky))
                self.last_mouse_pos = mouse_pos
            # if self.SwapTool.mouse_is_in(mouse_pos[0], mouse_pos[1]):
            #     self.SwapTool.SetTexture(pygame.image.load("textures/Label_pressed.png").convert_alpha(), True, round(10 * ky))
            #     self.last_mouse_pos = mouse_pos
            if self.MoveMap.mouse_is_in(mouse_pos[0], mouse_pos[1]):
                self.MoveMap.SetTexture(pygame.image.load("textures/Label_pressed.png").convert_alpha(), True, round(10 * ky))
                self.last_mouse_pos = mouse_pos
            if self.AddImage.mouse_is_in(mouse_pos[0], mouse_pos[1]):
                self.AddImage.SetTexture(pygame.image.load("textures/Label_pressed.png").convert_alpha(), True, round(10 * ky))
                self.last_mouse_pos = mouse_pos
            if self.Clear.mouse_is_in(mouse_pos[0], mouse_pos[1]):
                self.Clear.SetTexture(pygame.image.load("textures/Label_pressed.png").convert_alpha(), True, round(10 * ky))
                self.last_mouse_pos = mouse_pos
            if self.SetStartPoint.mouse_is_in(mouse_pos[0], mouse_pos[1]):
                self.SetStartPoint.SetTexture(pygame.image.load("textures/Label_pressed.png").convert_alpha(), True, round(10 * ky))
                self.last_mouse_pos = mouse_pos
            if self.SetArea.mouse_is_in(mouse_pos[0], mouse_pos[1]):
                self.SetArea.SetTexture(pygame.image.load("textures/Label_pressed.png").convert_alpha(), True, round(10 * ky))
                self.last_mouse_pos = mouse_pos
            if self.Undo.mouse_is_in(mouse_pos[0], mouse_pos[1]):
                self.Undo.SetTexture(pygame.image.load("textures/Label_pressed.png").convert_alpha(), True, round(10 * ky))
                self.last_mouse_pos = mouse_pos
            if self.Redo.mouse_is_in(mouse_pos[0], mouse_pos[1]):
                self.Redo.SetTexture(pygame.image.load("textures/Label_pressed.png").convert_alpha(), True, round(10 * ky))
                self.last_mouse_pos = mouse_pos
            if self.AddRemovePoints.mouse_is_in(mouse_pos[0], mouse_pos[1]):
                self.AddRemovePoints.SetTexture(pygame.image.load("textures/Label_pressed.png").convert_alpha(), True, round(10 * ky))
                self.last_mouse_pos = mouse_pos
            if self.LoadMap.mouse_is_in(mouse_pos[0], mouse_pos[1]):
                self.LoadMap.SetTexture(pygame.image.load("textures/Label_pressed.png").convert_alpha(), True, round(10 * ky))
                self.last_mouse_pos = mouse_pos
            if self.SaveMap.mouse_is_in(mouse_pos[0], mouse_pos[1]):
                self.SaveMap.SetTexture(pygame.image.load("textures/Label_pressed.png").convert_alpha(), True, round(10 * ky))
                self.last_mouse_pos = mouse_pos
            if self.UserMapPanel.mouse_is_in(mouse_pos[0], mouse_pos[1]) and not(ToolAddPoint) and not(self.set_start_point) and not(self.set_area):
                self.last_mouse_pos = mouse_pos
                MovingMap = True
        return MovingMap
    def mouseButtomUp(self, mouse_pos, ToolAddPoint, MovingMap, timer):
        if self.set_area:
            self.UserMap.set_pos1(mouse_pos)
        if self.InAddImageMenu:
            if self.AddImageMenu.Error:
                self.AddImageMenu.ErrorOk.SetTexture(pygame.image.load("textures/Label.png").convert_alpha())
                if self.AddImageMenu.ErrorOk.mouse_is_in(mouse_pos[0], mouse_pos[1]) and \
                        self.AddImageMenu.ErrorOk.mouse_is_in(self.last_mouse_pos[0], self.last_mouse_pos[1]):
                    self.AddImageMenu.Error = False
                    self.AddImageMenu.ErrorOk.SetTexture(pygame.image.load("textures/Label.png").convert_alpha())
            else:
                self.AddImageMenu.Exit.SetTexture(pygame.image.load("textures/Label.png").convert_alpha())
                self.AddImageMenu.Ok.SetTexture(pygame.image.load("textures/Label.png").convert_alpha())
                self.AddImageMenu.removeFlags()
                if self.AddImageMenu.Exit.mouse_is_in(mouse_pos[0], mouse_pos[1]) and \
                        self.AddImageMenu.Exit.mouse_is_in(self.last_mouse_pos[0], self.last_mouse_pos[1]):
                    self.InAddImageMenu = False
                if self.AddImageMenu.Ok.mouse_is_in(mouse_pos[0], mouse_pos[1]) and \
                        self.AddImageMenu.Ok.mouse_is_in(self.last_mouse_pos[0], self.last_mouse_pos[1]):
                    self.InAddImageMenu = False
                    self.AddImageMenu.Error = self.UserMap.addimage(int(self.AddImageMenu.x.text.text),
                                                                    int(self.AddImageMenu.y.text.text),
                                                                    self.AddImageMenu.image.text.text)
                    if self.AddImageMenu.Error:
                        self.InAddImageMenu = True
                    else:
                        self.UndoRedo.add([self.UserMap.pos0.copy(),
                                           self.UserMap.pos1.copy(),
                                           self.UserMap.way.copy(),
                                           self.UserMap.points.copy(),
                                           self.UserMap.start_point,
                                          self.UserMap.images.copy()])
                if self.AddImageMenu.x.mouse_is_in(mouse_pos[0], mouse_pos[1]):
                    self.AddImageMenu.x.pressed = True
                if self.AddImageMenu.y.mouse_is_in(mouse_pos[0], mouse_pos[1]):
                    self.AddImageMenu.y.pressed = True
                if self.AddImageMenu.h.mouse_is_in(mouse_pos[0], mouse_pos[1]):
                    self.AddImageMenu.h.pressed = True
                if self.AddImageMenu.image.mouse_is_in(mouse_pos[0], mouse_pos[1]):
                    self.AddImageMenu.image.pressed = True
        else:
            self.CreateTheWay.SetTexture(pygame.image.load("textures/Label.png").convert_alpha())
            # self.SwapTool.SetTexture(pygame.image.load("textures/Label.png").convert_alpha())
            self.MoveMap.SetTexture(pygame.image.load("textures/Label.png").convert_alpha())
            self.AddImage.SetTexture(pygame.image.load("textures/Label.png").convert_alpha())
            self.Clear.SetTexture(pygame.image.load("textures/Label.png").convert_alpha())
            self.SetStartPoint.SetTexture(pygame.image.load("textures/Label.png").convert_alpha())
            self.SetArea.SetTexture(pygame.image.load("textures/Label.png").convert_alpha())
            self.Undo.SetTexture(pygame.image.load("textures/Label.png").convert_alpha())
            self.Redo.SetTexture(pygame.image.load("textures/Label.png").convert_alpha())
            self.AddRemovePoints.SetTexture(pygame.image.load("textures/Label.png").convert_alpha())
            self.LoadMap.SetTexture(pygame.image.load("textures/Label.png").convert_alpha())
            self.SaveMap.SetTexture(pygame.image.load("textures/Label.png").convert_alpha())
            if self.CreateTheWay.mouse_is_in(mouse_pos[0], mouse_pos[1]) and \
                    self.CreateTheWay.mouse_is_in(self.last_mouse_pos[0], self.last_mouse_pos[1]):
                self.UserMap.GetTheWay()
                self.UndoRedo.add([self.UserMap.pos0.copy(),
                                   self.UserMap.pos1.copy(),
                                   self.UserMap.way.copy(),
                                   self.UserMap.points.copy(),
                                   self.UserMap.start_point,
                                  self.UserMap.images.copy()])
            if self.Clear.mouse_is_in(mouse_pos[0], mouse_pos[1]) and \
                    self.Clear.mouse_is_in(self.last_mouse_pos[0], self.last_mouse_pos[1]):
                self.UserMap.points.clear()
                self.UserMap.way.clear()
                if self.UserMap.start_point.x != 10000:
                    self.UserMap.way.append(self.UserMap.start_point)
                    self.UserMap.points.append(self.UserMap.start_point)
                self.UndoRedo.add([self.UserMap.pos0.copy(),
                                   self.UserMap.pos1.copy(),
                                   self.UserMap.way.copy(),
                                   self.UserMap.points.copy(),
                                   self.UserMap.start_point,
                                  self.UserMap.images.copy()])
            if self.SetStartPoint.mouse_is_in(mouse_pos[0], mouse_pos[1]) and \
                    self.SetStartPoint.mouse_is_in(self.last_mouse_pos[0], self.last_mouse_pos[1]):
                self.set_start_point = True
                self.set_area = False
                ToolAddPoint = False
                MovingMap = False
            if self.SetArea.mouse_is_in(mouse_pos[0], mouse_pos[1]) and \
                    self.SetArea.mouse_is_in(self.last_mouse_pos[0], self.last_mouse_pos[1]):
                self.set_area = True
                self.set_start_point = False
                ToolAddPoint = False
                MovingMap = False
            # if self.SwapTool.mouse_is_in(mouse_pos[0], mouse_pos[1]) and \
            #         self.SwapTool.mouse_is_in(self.last_mouse_pos[0], self.last_mouse_pos[1]):
            #     if ToolAddPoint:
            #         ToolAddPoint = False
            #         self.set_start_point = False
            #         self.set_area = False
            #     else:
            #         ToolAddPoint = True
            #         self.set_start_point = False
            #         self.set_area = False
            #     self.set_start_point = False
            if self.MoveMap.mouse_is_in(mouse_pos[0], mouse_pos[1]) and \
                    self.MoveMap.mouse_is_in(self.last_mouse_pos[0], self.last_mouse_pos[1]):
                ToolAddPoint = False
                self.set_start_point = False
                self.set_area = False
                self.set_start_point = False
            if self.AddRemovePoints.mouse_is_in(mouse_pos[0], mouse_pos[1]) and \
                    self.AddRemovePoints.mouse_is_in(self.last_mouse_pos[0], self.last_mouse_pos[1]):
                ToolAddPoint = True
                self.set_start_point = False
                self.set_area = False
                self.set_start_point = False
            if self.UserMapPanel.mouse_is_in(mouse_pos[0], mouse_pos[1]):
                if self.set_start_point:
                    self.UserMap.set_start_point(mouse_pos[0], mouse_pos[1])
                    self.UndoRedo.add([self.UserMap.pos0.copy(),
                                       self.UserMap.pos1.copy(),
                                       self.UserMap.way.copy(),
                                       self.UserMap.points.copy(),
                                       self.UserMap.start_point,
                                      self.UserMap.images.copy()])
                elif ToolAddPoint and timer == 0:
                    self.UserMap.addpoint(mouse_pos[0], mouse_pos[1])
                    self.UndoRedo.add([self.UserMap.pos0.copy(),
                                       self.UserMap.pos1.copy(),
                                       self.UserMap.way.copy(),
                                       self.UserMap.points.copy(),
                                       self.UserMap.start_point,
                                      self.UserMap.images.copy()])
                else:
                    MovingMap = False
            if self.AddImage.mouse_is_in(mouse_pos[0], mouse_pos[1]) and \
                    self.AddImage.mouse_is_in(self.last_mouse_pos[0], self.last_mouse_pos[1]):
                self.InAddImageMenu = True
            if self.Undo.mouse_is_in(mouse_pos[0], mouse_pos[1]) and \
                    self.Undo.mouse_is_in(self.last_mouse_pos[0], self.last_mouse_pos[1]):
                    x = self.UndoRedo.undo()
                    if x != -1:
                        self.UserMap.pos0 = x[0]
                        self.UserMap.pos1 = x[1]
                        self.UserMap.way = x[2]
                        self.UserMap.points = x[3]
                        self.UserMap.start_point = x[4]
                        self.UserMap.images = x[5]
            if self.Redo.mouse_is_in(mouse_pos[0], mouse_pos[1]) and \
                    self.Redo.mouse_is_in(self.last_mouse_pos[0], self.last_mouse_pos[1]):
                    x = self.UndoRedo.redo()
                    if x != -1:
                        self.UserMap.pos0 = x[0]
                        self.UserMap.pos1 = x[1]
                        self.UserMap.way = x[2]
                        self.UserMap.points = x[3]
                        self.UserMap.start_point = x[4]
                        self.UserMap.images = x[5]
            if self.SaveMap.mouse_is_in(mouse_pos[0], mouse_pos[1]) and \
                    self.SaveMap.mouse_is_in(self.last_mouse_pos[0], self.last_mouse_pos[1]):
                self.save()
            if self.LoadMap.mouse_is_in(mouse_pos[0], mouse_pos[1]) and \
                    self.LoadMap.mouse_is_in(self.last_mouse_pos[0], self.last_mouse_pos[1]):
                self.load()
        return [ToolAddPoint, MovingMap]
    def draw(self, window):
        self.UserMap.draw(window)
        self.TopPanel.draw(window)
        self.BottomPanel.draw(window)
        self.ToolsPanel.draw(window)
        self.CreateTheWay.draw(window)
        # self.SwapTool.draw(window)
        self.MoveMap.draw(window)
        self.AddImage.draw(window)
        self.Clear.draw(window)
        self.SetStartPoint.draw(window)
        self.SetArea.draw(window)
        self.Undo.draw(window)
        self.Redo.draw(window)
        self.AddRemovePoints.draw(window)
        self.LoadMap.draw(window)
        self.SaveMap.draw(window)
        if self.InAddImageMenu:
            self.AddImageMenu.draw(window)
    def load(self):
        f = open('info/qwerty.txt', 'r')
        self.UserMap.points = []
        self.UserMap.way = []
        i = f.readline()
        start_x = int(i)
        i = f.readline()
        start_y = int(i)
        self.UserMap.start_point.x = start_x
        self.UserMap.start_point.y = start_y
        i = f.readline()
        while i != '-1\n':
            x = int(i)
            i = f.readline()
            y = int(i)
            if x != start_x and y != start_y:
                self.UserMap.points.append(controlmap.Point(x, y))
            else:
                self.UserMap.points.append(self.UserMap.start_point)
            i = f.readline()
        i = f.readline()
        while i != '-1\n':
            x = int(i)
            i = f.readline()
            y = int(i)
            # if x != start_x and y != start_y:
            self.UserMap.way.append(controlmap.Point(x, y))
            # else:
            #     self.UserMap.way.append(self.UserMap.start_point)
            i = f.readline()
        f.close()
    def save(self):
        f = open('info/qwerty.txt', 'w')
        f.write(str(self.UserMap.start_point.x) + '\n' + str(self.UserMap.start_point.y) + '\n')
        for t in self.UserMap.points:
            f.write(str(t.x) + '\n' + str(t.y) + '\n')
        f.write('-1\n')
        for t in self.UserMap.way:
            f.write(str(t.x) + '\n' + str(t.y) + '\n')
        f.write('-1\n')
        f.close()
class AddImageMenu:
    def __init__(self, kx, ky):
        self.last_mouse_pos = [-1, -1]
        self.BG1 = objects.Panel(round(630.0 * kx), round(263.0 * ky), round(660.0 * kx), round(498.0 * ky), (116, 105, 75))
        self.BG2 = objects.Panel(round(660.0 * kx), round(278.0 * ky), round(600.0 * kx), round(468.0 * ky), (39, 38, 34))
        self.Exit = objects.Label(round(1005.0 * kx), round(610.0 * ky), round(189.0 * kx), round(98.0 * ky),
                                pygame.image.load("textures/Label.png").convert_alpha(),
                                "Exit")
        self.Ok = objects.Label(round(730.0 * kx), round(609.0 * ky), round(189.0 * kx), round(98.0 * ky),
                                pygame.image.load("textures/Label.png").convert_alpha(),
                                "OK")
        self.x = objects.TextBox(round(699.0 * kx), round(330.0 * ky), "0", round(30.0 * min(kx, ky)))
        self.y = objects.TextBox(round(699.0 * kx), round(410.0 * ky), "0", round(30.0 * min(kx, ky)))
        self.h = objects.TextBox(round(999.0 * kx), round(410.0 * ky), "0", round(30.0 * min(kx, ky)))
        self.image = objects.TextBox(round(699.0 * kx), round(492.0 * ky), "0", round(30.0 * min(kx, ky)))
        self.Error = False
        self.ErrorMenu = objects.Panel(round(641.0 * kx), round(286.0 * ky), round(636.0 * kx), round(237.0 * ky),
                                (30, 220, 25))
        self.ErrorOk = objects.Label(round(799.0 * kx), round(414.0 * ky), round(322.0 * kx), round(84.0 * ky),
                                pygame.image.load("textures/Label.png").convert_alpha(),
                                "Ok")
    def Update(self, keys):
        self.x.Update(some_functions.GetNumber(keys))
        self.y.Update(some_functions.GetNumber(keys))
        self.h.Update(some_functions.GetNumber(keys))
        self.image.Update(some_functions.GetKey(keys))
    def removeFlags(self):
        self.x.pressed = False
        self.y.pressed = False
        self.h.pressed = False
        self.image.pressed = False
    def draw(self, window):
        self.BG1.draw(window)
        self.BG2.draw(window)
        self.x.draw(window)
        self.y.draw(window)
        self.h.draw(window)
        self.image.draw(window)
        self.Exit.draw(window)
        self.Ok.draw(window)
        if self.Error:
            self.ErrorMenu.draw(window)
            self.ErrorOk.draw(window)