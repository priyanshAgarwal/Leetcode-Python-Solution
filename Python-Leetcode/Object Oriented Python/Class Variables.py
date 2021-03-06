# cook your dish here

"""
https://www.youtube.com/watch?v=BJ-VvGyQxho
"""


class Employee:

    raise_amount=1.04
    static number_of_employee=0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.number_of_employee+=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        return self.pay*self.raise_amount

Employee.raise_amount=1.08

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(f'Salary is $ {emp_1.pay}')
print(f'Amount Raise % {emp_1.raise_amount}')
print(f'New salary after Raise is $ {emp_1.apply_raise()}')

print(f'Salary is $ {emp_2.pay}')
emp_2.raise_amount=1.05
print(f'Amount Raise % {emp_2.raise_amount}')
print(f'New salary after Raise is $ {emp_2.apply_raise()}')


print(f'Number of Employee are {emp_2.number_of_employee}')
emp_2.number_of_employee=5 
print(f'Number of Employee are {emp_2.number_of_employee}')

print(f'Number of Employee are {Employee.number_of_employee}')
Employee.number_of_employee=5
print(f'Number of Employee are {Employee.number_of_employee}')

