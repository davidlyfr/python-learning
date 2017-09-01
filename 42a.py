# experiment space
class Customer(object):
     """A customer of ABC Bank with a checking account. Customers have the 
       following properties:
     Attributes:
     name: a string 
     balance: floating balance of their account
     """
    
    def __init__(self, name, balance=0.0):
        """Return a customer object whose name is *name* and starting
           balance is *balance*."""
        self.name = name
        self.balance = balance
    
    def withdraw(self, amount):
        """" return the balance remaining after withdrawing amount"""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance--sorry')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """return the balance remaining after depositing amount"""
        self.balance += amount
        return self.balance, name

addition = deposit("David", 101.0)
print addition
