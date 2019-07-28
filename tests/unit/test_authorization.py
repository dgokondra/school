"""
This module contains tests for checking a work of login to the system.
"""

import pytest
from PyQt5 import QtCore

from package.config import Config
from package.controllers.authorization import LoginWindow


class TestLogin:
    """
    This class use to test login system of the project.
    """
    @pytest.mark.parametrize('login, password, message', [
        (Config.ACCOUNT['LOGIN'], Config.ACCOUNT['PASSWORD'], ''),
        ('login', Config.ACCOUNT['PASSWORD'], Config.MESSAGES['ERROR_LOGIN_MESSAGE']),
        (Config.ACCOUNT['LOGIN'], 'password', Config.MESSAGES['ERROR_LOGIN_MESSAGE']),
        ('', Config.ACCOUNT['PASSWORD'], Config.MESSAGES['ERROR_LOGIN_MESSAGE']),
        (Config.ACCOUNT['LOGIN'], '', Config.MESSAGES['ERROR_LOGIN_MESSAGE']),
        ('', '', Config.MESSAGES['ERROR_LOGIN_MESSAGE']),
    ])
    def test_login_to_the_system(self, qtbot, login_attempt, login, password, message, open_window):
        widget = login_attempt(open_window, login, password, LoginWindow)
        qtbot.mouseClick(widget.login_button, QtCore.Qt.LeftButton)
        assert widget.error_label.text() == message
