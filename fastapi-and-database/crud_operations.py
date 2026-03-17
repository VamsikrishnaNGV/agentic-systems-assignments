# Logic for CRUD Operations
from db import engine
from tables import students
from sqlalchemy import insert, select, update, delete


# Create database connection
# Create students table
def create_user(student_id: int, student_name: str, student_age: int, city: str):
    with engine.connect() as conn:
        query = insert(students).values(
            id=student_id, name=student_name, age=student_age, city=city
        )
        conn.execute(query)
        conn.commit()


# Fetch all students
def fetch_all_students():
    with engine.connect() as conn:
        query = select(students)
        result = conn.execute(query)
        return result.fetchall()


# Update city of student whose name = "Rahul"
def update_student_city(name: str, new_city: str):
    with engine.connect() as conn:
        query = update(students).where(students.c.name == name).values(city=new_city)
        conn.execute(query)
        conn.commit()


# Delete student whose age < 20
def delete_students_by_age(age_limit: int):
    with engine.connect() as conn:
        query = delete(students).where(students.c.age < age_limit)
        conn.execute(query)
        conn.commit()
