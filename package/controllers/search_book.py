"""This module contains classes using to search need schoolbooks and fiction books in the database."""

from PyQt5.QtWidgets import *
from loguru import logger

from package.views.search_fictionbook_view import Ui_SearchFictionbookWindow
from package.views.search_schoolbook_view import Ui_SearchSchoolbookWindow


class SearchSchoolBookWindow(QDialog, Ui_SearchSchoolbookWindow):
    """The widget using to search current schoolbooks in the database."""
    @logger.catch
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class SearchFictionBookWindow(QDialog, Ui_SearchFictionbookWindow):
    """The widget using to search current fiction books in the database."""
    @logger.catch
    def __init__(self):
        super().__init__()
        self.setupUi(self)
