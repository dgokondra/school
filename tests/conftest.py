import pytest
from PyQt5 import QtTest


@pytest.fixture
def login_attempt(qtbot):
    def callback(test_login, test_password, widget_name):
        widget = widget_name()
        qtbot.addWidget(widget)
        widget.show()
        qtbot.wait_for_window_shown(widget)
        qtbot.keyClicks(widget.login_edit, test_login)
        qtbot.keyClicks(widget.password_edit, test_password)
        QtTest.QTest.qWait(3 * 400)
        return widget
    return callback


@pytest.fixture
def assert_login_attempt():
    def callback(widget, window):
        assert widget.current_window.isVisible()
        assert isinstance(widget.current_window, window)
        return widget
    return callback