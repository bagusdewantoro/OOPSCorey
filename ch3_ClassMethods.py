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


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

"""
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# Use class variable
Employee.raise_amt = 1.05

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# Use class method
Employee.set_raise_amt(1.06)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# Use class method from through object
emp_1.set_raise_amt(1.07)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
"""

# new data based on string separated by hyphens
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# create object based on new data
first, last, pay = emp_str_1.split('-')
print(first, last, pay)
new_emp_1 = Employee(first, last, pay)

print(new_emp_1.email)
print(new_emp_1.pay)
print(new_emp_1.fullname())

# create object use CLASS METHOD
new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.email)
print(new_emp_2.pay)
print(new_emp_2.fullname())
