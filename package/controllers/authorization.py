"""
The code contains the login window. A user input login and password to login in the system.

"""
import sys

from PyQt5.QtWidgets import QDialog, QApplication
from loguru import logger

from package.views.authorization_view import Ui_Dialog
from package.config import Config
from package.controllers.start import MainWindow


class LoginWindow(QDialog, Ui_Dialog):
    """This class is a widget to login in the system"""
    @logger.catch
    def __init__(self):
        """initialising the instance of the window to login in the system"""
        super().__init__()
        self.setupUi(self)
        logger.info('The login window is open')
        self.current_window = self
        self.login_button.clicked.connect(lambda: self.sign_in())

    @logger.catch
    def sign_in(self) -> None:
        """
        Checking a user account for the login to the system.

        :return:
        """
        login = self.login_edit.text()
        password = self.password_edit.text()
        if login == Config.ACCOUNT['LOGIN'] and password == Config.ACCOUNT['PASSWORD']:
            self.current_window = MainWindow()
            self.close()
            logger.success('The user success login to the system!')
            self.current_window.show()
        else:
            self.error_label.setText(Config.MESSAGES['ERROR_LOGIN_MESSAGE'])
            logger.error(f'Incorrect account information: login="{login}", password="{password}"')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    app.exec_()
