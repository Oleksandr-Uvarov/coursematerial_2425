class Averager:
    def __init__(self):
        # self.__lst = []
        self.__sum = 0
        self.__count = 0

    def add(self, number):
        # self.__lst.append(number)
        self.__sum += number
        self.__count += 1
    

    def average(self):
        # return sum(self.__lst) / len(self.__lst)
        return self.__sum / self.__count

    
    def reset(self):
        # self.__lst = []
        self.__sum = 0
        self.__count = 0