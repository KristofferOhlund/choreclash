from choreclash.db.db import Base, DB
from sqlalchemy import inspect

# First, ensure that the database and tables are created
engine = DB().get_engine()
inspector = inspect(engine)
print("tabeller i databasen:")
print(inspector.get_table_names())

# DML (Data Manipulation Language) = datan (INSERT, UPDATE, DELETE, SELECT)

