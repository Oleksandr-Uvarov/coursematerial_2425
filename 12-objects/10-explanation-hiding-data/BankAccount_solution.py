class BankAccount:

    def __init__(self,holder,number):
        self.holder = holder
        self.__number = number
        self.balance = -10900

    @property
    def number(self):
        return self.__number
    
    @property
    def balance(self):
        return self.__balance
    
    @number.setter
    def number(self,value):
        raise ValueError("Pass by the office")
    
    @balance.setter
    def balance(self,value):
        if not isinstance(value,int) or value < 0:
            raise ValueError("Balance should be a positive integer")
        self.__balance = value
    
    def deposit(self,amount):
        if not isinstance(amount,int) or amount < 0:
            raise ValueError("Invalid")
        self.__balance += amount

    def withdraw(self,amount):
        if not isinstance(amount,int) or amount > self.__balance:
            raise ValueError("Insufficient")
        self.__balance -= amount

    def transfer(self,other,amount):
        if not isinstance(other,BankAccount):
            raise ValueError("This is not a Bank Account")
        self.withdraw(amount)
        other.deposit(amount)

    def info(self):
        return f"Account '{self.holder}' - € {self.balance}"
    
mine = BankAccount("Sophie",123)
yours = BankAccount("Jef",345)

# mine.deposit(1000)
# mine.transfer(yours,200)
# yours.withdraw(100)

print(mine.info())
print(yours.info())