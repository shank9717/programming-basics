# So we simply split the class, we create another class that will handle the responsibility
# of storing an employee in a database:
# A common solution to this dilemma is to apply the Façade pattern

class Employee:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        pass


class EmployeeDB:
    def get_user(self, id) -> Employee:
        pass

    def save(self, employee: Employee) -> bool:
        pass

