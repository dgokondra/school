"""This module is entrypoint to the system.

It contains logger using in the project, and a calling of the main window.
"""

import sys
from os.path import join

from PyQt5.QtWidgets import QApplication
from loguru import logger

from package.app import Application
from package.config import Config


logger.add(join(Config.PATHES['TO_LOG'], 'file_{time}.log'),
           format="{module} {name} {message}", level='DEBUG', rotation='5MB')


@logger.catch
def run_program():
    """runs the main window"""
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    app.exec_()
    logger.info('The work of the program was finished')


if __name__ == '__main__':
    run_program()
