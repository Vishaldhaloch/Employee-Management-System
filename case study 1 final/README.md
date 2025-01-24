# Employee Management System

A simple **Employee Management System** implemented in Python. This project demonstrates a basic three-tier architecture, including a Presentation Layer, Backend Layer, and Business Logic Layer.

## Features

- **Add Employees**: Insert new employee records with ID, name, salary, and contact.
- **View Records**: Display all employee data.
- **Search Employees**:
  - By ID
  - By Name (supports partial matches)
  - By Contact
  - By Salary Range
- **Delete Employees**: Remove an employee by their ID.
- **Sort Records**:
  - By Salary (Ascending/Descending)
  - By Name (Ascending/Descending)
  - 
## File Structure

- **`emp.py`**: Presentation Layer (handles input/output and menu navigation).
- **`employee.py`**: Backend Layer (defines the `Employee` class and its attributes).
- **`service.py`**: Business Logic Layer (implements core functionalities such as adding, searching, and sorting).

## How It Works

### 1. Presentation Layer (`emp.py`)
This is the user interface. It provides a menu-driven system where users can:
- Add a new employee.
- View all records.
- Search, delete, or sort records using various criteria.
- Exit the program.

### 2. Backend Layer (`employee.py`)
This defines the `Employee` class with:
- Attributes: `id`, `name`, `salary`, `contact`.
- Getter and setter methods for encapsulation.
- A `__str__` method for string representation.

### 3. Business Logic Layer (`service.py`)
This layer performs operations such as:
- Adding employees to an in-memory list (`emp_list`).
- Searching and sorting employee records.
- Deleting employees by ID.

## How to Run the Project

### Prerequisites
- Python 3.x installed on your system.

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   
2. Navigate to the project directory:
   
    cd employee-management-system
   
4. Run the application:

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





