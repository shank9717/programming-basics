# The idea of Single Responsibility Principle is that we keep classes very simple. Each class should perform a
# single functionality, and we should split any class that performs multiple functionalities accordingly.

# Below is a class which has two responsibilities.
from __future__ import annotations

class Employee:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def save(self, employee: 'Employee') -> bool:
        pass

# Here, Employee class stores information about a single employee, but also has additional functionality of saving
# employee details into DB. Hence it breaks Single Responsibility Principle.