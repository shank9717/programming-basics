# To make this function follow the LSP principle, we will follow this LSP requirements postulated by Steve Fenton:

# If the super-class (Employee) has a method that accepts a super-class type (Employee) parameter:
# Its sub-class(AverageEmployee) should accept as argument a super-class type (Employee type) or sub-class type(AverageEmployee type).

# If the super-class returns a super-class type (Employee):
# Its sub-class should return a super-class type (Employee type) or sub-class type(AverageEmployee).
# Now, we can re-implement get_grades function:

from typing import List


class Employee:
    current_salary = 10

    def __init__(self, name: str):
        self.name = name
        self.performance = 'Average'

    def get_grade(self):
        return f'{self} is a C grade employee'

    def __repr__(self):
        return f'{self.name}'


class AverageEmployee(Employee):
    pass


class GoodEmployee(AverageEmployee):
    def __init__(self, name: str):
        super().__init__(name)
        self.performance = 'Good'

    def get_grade(self) -> str:
        return f'{self} is a B grade employee'


class OutstandingEmployee(AverageEmployee):
    def __init__(self, name: str):
        super().__init__(name)
        self.performance = 'Outstanding'

    def get_grade(self) -> str:
        return f'{self} is an A grade employee'


def get_grades(employees: List[Employee]):
    for employee in employees:
        print(employee.get_grade())
