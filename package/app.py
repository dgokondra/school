from package.controllers.authorization import LoginWindow


class Application(LoginWindow):
    """This class using to run the project"""
    def __init__(self, *args, **kwargs):
        """initialising the instance of the main window"""
        super().__init__(*args, **kwargs)
