class Employee:
    current_salary = 10

    def __init__(self):
        self.performance = 'Average'


class Hike:
    def __init__(self, employee: Employee):
        self.employee = employee
        self.employee.current_salary = self.apply_increment()

    def apply_increment(self) -> float:
        return self.employee.current_salary + (self.employee.current_salary * 0.05)

class AveragePerformerHike(Hike):
    pass

class GoodPerformerHike(Hike):
    def apply_increment(self):
        self.employee.current_salary += (self.employee.current_salary * 0.1)

class OutstandingPerformerHike(GoodPerformerHike):
    def apply_increment(self):
        self.employee.current_salary += (self.employee.current_salary * 0.2)

# Here, existing class has not been modified, but instead we have extended the base class to handle new scenarios