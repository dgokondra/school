import pytest
from PyQt5 import QtTest


@pytest.fixture
def open_window(qtbot):
    def callback(window):
        widget = window()
        qtbot.addWidget(widget)
        widget.show()
        qtbot.wait_for_window_shown(widget)
        QtTest.QTest.qWait(3 * 200)
        return widget
    return callback


@pytest.fixture
def login_attempt(qtbot):
    def callback(open_window, test_login, test_password, widget_name):
        widget = open_window(widget_name)
        qtbot.keyClicks(widget.login_edit, test_login)
        qtbot.keyClicks(widget.password_edit, test_password)
        QtTest.QTest.qWait(3 * 200)
        return widget
    return callback


@pytest.fixture
def assert_login_attempt():
    def callback(widget, window):
        assert widget.current_window.isVisible()
        assert isinstance(widget.current_window, window)
        return widget
    return callback
