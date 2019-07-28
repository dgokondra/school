"""This module contains some classes using to select need object and then opening it."""

from PyQt5.QtWidgets import *
from loguru import logger

from package.views.select_object_view import Ui_selectBookTypeWindow
from package.controllers.add_book import AddSchoolBookWindow, AddFictionBookWindow
from package.controllers.search_book import SearchSchoolBookWindow, SearchFictionBookWindow


class SelectBookTypeWindow(QDialog, Ui_selectBookTypeWindow):
    """The widget will open a need window which will use for the next operations."""
    @logger.catch
    def __init__(self, widget1: QDialog, widget2: QDialog):
        super().__init__()
        self.setupUi(self)
        self.selectBtn.clicked.connect(lambda x: self.open_new_window(widget1, widget2))
        self._selected_window = None

    @property
    def selected_window(self):
        return self._selected_window

    def open_new_window(self, schoolbook_widget: QDialog, fictionbook_widget: QDialog) -> None:
        """
        This method will open a widget after the usel selected need type of the book and clicked by the button.

        :param schoolbook_widget:  a widget open if user selected schoolbookSelector
        :param fictionbook_widget: a widget open if user selected fictionbookSelector
        :return:
        """
        if self.schoolbookSelector.isChecked():
            self._selected_window = schoolbook_widget()
        elif self.fictionbookSelector.isChecked():
            self._selected_window = fictionbook_widget()
        if self.selected_window:
            self.selected_window.show()
            self.close()


class SelectSearchingBookTypeWindow(SelectBookTypeWindow):
    """The widget will open a window to search need books"""
    def __init__(self):
        super().__init__(SearchSchoolBookWindow, SearchFictionBookWindow)


class SelectAddingBookTypeWindow(SelectBookTypeWindow):
    """The widget will open a window to add need books"""
    @logger.catch
    def __init__(self):
        super().__init__(AddSchoolBookWindow, AddFictionBookWindow)
