Overview
This project is a menu-driven program designed to manage a database of student records using binary file handling in Python. The program offers various functionalities to create, view, search, update, insert, and delete student records. The records are stored persistently in a binary file using the pickle module, ensuring efficient serialization and deserialization of data.

Features
Create a Fresh Database:

Users can input the details of multiple students, including their roll number, name, class, and marks.
Records are stored as dictionaries and serialized into a binary file (mybinary.dat).
Display All Records:

Retrieve and display all student records stored in the binary file.
Search and Display by Roll Number:

Search for a specific student by roll number and display their details.
Alerts the user if no matching record is found.
Insert a New Record:

Add a new student's record at a specific position in the database.
Ensures records are re-organized correctly after the insertion.
Delete a Record by Roll Number:

Remove a student’s record based on their roll number.
Retains all other records while deleting the specified one.
Update Marks of a Student:

Modify the marks of a specific student based on their roll number.
Updates the record in the file and retains all other data.
Exit:

Provides an option to gracefully terminate the program.
Technologies Used
Programming Language: Python
File Handling: Binary file handling using the pickle module for serialization and deserialization of student records.
Key Concepts Demonstrated
Binary File Handling:

Efficient storage and retrieval of structured data.
Use of pickle.dump() and pickle.load() for serialization and deserialization.
Menu-Driven Interface:

User-friendly interface to perform multiple operations interactively.
Data Manipulation:

CRUD operations (Create, Read, Update, Delete) implemented efficiently.
Error Handling:

Uses try-except blocks to manage EOFError during file reading.


Workflow
Start the program to see the main menu.
Enter a choice corresponding to an operation.
Perform the operation (e.g., creating a record, searching, or updating).
Return to the menu until the user chooses to exit.
