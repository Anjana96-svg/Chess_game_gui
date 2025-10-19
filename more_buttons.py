from PyQt5.QtWidgets import QPushButton

class modbutton(QPushButton):
    def add_xy(self, x, y):
        self.x, self.y = x, y

    def get_xy(self):
        return (self.x, self.y)


        