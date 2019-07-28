"""This module contains classes using to add schoolbooks and fiction books in the database."""

from PyQt5.QtWidgets import *
from loguru import logger

from package.views.add_fictionbook_view import Ui_AddFictionbookWindow
from package.views.add_schoolbook_view import Ui_AddSchoolbookWindow


class AddSchoolBookWindow(QDialog, Ui_AddSchoolbookWindow):
    """The widget using to add a schoolbook in the database."""
    @logger.catch
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class AddFictionBookWindow(QDialog, Ui_AddFictionbookWindow):
    """The widget using to add a fiction book in the database."""
    @logger.catch
    def __init__(self):
        super().__init__()
        self.setupUi(self)
