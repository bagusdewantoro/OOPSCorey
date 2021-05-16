class Employee:

    # class variables
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    # regular method (automatically takes the class's INSTANCE with self argument)
    def fullname(self):
        return f'{self.first} {self.last}'

    # regular method (automatically takes the class's INSTANCE with self argument)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # CLASS METHOD take the CLASS as FIRST ARGUMENT
    # class method to set raise_amt variable
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # class method to create new object from new string data
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # STATIC METHODS used when we don't need to access the class / instance
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

import datetime
my_date = datetime.date(2021, 5, 17)
print

# use static method
print(Employee.is_workday(my_date))
