# Book Store Management System - OOP

A **Book Store Management System** built using **Python**, **Object-Oriented Programming**, **MySQL Database**, and **Tkinter GUI**. This project demonstrates OOP concepts with clean code architecture and user-friendly interface.

## Project Overview

This system allows bookstore owners to manage inventory, handle customer information, and process sales transactions. Built with OOP principles for scalability and maintainability.

## Features

### Book Management
- Add new books with complete details
- Remove books from inventory
- Search books by name, author, or genre
- Track inventory and pricing

### Customer Management
- Create customer profiles
- Shopping cart functionality
- Generate detailed bills

### Database Integration
- MySQL database with persistent storage
- Automatic database setup
- Pre-loaded sample data
- Error handling for all operations

## Screenshots

### Main Application Interface
*Screenshot of the main GUI window showing all input fields, labels, and buttons*

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/f9537a36-2ce4-482e-8e23-dd258cf93d92" />


### Search Results Output
*Screenshot of the console showing search results with book details*

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/b63b0548-265a-46b6-9deb-125642d07b0c" />

### Bill Generation Output
*Screenshot of the console showing complete bill with customer details and total amount*

<img width="1918" height="1079" alt="image" src="https://github.com/user-attachments/assets/ab53b39e-c169-45ac-a76f-a13d510aaffd" />

## Technical Architecture

### Classes Used

**Book Class**
- Properties: name, genre, author, quantity, publication, price
- Methods: display_info()

**Customer Class** 
- Properties: name, phone, cart
- Methods: add_to_cart(), calculate_total()

**DatabaseManager Class**
- Handles all database operations
- Methods: add_book(), remove_book(), search_books()

**BookStoreGUI Class**
- Main application interface
- Coordinates all system components

## Technologies Used

- **Python 3.x** - Core programming language
- **Tkinter** - GUI framework
- **MySQL** - Database management
- **mysql-connector-python** - Database connector

## Installation & Setup

### Prerequisites
- Python 3.x installed
- MySQL Server running
- mysql-connector-python package

### Setup Steps
1. Install required package:
   ```bash
   pip install mysql-connector-python
   ```

2. Ensure MySQL is running with default credentials (root/mysql)

3. Run the application:
   ```bash
   bookstore_management_system.py
   ```

## How to Use

### Managing Books
1. **Add Books**: Fill details and click "Add Book"
2. **Search Books**: Enter search criteria and click "Search Book"  
3. **Remove Books**: Enter book name/author and click "Remove Book"

### Processing Sales
1. **Create Customer**: Enter name and phone, click "Create Customer"
2. **Add to Cart**: Enter book name, click "Add to Cart"
3. **Generate Bill**: Click "Generate Bill" for complete invoice

## Key Features Demonstrated

### Object-Oriented Programming
- Encapsulation and abstraction
- Modular design with separate classes
- Code reusability and maintainability

### Database Integration
- CRUD operations
- Error handling
- Data persistence

### GUI Development
- User-friendly interface
- Event handling
- Input validation

## Sample Data

System includes pre-loaded Harry Potter book series with complete details including pricing and availability.

*This project showcases modern software development practices using Python OOP, database integration, and GUI design.*
