"""This module contains classes are parts of the main window current project"""

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from package.views.start_view import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """This class is a widget realizing a main window of the system"""
    def __init__(self):
        """initialising the instance of the main window"""
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
