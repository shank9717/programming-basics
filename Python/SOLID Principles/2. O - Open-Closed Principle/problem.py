# Software entities like classes, modules and functions etc., should be open for extension, but not for modification

# Assume we design a class to calculate the increment an employee receives based on his/her/their performance.
# An `Average` performer receives 5% hike on current salary.
# A `Good` performer receives 10% hike on current salary.


class Employee:
    current_salary = 10

    def __init__(self):
        self.performance = 'Average'


class Hike:
    def __init__(self, employee: Employee):
        self.employee = employee
        self.employee.current_salary = self.apply_increment()

    def apply_increment(self):
        if self.employee.performance == 'Average':
            return self.employee.current_salary + (self.employee.current_salary * 0.05)
        if self.employee.performance == 'Good':
            return self.employee.current_salary + (self.employee.current_salary * 0.1)

# This fails the OCP principle. If we wish to add a new performance slab and give increment based on that slab,
# you will see that a new logic will be added to the `apply_increment()` method.
# To make it follow the OCP principle, we will add a new class that will extend the Hike based on post
