# Manage Tables
# students table
# Column Name	Data Type	Constraints
# id	Integer	Primary Key
# name	String	Not Null
# age	Integer	18+
# city	String	Nullable

from db import engine

from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

students = Table(
    "students",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("age", Integer, nullable=False),
    Column("city", String, nullable=True),
)


def create_all():
    metadata.create_all(engine)
