from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize
import sys, os
from more_buttons import modbutton
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from chess_gui import validate_move


class Ui_Dialog(QtWidgets.QMainWindow):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 700)
        self.turn = 0  # 0 = Black, 1 = White
        self.points = []
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 50, 700, 700))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.init_grid()
        self.add_buttons()
        self.render_board()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def init_grid(self):
        arr = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        grid = [['.'] * 8 for _ in range(8)]

        for i in range(8):
            grid[0][i] = 'BR' if arr[i] == 'R' else 'B' + arr[i]
            grid[1][i] = 'BP'
            grid[6][i] = 'WP'
            grid[7][i] = 'WR' if arr[i] == 'R' else 'W' + arr[i]
        self.grid = grid

    def add_buttons(self):
        self.button = {}
        for x in range(8):
            for y in range(8):
                btn = modbutton()
                btn.add_xy(x, y)
                btn.clicked.connect(self.called(x, y))
                self.gridLayout.addWidget(btn, x, y)
                btn.setFixedSize(QtCore.QSize(88, 88))
                color1 = "background-color:rgb(240,217,181)"
                color2 = "background-color:rgb(181,136,99)"
                btn.setStyleSheet(color1 if (x + y) % 2 == 0 else color2)
                self.button[(x, y)] = btn

    def render_board(self):
        for x in range(8):
            for y in range(8):
                piece = self.grid[x][y]
                btn = self.button[(x, y)]
                if piece != '.':
                    path = f"src/images/{piece}.png"
                    if os.path.exists(path):
                        btn.setIcon(QIcon(QPixmap(path)))
                        btn.setIconSize(QSize(70, 70))
                else:
                    btn.setIcon(QIcon())

    def called(self, x, y):
        def clicked():
            self.updated(x, y)
        return clicked

    def updated(self, x, y):
        if len(self.points) == 0:
            self.points.append((x, y))
        else:
            x1, y1 = self.points[0]
            x2, y2 = x, y
            moved = validate_move(self.grid, self.turn, x1, y1, x2, y2)
            if moved:
                self.turn = 1 - self.turn  # Switch turn
                self.render_board()
            self.points = []

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Chess Game"))


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())



