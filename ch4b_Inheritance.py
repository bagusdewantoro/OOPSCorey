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


# Inheritance. Create Subclasses
class Developer(Employee):
    # change class variable
    raise_amt = 1.10

    # add init attribute
    def __init__(self, first, last, pay, prog_lang):
        # no need to copy the init attributes, just use super()
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

# help(Developer)

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# check whether inherint from what or not
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))
