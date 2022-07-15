# A way to fix the issue is to create an abstract class for DB connection in general, and let different types of DB
# inherit that class and implement the save method individually. In Employee class, we can use the abstract class to
# save into DB , and let the client pass in the correct DB type.


class DataBase:
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port

    def connect(self):
        raise NotImplementedError()

    def save(self, obj, table: str) -> bool:
        raise NotImplementedError()


class PostgresDB(DataBase):
    def __init__(self, ip: str, port: int, username: str, password: str, db: str):
        super().__init__(ip, port)
        self.username = username
        self.password = password
        self.db = db
        self.connect()

    def connect(self):
        pass

    def save(self, obj, table: str) -> bool:
        pass


class OracleDB(DataBase):
    def __init__(self, ip: str, port: int, username: str, password: str, schema: str):
        super().__init__(ip, port)
        self.username = username
        self.password = password
        self.schema = schema
        self.connect()

    def connect(self):
        pass

    def save(self, obj, table: str) -> bool:
        pass


class Employee:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def save(self, db_connection: DataBase) -> bool:
        return db_connection.save(self, 'emp_table')

# Saving:
# Employee('Shashank').save(PostgresDB(ip='10.113.56.125', port='9001', username='shashank', password='admin', db='solid'))
# Or
# Employee('Shashank').save(OracleDB(ip='10.113.56.125', port='10800', username='shashank', password='admin', schema='solid'))
