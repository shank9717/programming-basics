# Dependency Inversion Principle
# Dependency should be on abstractions not concretions
# A. High-level modules should not depend upon low-level modules. Both should depend upon abstractions.
# B. Abstractions should not depend on details. Details should depend upon abstractions.

# There comes a point in software development where our app will be largely composed of modules.
# When this happens, we have to clear things up by using dependency injection.
# High-level components depending on low-level components to function.

# Consider below example where we are saving employee info into a DB.


class PostgresDB:
    def __init__(self, ip: str, port: int, username: str, password: str, db: str):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.db = db
        self.connect()

    def connect(self):
        pass

    def save(self, obj: object, table: str) -> bool:
        pass


class Employee:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def save(self, db_connection: PostgresDB) -> bool:
        return db_connection.save(self, 'emp_table')

# The DB connection used here is hardcoded to use PostgresDB. We are restricting Employee to use a low level
# class implementation instead of an abstract DB connection. This is not compliant with the principle.
# Any change of DB type will cause major changes in code.
