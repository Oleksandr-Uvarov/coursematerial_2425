class Car:
    def __init__(self):
        self.speed = 5

        
    @property
    def speed(self):
        print("test")
        return self.__speed
    
    @speed.setter
    def speed(self, kmh):
        if kmh > 180:
            raise ValueError("no")
        else:
            self.__speed = kmh


car = Car()
print(car.speed)