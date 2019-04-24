class PrivateVariableAndFunction:
    def __init__(self):
        self.x = 10
        self.__y = 100

    def __test_private_method(self):
        print("I am a private method")
