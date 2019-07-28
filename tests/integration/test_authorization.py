"""
This module contains tests for checking a work of login to the system.
"""

from PyQt5 import QtCore

from package.config import Config
from package.controllers.authorization import LoginWindow
from package.controllers.start import MainWindow


class TestLoginToTheSystem:
    """
    Тест, что при успешном логировании откроется главное окно, а при неуспешном - нет.
    """

    def test_successful_login(self, qtbot, login_attempt, assert_login_attempt, open_window):
        widget = login_attempt(open_window, Config.ACCOUNT['LOGIN'], Config.ACCOUNT['PASSWORD'], LoginWindow)
        assert_login_attempt(widget, LoginWindow)
        qtbot.mouseClick(widget.login_button, QtCore.Qt.LeftButton)
        assert_login_attempt(widget, MainWindow)

    def test_failure_login(self, qtbot, login_attempt, assert_login_attempt, open_window):
        widget = login_attempt(open_window, 'sdgfer', '23erff232g@#', LoginWindow)
        assert_login_attempt(widget, LoginWindow)
        qtbot.mouseClick(widget.login_button, QtCore.Qt.LeftButton)
        assert_login_attempt(widget, LoginWindow)
