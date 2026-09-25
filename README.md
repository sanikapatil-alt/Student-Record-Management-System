# Student Record Management System

## Project Title
**Student Record Management System – Console-Based Python Application**

## Project Description
The Student Record Management System is a menu-driven console application developed in Python. It allows users to add, view, search, update, and delete student records.

The application uses file handling to store records permanently in a text file. Therefore, records remain available even after the program is closed and reopened.

## Features
- Add new student records
- View all student records
- Search a student by Student ID
- Update an existing student record
- Delete a student record
- Persistent storage using `students.txt`
- Input validation
- Exception handling
- Menu-driven console interface
- Modular programming using functions

## Student Record Fields
Each record contains:
- Student ID
- Name
- Age
- Course
- Email
- Marks

## Technologies / Concepts Used
- Python 3
- Variables and data types
- Lists
- Dictionaries
- Conditional statements
- `while` and `for` loops
- Functions
- Exception handling (`try`, `except`)
- File I/O (`open`, read, write)
- String operations
- Menu-driven application design

## Project Structure
```text
Student-Record-Management-System/
│
├── student_record_management.py
├── students.txt
├── Assignment_Report.docx
├── README.md
└── screenshots/
    ├── menu.png
    ├── add_record.png
    ├── view_records.png
    ├── search_record.png
    ├── update_record.png
    ├── delete_record.png
    └── exception_handling.png
```

## How to Run

### 1. Install Python
Make sure Python 3 is installed on your computer.

Check the version:

```bash
python --version
```

### 2. Open the Project Folder
Open the project folder in VS Code or a terminal.

### 3. Run the Application
Execute:

```bash
python student_record_management.py
```

If `python` does not work on Windows, try:

```bash
py student_record_management.py
```

## Main Menu
The application provides the following options:

```text
==================================================
       STUDENT RECORD MANAGEMENT SYSTEM
==================================================
1. Add Student Record
2. View All Records
3. Search Student
4. Update Student
5. Delete Student
6. Exit
==================================================
Enter your choice (1-6):
```

## Sample Input

```text
Enter Student ID: 101
Enter Name: Sanika Patil
Enter Age: 22
Enter Course: BCA
Enter Email: sanika@gmail.com
Enter Marks: 85
```

## Sample Output

```text
Student record added successfully!
```

## File Storage
Student records are stored in:

```text
students.txt
```

Records are stored using the `|` separator, for example:

```text
101|Sanika Patil|22|BCA|sanika@gmail.com|85.0
```

## Exception Handling
The application handles invalid input without terminating unexpectedly.

For example, if the user enters text instead of a numeric age:

```text
Enter Age: abc
```

the application displays:

```text
Invalid input! Age must be an integer and marks must be a number.
```

File-related errors are also handled using exception handling.

## Testing Performed
The following operations were tested:
- Adding student records
- Viewing records
- Searching records
- Updating records
- Deleting records
- Invalid input handling
- File persistence after closing and reopening the application

## Screenshots
Add the following screenshots to the `screenshots` folder and include them in the GitHub repository:
- Main menu
- Add record
- View records
- Search record
- Update record
- Delete record
- Exception handling
- Optional: `students.txt` showing saved records

## Learning Outcomes
This project demonstrates how fundamental Python programming concepts can be combined to create a practical application. It provides experience with data structures, functions, loops, conditional statements, exception handling, file handling, and menu-driven program design.

## Future Enhancements
Possible future improvements include:
- GUI interface using Tkinter
- Database storage using SQLite/MySQL
- Sorting and filtering records
- Student result/grade calculation
- Login and authentication
- Exporting records to CSV or Excel

## Conclusion
The Student Record Management System successfully demonstrates a functional console-based record-management application in Python. It satisfies the required concepts of variables and data types, conditional statements, loops, functions, exception handling, file I/O, and menu-driven application design.
