"""This module is the main configuration file"""
from os.path import join, dirname


class Config:
    """All settings of the project are attributes this class."""
    ACCOUNT = {
        'LOGIN': '1',  # This will be user login
        'PASSWORD': '1',  # This will be user password
    }
    MESSAGES = {
        'ERROR_LOGIN_MESSAGE': 'Неправильные логин/пароль',
    }
    PATHES = {
        'TO_LOG': join(dirname(dirname(__file__)), 'logs'),
    }
