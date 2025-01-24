# Employee Management System

A simple **Employee Management System** implemented in Python. This project demonstrates a basic three-tier architecture, including a Presentation Layer, Backend Layer, and Business Logic Layer.

---

## Features

- **Add Employees**: Insert new employee records.
- **View Records**: Display all employee data.
- **Search Employees**:
  - By ID
  - By Name (supports partial match)
  - By Contact
  - By Salary Range
- **Delete Employees**: Remove an employee by their ID.
- **Sort Records**:
  - By Salary (Ascending/Descending)
  - By Name (Ascending/Descending)

---

## File Structure

- **`emp.py`**: Presentation Layer (handles input/output and menu navigation).
- **`employee.py`**: Backend Layer (defines the `Employee` class and its attributes).
- **`service.py`**: Business Logic Layer (implements core functionalities such as adding, searching, and sorting).

---

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>
2. Navigate to the project folder:

cd employee-management-system

3. Run the Program:
   python emp.py


Here's a detailed explanation of your code and the steps to create a GitHub repository with a README.md file for this project.

Project Explanation
This project is a simple Employee Management System in Python. It is divided into three layers, following a basic three-tier architecture:

Presentation Layer (emp.py)

Acts as the user interface.
Provides a menu-driven interface for the user to interact with the system.
Handles input and output operations.
Backend Layer (employee.py)

Defines the Employee class.
Contains attributes (id, name, salary, contact) and their getter and setter methods.
Includes a __str__ method for string representation of the Employee object.
Business Logic Layer (service.py)

Implements the Service class.
Contains all the core functionalities of the system, such as:
Adding employees.
Viewing employee records.
Searching by various criteria (e.g., name, ID, salary range).
Sorting employee records (by name or salary, in ascending or descending order).
Deleting employees.
Key Functionalities
Insert Record: Adds a new employee to the system. Ensures no duplicate IDs are added.
View Records: Displays all employee records.
Search:
By ID: Finds an employee by their ID.
By Name: Finds employees with a matching or partial name.
By Contact: Finds employees by their contact information.
By Salary Range: Finds employees within a specified salary range.
Delete: Removes an employee by their ID.
Sorting:
By Salary (Ascending/Descending).
By Name (Ascending/Descending).
Steps to Create a GitHub Repository
Create a Repository on GitHub

Go to GitHub and log in.
Click the New button to create a new repository.
Provide a repository name, e.g., employee-management-system.
Add a description: "A simple employee management system implemented in Python."
Initialize the repository with a README.md file.
Organize Your Code

Create a folder on your local machine, e.g., employee-management-system.
Inside the folder, create three files:
emp.py: Contains the presentation layer.
employee.py: Contains the backend layer.
service.py: Contains the business logic layer.
Create a README.md file to document the project.
Push the Code to GitHub

Open a terminal and navigate to the project folder.
Initialize a git repository:
bash
Copy
Edit
git init
Add the files to the staging area:
bash
Copy
Edit
git add .
Commit the changes:
bash
Copy
Edit
git commit -m "Initial commit"
Add the remote repository URL:
bash
Copy
Edit
git remote add origin <repository-url>
Push the code:
bash
Copy
Edit
git branch -M main
git push -u origin main
README File
Here’s the content for the README.md file:

markdown
Copy
Edit
# Employee Management System

A simple **Employee Management System** implemented in Python. This project demonstrates a basic three-tier architecture, including a Presentation Layer, Backend Layer, and Business Logic Layer.

---

## Features

- **Add Employees**: Insert new employee records.
- **View Records**: Display all employee data.
- **Search Employees**:
  - By ID
  - By Name (supports partial match)
  - By Contact
  - By Salary Range
- **Delete Employees**: Remove an employee by their ID.
- **Sort Records**:
  - By Salary (Ascending/Descending)
  - By Name (Ascending/Descending)

---

## File Structure

- **`emp.py`**: Presentation Layer (handles input/output and menu navigation).
- **`employee.py`**: Backend Layer (defines the `Employee` class and its attributes).
- **`service.py`**: Business Logic Layer (implements core functionalities such as adding, searching, and sorting).

---

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>
2. Navigate to the project folder:
   
   cd employee-management-system
4. Run the program:
   
   python emp.py


   
Example Usage
Menu Options

1. Insert Record
2. View Record
3. Search by ID
4. Delete by ID
5. Search by Name
6. Search by Contact
7. Search Salary by Range
8. Search Salary by Ascending Order
9. Search Salary by Descending Order
10. Search Name by Ascending Order
11. Search Name by Descending Order
12. Exit


Sample Input/Output

Add Employee

Enter id = 1
Enter name = Alice
Enter salary = 50000
Enter contact = 1234567890
Record inserted successfully


View Employees

name: Alice
id: 1
salary: 50000.0
contact: 1234567890


Technologies Used
Python: The core programming language.





