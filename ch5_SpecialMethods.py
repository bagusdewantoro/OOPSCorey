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


    # Special / Magic / Dunder Methods
    # representation of the object, for debugging, etc
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    # readable representation of the object
    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other_emp):
        return self.pay + other_emp.pay

    def __len__(self):
        return len(self.fullname())



emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)


print(1 + 2)
# in background :
print(int.__add__(1, 2))

print('a' + 'b')
# in background :
print(str.__add__('a', 'b'))

print(len('test'))
# in background :
print('test'.__len__())


print(emp_1.__repr__())
print(emp_1.__str__())

print(emp_1)
print(emp_1 + emp_2)
print(len(emp_1))
