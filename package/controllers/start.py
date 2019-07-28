"""This module contains classes are parts of the main window current project"""

import sys

from loguru import logger
from PyQt5.QtWidgets import QApplication, QMainWindow

from package.views.start_view import Ui_MainWindow
from package.controllers.help import HelpWindow
from package.controllers.excel import ExcelUnloader
from package.controllers.select_object import SelectAddingBookTypeWindow, SelectSearchingBookTypeWindow


class Toolbar:
    """This class sets behavior for all buttons in the toolbar of the main window."""

    def __init__(self, buttons_list):
        """

        :param buttons_list: the list of all buttons widgets in the toolbar
        """
        self._btns = buttons_list
        self._events = [self._search_book, self._add_book, self._unload_books, self._show_help, ]
        self._btn_event_mapper = dict(zip(self._btns, self._events))
        self._set_event_for_toolbar_element()
        self._selected_window = None

    @property
    def selected_window(self):
        return self._selected_window

    def _set_event_for_toolbar_element(self):
        """binds the widget with the event"""
        for btn, event in self._btn_event_mapper.items():
            btn.triggered.connect(event)

    def _open_window(self, log_message, opening_window):
        logger.info(log_message)
        self._selected_window = opening_window()
        if self.selected_window:
            self.selected_window.show()

    def _search_book(self):
        """opens the window for searching the books"""
        self._open_window('User wants to search need books', SelectSearchingBookTypeWindow)

    def _add_book(self):
        """opens the window for adding the book"""
        self._open_window('User wants to add a new books', SelectAddingBookTypeWindow)

    def _unload_books(self):
        """unloads all books from database to the excel file"""
        self._open_window('User wants to unload books to the excel file', ExcelUnloader)

    def _show_help(self):
        """opens the window containing the help information"""
        self._open_window('User wants to get help information', HelpWindow)


class MainWindow(QMainWindow, Ui_MainWindow):
    """This class is a widget realizing a main window of the system"""
    def __init__(self):
        """initialising the instance of the main window"""
        super().__init__()
        self.setupUi(self)

        self._toolbar_buttons = [
            self.search_book_btn, self.add_book_btn, self.unload_book_btn, self.help_btn, self.exit_btn,
        ]
        self.toolbar = self.set_toolbar_events(self._toolbar_buttons)

    def set_toolbar_events(self, btns):
        """creates the toolbar of the window"""
        return Toolbar(btns)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
