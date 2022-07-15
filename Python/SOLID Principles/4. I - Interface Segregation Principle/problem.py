# According to the Interface Segregation Principle, no code should be forced into methods
# that it does not depend on methods that it does not use. This principle, which is in line
# with the other principles of SOLID, facilitates abstraction, interpretation and development.

# Clients should not be forced to depend upon interfaces that they do not use.
# This principle deals with the disadvantages of implementing big interfaces.

# In the below example, by creating separate methods in base class (Employee) for different performance benefits,
# we are forcing each implementation class to implement all 3 methods, which breaks this principle.

class Employee:
    current_salary = 10

    def __init__(self):
        self.performance = 'Average'

    def average_performance_benefits(self):
        raise NotImplementedError()

    def good_performance_benefits(self):
        raise NotImplementedError()

    def outstanding_performance_benefits(self):
        raise NotImplementedError()


class AverageEmployee(Employee):

    def average_performance_benefits(self):
        return ['Foo']

    def good_performance_benefits(self):
        raise None

    def outstanding_performance_benefits(self):
        raise None


class GoodEmployee(AverageEmployee):
    def __init__(self):
        super().__init__()
        self.performance = 'Good'

    def average_performance_benefits(self):
        return None

    def good_performance_benefits(self):
        raise ['Foo', 'Bar']

    def outstanding_performance_benefits(self):
        raise None


class OutstandingEmployee(AverageEmployee):
    def __init__(self):
        super().__init__()
        self.performance = 'Outstanding'

    def average_performance_benefits(self):
        return None

    def good_performance_benefits(self):
        raise None

    def outstanding_performance_benefits(self):
        raise ['Foo', 'Bar', 'Max']

# The fix would be to create single generic method in the base interface , and let all sub-classes implement that.
