"""
This module contains tests for checking a window of selecting object for to add
to the database or to search in the database.
"""

import pytest
from PyQt5 import QtCore

from package.controllers.select_object import SelectAddingBookTypeWindow, SelectSearchingBookTypeWindow
from package.controllers.add_book import AddSchoolBookWindow, AddFictionBookWindow
from package.controllers.search_book import SearchSchoolBookWindow, SearchFictionBookWindow


class TestSelectObject:
    """
    This class use to test the window of select need object.
    """
    @pytest.mark.parametrize('window, radio_btn, parent', [
        (SelectAddingBookTypeWindow, 'schoolbookSelector', AddSchoolBookWindow),
        (SelectAddingBookTypeWindow, 'fictionbookSelector', AddFictionBookWindow),
        (SelectSearchingBookTypeWindow, 'schoolbookSelector', SearchSchoolBookWindow),
        (SelectSearchingBookTypeWindow, 'fictionbookSelector', SearchFictionBookWindow),
    ])
    def test_select_object(self, open_window, qtbot, window, radio_btn, parent):
        widget = open_window(window)
        assert widget.isVisible()
        qtbot.mouseClick(widget.__dict__[radio_btn], QtCore.Qt.LeftButton)
        qtbot.mouseClick(widget.selectBtn, QtCore.Qt.LeftButton)
        assert widget.isHidden()
        assert widget.selected_window is not None
        assert isinstance(widget.selected_window, parent)
        assert widget.selected_window.isVisible()
