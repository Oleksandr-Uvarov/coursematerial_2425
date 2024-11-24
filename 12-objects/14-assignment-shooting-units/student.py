class Unit:
    def __init__(self, health, armor, firepower):
        self.__armor = armor
        self.__firepower = firepower
        self.__health = health
        self.validation()

    def validation(self):
        if self.__armor < 0 or self.__firepower < 0 or self.__health < 0:
            raise ValueError()
        return True
    
    @property
    def armor(self):
        return self.__armor
    
    @property
    def firepower(self):
        return self.__firepower
    
    @property
    def health(self):
        return self.__health
    
    
    def shot_by(self, other):

        if (self.__health + self.__armor) - other.firepower < 0:
            self.__health = 0
         
        elif other.firepower < self.armor:
            return
        

        else:
            if other.firepower - self.__armor > 0:
                self.__health -= (other.firepower - self.__armor)






# unit = Unit(60, 50, 400)
# unit2 = Unit(100, 100, 400)

# unit = Unit(2, 2, 10)
# unit2 = Unit(50, 6, 10)

    # (50, 5, 10, 45),
    # (50, 6, 10, 46),
    # (50, 15, 10, 50),

unit = Unit(health=50, armor=5, firepower=9000)
unit2 = Unit(50, 5, 10)

unit = Unit(50, 6, 9000)
unit2 = Unit(50, 6, 10)

unit = Unit(50, 15, 9000)
unit2 = Unit(50, 15, 10)

unit = Unit(50, 6, 2)
unit2 = Unit(10, 10, 2)

unit = Unit(0, 0, 5)
unit2 = Unit(5, 0, 10)

print(unit.shot_by(unit2))
# print(unit2.shot_by(unit))