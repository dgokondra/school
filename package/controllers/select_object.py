"""This module contains some classes using to select need object and then opening it."""


from PyQt5.QtWidgets import *

from package.views.select_object_view import Ui_selectBookTypeWindow


class SelectSearchingBookTypeWindow(QDialog, Ui_selectBookTypeWindow):
    """The widget will open a window to search need books"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class SelectAddingBookTypeWindow(QDialog, Ui_selectBookTypeWindow):
    """The widget will open a window to add need books"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
