# Student Record Management System
# Mini Project - Assignment 1

import os

FILE_NAME = "students.txt"


# Function to load records from file
def load_records():
    records = []

    try:
        if not os.path.exists(FILE_NAME):
            return records

        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()

                if line:
                    data = line.split("|")

                    if len(data) == 6:
                        student = {
                            "id": data[0],
                            "name": data[1],
                            "age": int(data[2]),
                            "course": data[3],
                            "email": data[4],
                            "marks": float(data[5])
                        }

                        records.append(student)

    except (FileNotFoundError, ValueError) as error:
        print(f"Error loading records: {error}")

    except Exception as error:
        print(f"Unexpected error: {error}")

    return records


# Function to save records to file
def save_records(records):
    try:
        with open(FILE_NAME, "w") as file:
            for student in records:
                file.write(
                    f"{student['id']}|"
                    f"{student['name']}|"
                    f"{student['age']}|"
                    f"{student['course']}|"
                    f"{student['email']}|"
                    f"{student['marks']}\n"
                )

    except OSError as error:
        print(f"Error saving records: {error}")


# Function to add a new student record
def add_record(records):
    print("\n--- Add Student Record ---")

    try:
        student_id = input("Enter Student ID: ").strip()

        if not student_id:
            print("Student ID cannot be empty.")
            return

        # Check if ID already exists
        for student in records:
            if student["id"] == student_id:
                print("Student ID already exists.")
                return

        name = input("Enter Name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        age = int(input("Enter Age: "))

        if age <= 0:
            print("Age must be greater than 0.")
            return

        course = input("Enter Course: ").strip()

        if not course:
            print("Course cannot be empty.")
            return

        email = input("Enter Email: ").strip()

        if not email or "@" not in email:
            print("Please enter a valid email address.")
            return

        marks = float(input("Enter Marks: "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "course": course,
            "email": email,
            "marks": marks
        }

        records.append(student)
        save_records(records)

        print("\nStudent record added successfully!")

    except ValueError:
        print("Invalid input! Age must be an integer and marks must be a number.")

    except Exception as error:
        print(f"An unexpected error occurred: {error}")

# Function to view all student records
def view_records(records):
    print("\n--- All Student Records ---")

    if not records:
        print("No student records found.")
        return

    print("-" * 90)
    print(f"{'ID':<10}{'Name':<20}{'Age':<8}{'Course':<15}{'Email':<25}{'Marks':<10}")
    print("-" * 90)

    for student in records:
        print(
            f"{student['id']:<10}"
            f"{student['name']:<20}"
            f"{student['age']:<8}"
            f"{student['course']:<15}"
            f"{student['email']:<25}"
            f"{student['marks']:<10.2f}"
        )

    print("-" * 90)

# Function to search for a student
def search_record(records):
    print("\n--- Search Student Record ---")

    search_id = input("Enter Student ID to search: ").strip()

    if not search_id:
        print("Student ID cannot be empty.")
        return

    for student in records:
        if student["id"] == search_id:
            print("\nStudent Found!")
            print("-" * 40)
            print(f"Student ID : {student['id']}")
            print(f"Name       : {student['name']}")
            print(f"Age        : {student['age']}")
            print(f"Course     : {student['course']}")
            print(f"Email      : {student['email']}")
            print(f"Marks      : {student['marks']}")
            print("-" * 40)
            return

    print("Student record not found.")

# Function to update a student record
def update_record(records):
    print("\n--- Update Student Record ---")

    student_id = input("Enter Student ID to update: ").strip()

    for student in records:
        if student["id"] == student_id:

            print("\nLeave a field blank if you don't want to change it.")

            name = input(f"Enter Name [{student['name']}]: ").strip()
            age = input(f"Enter Age [{student['age']}]: ").strip()
            course = input(f"Enter Course [{student['course']}]: ").strip()
            email = input(f"Enter Email [{student['email']}]: ").strip()
            marks = input(f"Enter Marks [{student['marks']}]: ").strip()

            try:
                if name:
                    student["name"] = name

                if age:
                    new_age = int(age)

                    if new_age <= 0:
                        print("Age must be greater than 0.")
                        return

                    student["age"] = new_age

                if course:
                    student["course"] = course

                if email:
                    if "@" not in email:
                        print("Invalid email address.")
                        return

                    student["email"] = email

                if marks:
                    new_marks = float(marks)

                    if new_marks < 0 or new_marks > 100:
                        print("Marks must be between 0 and 100.")
                        return

                    student["marks"] = new_marks

                save_records(records)

                print("\nStudent record updated successfully!")
                return

            except ValueError:
                print("Invalid input. Please enter valid numbers for age and marks.")
                return

    print("Student record not found.")

# Function to delete a student record
def delete_record(records):
    print("\n--- Delete Student Record ---")

    student_id = input("Enter Student ID to delete: ").strip()

    for student in records:
        if student["id"] == student_id:

            print("\nStudent Found:")
            print(f"Name: {student['name']}")
            print(f"Course: {student['course']}")

            confirmation = input("Are you sure you want to delete this record? (y/n): ").lower()

            if confirmation == "y":
                records.remove(student)
                save_records(records)
                print("Student record deleted successfully!")
            else:
                print("Delete operation cancelled.")

            return

    print("Student record not found.")

# Main menu function
def main():
    records = load_records()

    while True:
        print("\n")
        print("=" * 50)
        print("       STUDENT RECORD MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Add Student Record")
        print("2. View All Records")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("=" * 50)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_record(records)

        elif choice == "2":
            view_records(records)

        elif choice == "3":
            search_record(records)

        elif choice == "4":
            update_record(records)

        elif choice == "5":
            delete_record(records)

        elif choice == "6":
            print("\nThank you for using Student Record Management System!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 6.")


# Start the application
if __name__ == "__main__":
    main()