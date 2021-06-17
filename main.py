import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_loading_screen import Ui_LoadingScreen
from ui_main import Ui_MainWindow
from widgets import CircularProgress

counter = int(0)

class LoadingScreen(QMainWindow):
    def __init__(self):
        # Setup main loading screen

        QMainWindow.__init__(self)
        self.ui = Ui_LoadingScreen()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Create progress bar
        self.progress = CircularProgress()
        self.progress.width = 300
        self.progress.height = 300
        self.progress.value = 0
        self.progress.move(25, 25)
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.add_shadow(True)
        self.progress.font_size = 16
        self.progress.setParent(self.ui.centralwidget)
        self.progress.show()

        # Crete timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_status)
        self.timer.start(25)


        self.show()

    def update_status(self):
        global counter
        self.progress.set_value(counter)
        if counter >= 100:
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            self.close()
        counter += 1







class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoadingScreen()
    sys.exit(app.exec_())
