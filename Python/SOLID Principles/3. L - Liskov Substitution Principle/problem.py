# Liskov Substitution Principle states :- Let q(x) be a property provable about objects of x of type T.
# Then q(y) should be provable for objects y of type S where S is a subtype of T.

# In simpler terms it means that a subclass, child or specialization of an object or class must be substitutable
# for its Parent or SuperClass.

# The aim of this principle is to ascertain that a sub-class can assume the place of its super-class without errors.
# If the code finds itself checking the type of class then, it must have violated this principle.

# We can take a variation of the Hike example in Open-Close Principle to demonstrate this:-
from typing import List


class Employee:
    current_salary = 10

    def __init__(self):
        self.performance = 'Average'


class AverageEmployee(Employee):
    pass


class GoodEmployee(AverageEmployee):
    def __init__(self):
        super().__init__()
        self.performance = 'Good'


class OutstandingEmployee(AverageEmployee):
    def __init__(self):
        super().__init__()
        self.performance = 'Outstanding'


def get_grades(employees: List[Employee]):
    for employee in employees:
        if isinstance(employee, AverageEmployee):
            print(f'{employee} is a C grade employee')
        if isinstance(employee, GoodEmployee):
            print(f'{employee} is a B grade employee')
        if isinstance(employee, OutstandingEmployee):
            print(f'{employee} is an A grade employee')
