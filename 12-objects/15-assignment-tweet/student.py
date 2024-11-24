class Tweet:
    def __init__(self, message, max_length):
        if max_length < 1:
            raise ValueError()
        
        self.__message = message
        self.__max_length = max_length

        if len(message) > max_length:
            self.__message = message[0:max_length]

    @property
    def message(self):
        return self.__message
    
    @message.setter
    def message(self, message):
        if len(message) > self.max_length:
            self.__message = message[0:self.max_length]
        else:
            self.__message = message

    
    @property
    def max_length(self):
        return self.__max_length
    

    @max_length.setter
    def max_length(self, new_length):
        if new_length < 1:
            raise ValueError()
        
        if len(self.__message) > new_length:
            self.__message = self.__message[0:new_length]
            self.__max_length = new_length
        else:
            self.__max_length = new_length


tweet = Tweet("abc", 1)
print(tweet.message)
tweet.max_length = 100
print(tweet.max_length)