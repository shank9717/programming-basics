from typing import List


class Employee:
    current_salary = 10

    def __init__(self):
        self.performance = 'Average'

    def performance_benefits(self):
        raise NotImplementedError()


class AverageEmployee(Employee):
    def performance_benefits(self) -> List:
        return ['Foo']


class GoodEmployee(AverageEmployee):
    def __init__(self):
        super().__init__()
        self.performance = 'Good'

    def performance_benefits(self) -> List:
        return ['Foo', 'Bar']


class OutstandingEmployee(AverageEmployee):
    def __init__(self):
        super().__init__()
        self.performance = 'Outstanding'

    def performance_benefits(self) -> List:
        return ['Foo', 'Bar', 'Max']
