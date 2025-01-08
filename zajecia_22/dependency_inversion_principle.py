# class MySQLDatabase:
#     def connect(self):
#         print("MySQLDatabase connected")
#
#
# class PostgresDatabase:
#     def connect(self):
#         print("PostgresDatabase connected")
#
# class MySQLDataProcessor:
#     def __init__(self):
#         self.db = MySQLDatabase()
#
#     def process(self):
#         self.db.connect()
#         print("Processing data")
#
# class PostgresDataProcessor:
#     def __init__(self):
#         self.db = PostgresDatabase()
#
#     def process(self):
#         self.db.connect()
#         print("Processing data")

from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("MySQLDatabase connected")

class PostgresDatabase(Database):
    def connect(self):
        print("PostgresDatabase connected")

class DataProcessor:
    def __init__(self, db: Database):
        self.db = db

    def process(self):
        self.db.connect()
        print("Processing data")


mysql_db = MySQLDatabase()
postgres_db = PostgresDatabase()
data_processor = DataProcessor(mysql_db)
data_processor_2 = DataProcessor(postgres_db)
data_processor.process()
data_processor_2.process()