from crud_operations import (
    create_user,
    fetch_all_students,
    update_student_city,
    delete_students_by_age,
)
from tables import create_all

# Create database connection and students table
print("Creating students table...")
create_all()
print("Table created successfully!\n")

# Insert 3 student records
print("Inserting 3 student records...")
create_user(1, "Rahul", 22, "Mumbai")
create_user(2, "Priya", 19, "Delhi")
create_user(3, "Amit", 18, "Bangalore")
print("Records inserted successfully!\n")

# Fetch all students
print("Fetching all students...")
all_students = fetch_all_students()
print("All Students:")
for student in all_students:
    print(
        f"  ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, City: {student[3]}"
    )
print()

# Update city of student whose name = "Rahul"
print("Updating Rahul's city to 'Pune'...")
update_student_city("Rahul", "Pune")
print("Update successful!\n")

# Fetch all students after update
print("Fetching all students after update...")
all_students = fetch_all_students()
print("All Students (After Update):")
for student in all_students:
    print(
        f"  ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, City: {student[3]}"
    )
print()

# Delete student whose age < 20
print("Deleting students with age < 20...")
delete_students_by_age(20)
print("Delete successful!\n")

# Fetch all students after deletion
print("Fetching all students after deletion...")
all_students = fetch_all_students()
print("All Students (After Deletion):")
for student in all_students:
    print(
        f"  ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, City: {student[3]}"
    )
