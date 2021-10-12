class UndoRedo:
    def __init__(self):
        self.c = 0
        self.actions = []
    def add(self, x):
        self.actions = self.actions[:self.c]
        self.actions.append(x)
        self.c = len(self.actions)
    def undo(self):
        if self.c == 1:
            return -1
        self.c -= 1
        return [self.actions[self.c - 1][0].copy(),
                self.actions[self.c - 1][1].copy(),
                self.actions[self.c - 1][2].copy(),
                self.actions[self.c - 1][3].copy(),
                self.actions[self.c - 1][4],
                self.actions[self.c - 1][5].copy()]
    def redo(self):
        if self.c >= len(self.actions):
            return -1
        self.c += 1
        return [self.actions[self.c - 1][0].copy(),
                self.actions[self.c - 1][1].copy(),
                self.actions[self.c - 1][2].copy(),
                self.actions[self.c - 1][3].copy(),
                self.actions[self.c - 1][4],
                self.actions[self.c - 1][5].copy()]