#  Mini Library Management System 

A simple, in-memory library management system built with Python using only **functions, dictionaries, lists, and tuples** — no classes or object-oriented programming.

This project supports basic **CRUD operations** for books and members, and allows users to **borrow and return books**, enforcing constraints like genre validation, borrowing limits, and unique entries.

---

##  Features

 Add / Update / Delete books  
 Add / Update / Delete members  
 Search books by title or author (case-insensitive, partial match)  
 Borrow and return books (max 3 per member)  
 Enforce genre validation using tuple  
 Data integrity checks for borrowed items  
 Console-based demo and simple unit testing using `assert`

---

## Project Structure

├── operations.py # Core functions: CRUD + borrow/return logic
├── tests.py # Unit tests using assert statements
├── demo.py # Sample run-through of main features
├── README.md # Project overview (this file)
├── UML.png or UML.pdf # Hand-drawn UML (must be created manually)
├── DesignRationale.pdf # Design decisions & justifications


---

##   How to Run 

1. *Clone or Download* the project.
2. Open a terminal or IDE inside the project folder.
3. Run the demo script:

   ```bash
   python demo.py

