class RegisterException(Exception):
    """
    General Exception class
    """

    def __init__(self, msg):
        super().__init__(self, msg)


class ValidationException(RegisterException):
    def __init__(self, msgs):
        """
         Initialise
         msg is a list of strings (errors)
        """
        self.__msgs = msgs

    @property
    def messages(self):
        return self.__msgs

    def __str__(self):
        return str(self.__msgs)