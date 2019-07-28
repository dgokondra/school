import pytest
from PyQt5 import QtTest

from package.controllers.start import MainWindow
from package.controllers.help import HelpWindow
from package.controllers.excel import ExcelUnloader
from package.controllers.select_object import SelectSearchingBookTypeWindow, SelectAddingBookTypeWindow


@pytest.fixture
def check_toolbar(qtbot):
    def callback(window):
        widget = window()
        qtbot.addWidget(widget)
        widget.show()
        qtbot.wait_for_window_shown(widget)
        QtTest.QTest.qWait(3 * 200)
        return widget
    return callback


class TestToolbar:
    """
    This class use to test toolbar in the main window of program.
    """
    @pytest.mark.parametrize('button, parent', [
        ('add_book_btn', SelectAddingBookTypeWindow), ('search_book_btn', SelectSearchingBookTypeWindow),
        ('unload_book_btn', ExcelUnloader), ('help_btn', HelpWindow)
    ])
    def test_elements_toolbar(self, check_toolbar, button, parent):
        """test: the elements of the toolbar correct open need windows"""
        widget = check_toolbar(MainWindow)
        widget.__dict__[button].trigger()
        assert widget.isVisible()
        assert widget.toolbar.selected_window is not None
        assert isinstance(widget.toolbar.selected_window, parent)
        assert widget.toolbar.selected_window.isVisible()

    def test_close_window_from_toolbar(self, qtbot, check_toolbar):
        """test: to test the button for closing the main window"""
        button = 'exit_btn'
        widget = check_toolbar(MainWindow)
        widget.__dict__[button].trigger()
        assert widget.isHidden()