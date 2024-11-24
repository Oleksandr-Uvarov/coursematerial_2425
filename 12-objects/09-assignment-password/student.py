class Password:
    def __init__(self, password):
        self.__password = password


    def verify(self, password):
        return self.__password == password
    

password = Password("214142")
print(password.verify("23"))
print(password.verify("214142"))