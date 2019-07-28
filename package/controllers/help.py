"""This module realizes a opening window with a manual of program"""


class HelpWindow:
    """The class contains widgets with a helpful information about the program."""
    def __init__(self):
        self.show()

    def show(self):
        print('Окно справки')

    def isVisible(self):
        return True
