# Book Store Management System
import mysql.connector as msql
from tkinter import *

class Book:
    """Class to represent a book with its properties"""
    def __init__(self, name, genre, author, quantity, publication, price):
        self.name = name
        self.genre = genre
        self.author = author
        self.quantity = quantity
        self.publication = publication
        self.price = price
    
    def display_info(self):
        """Display book information"""
        return f"{self.name} | {self.author} | {self.price}"

class Customer:
    """Class to represent a customer"""
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.cart = []
    
    def add_to_cart(self, book):
        self.cart.append(book)
    
    def calculate_total(self):
        total = 0
        for book in self.cart:
            total += book.price
        return total

class DatabaseManager:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.setup_database()
    
    def setup_database(self):
        try:
            self.connection = msql.connect(host='localhost', user='root', password='mysql')#give your password
            self.cursor = self.connection.cursor()
            self.cursor.execute('CREATE DATABASE IF NOT EXISTS store')
            self.cursor.execute('USE store')
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS books(
                BookName VARCHAR(70) PRIMARY KEY, 
                genre VARCHAR(30), 
                author VARCHAR(30), 
                quantity INT(3), 
                publication VARCHAR(30), 
                price INT(6))''')
            self.load_sample_books()
        except Exception as e:
            print(f"Database connection error: {e}")
    
    def load_sample_books(self):
        """Load sample Harry Potter books into database"""
        self.cursor.execute("DELETE FROM books")
        sample_books = [
            ("Harry Potter and Philosophers Stone", "Fantasy", "J. K. Rowling", 7, "Bloomsbury(UK)", 425),
            ("Harry Potter and Chamber of Secrets", "Fantasy", "J. K. Rowling", 5, "Bloomsbury(UK)", 399),
            ("Harry Potter and Prisoner of Azkaban", "Fantasy", "J. K. Rowling", 3, "Bloomsbury(UK)", 390),
            ("Harry Potter and Goblet of Fire", "Fantasy", "J. K. Rowling", 9, "Bloomsbury(UK)", 599),
            ("Harry Potter and Order of the Phoenix", "Fantasy", "J. K. Rowling", 4, "Bloomsbury(UK)", 799),
            ("Harry Potter and Half-Blood Prince", "Fantasy", "J. K. Rowling", 3, "Bloomsbury(UK)", 399),
            ("Harry Potter and Deathly Hallows", "Fantasy", "J. K. Rowling", 1, "Bloomsbury(UK)", 699)
        ]
        
        for book_data in sample_books:
            self.cursor.execute("INSERT INTO books VALUES(%s,%s,%s,%s,%s,%s)", book_data)
        self.connection.commit()
    
    def add_book(self, book):
        try:
            self.cursor.execute("INSERT INTO books VALUES(%s,%s,%s,%s,%s,%s)", 
                              (book.name, book.genre, book.author, book.quantity, book.publication, book.price))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error adding book: {e}")
            return False
    
    def remove_book(self, book_name, author):
        try:
            self.cursor.execute("DELETE FROM books WHERE (BookName=%s AND author=%s)", (book_name, author))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error removing book: {e}")
            return False
    
    def search_books(self, book_name="", author="", genre=""):
        try:
            self.cursor.execute("SELECT * FROM books WHERE (BookName=%s OR author=%s OR genre=%s)", 
                              (book_name, author, genre))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error searching books: {e}")
            return []
    
    def get_book_details(self, book_name):
        try:
            self.cursor.execute("SELECT * FROM books WHERE BookName=%s", (book_name,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error getting book details: {e}")
            return None

class BookStoreGUI:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.current_customer = None
        self.setup_gui()
        self.setup_variables()
        self.create_widgets()
    
    def setup_gui(self):
        self.window = Tk()
        self.window.title("Books Store Management System")
        self.window.configure(bg='white')
    
    def setup_variables(self):
        self.book_name = StringVar()
        self.genre = StringVar()
        self.author = StringVar()
        self.quantity = StringVar()
        self.publication = StringVar()
        self.price = StringVar()
        self.customer_name = StringVar()
        self.phone = StringVar()
        self.bill_book_name = StringVar()
    
    def create_widgets(self):
        # Title
        Label(self.window, text="Books Store Management System", 
              font='BritannicBold 35 bold', fg="purple", bg="white", 
              justify="center").grid(row=0, columnspan=5, pady=10)
        
        # Book Information Labels and Entry Fields
        labels = ["Book's Name:", "Genre:", "Author:", "Quantity:", "Publication:", "Price:"]
        variables = [self.book_name, self.genre, self.author, self.quantity, self.publication, self.price]
        
        for i, (label, var) in enumerate(zip(labels, variables)):
            Label(self.window, text=label, bg='white', fg='black', 
                  font='none 10').grid(row=i+2, column=0, padx=40, pady=5, sticky='w')
            Entry(self.window, textvariable=var).grid(row=i+2, column=1, padx=10, pady=5)
        
        # Action Buttons
        Button(self.window, text='Add Book', command=self.add_book, width=20, bg='lightgreen').grid(row=9, column=0, padx=20, pady=10)
        Button(self.window, text='Remove Book', command=self.remove_book, width=20, bg='lightcoral').grid(row=9, column=1, padx=20, pady=10)
        Button(self.window, text='Search Book', command=self.search_book, width=20, bg='lightblue').grid(row=9, column=2, padx=20, pady=10)
        Button(self.window, text='Clear Fields', command=self.clear_fields, width=20, bg='lightyellow').grid(row=10, column=0, padx=20, pady=10)
        
        # Billing Section
        Label(self.window, text="Billing Section", bg='white', fg='purple', 
              font='BritannicBold 12').grid(row=13, column=0, padx=40, pady=5)
        
        Label(self.window, text="Customer Name:", bg='white', fg='black', 
              font='none 10').grid(row=14, column=0, padx=40, pady=5, sticky='w')
        Entry(self.window, textvariable=self.customer_name).grid(row=14, column=1, padx=10, pady=5)
        
        Label(self.window, text="Phone No.:", bg='white', fg='black', 
              font='none 10').grid(row=15, column=0, padx=40, pady=5, sticky='w')
        Entry(self.window, textvariable=self.phone).grid(row=15, column=1, padx=10, pady=5)
        
        Label(self.window, text="Book's Name:", bg='white', fg='black', 
              font='none 10').grid(row=16, column=0, padx=40, pady=5, sticky='w')
        Entry(self.window, textvariable=self.bill_book_name).grid(row=16, column=1, padx=10, pady=5)
        
        # Billing Buttons
        Button(self.window, text='Create Customer', command=self.create_customer, 
               width=20, bg='lightsteelblue').grid(row=17, column=0, padx=20, pady=5)
        Button(self.window, text='Add to Cart', command=self.add_to_cart, 
               width=20, bg='lightgreen').grid(row=18, column=0, padx=20, pady=10)
        Button(self.window, text='Generate Bill', command=self.generate_bill, 
               width=20, bg='gold').grid(row=18, column=1, padx=20, pady=10)
        
        # Exit Button
        Button(self.window, text='Close Application', command=self.exit_app, 
               width=20, background="red", fg='white').grid(row=20, column=2, padx=20, pady=10)
    
    def add_book(self):
        try:
            new_book = Book(
                self.book_name.get(),
                self.genre.get(),
                self.author.get(),
                int(self.quantity.get()),
                self.publication.get(),
                int(self.price.get())
            )
            
            if self.db_manager.add_book(new_book):
                print("Book Added Successfully!")
                self.clear_fields()
            else:
                print("Error adding book!")
                
        except ValueError:
            print("Please enter valid quantity and price numbers!")
        except Exception as e:
            print(f"Error: {e}")
    
    def remove_book(self):
        if self.db_manager.remove_book(self.book_name.get(), self.author.get()):
            print("Book Removed Successfully!")
            self.clear_fields()
        else:
            print("Error removing book!")
    
    def search_book(self):
        results = self.db_manager.search_books(
            self.book_name.get(),
            self.author.get(),
            self.genre.get()
        )
        
        print("Available Books:")
        if results:
            for book in results:
                print(book)
        else:
            print("No books found!")
        print('.' * 50)
    
    def clear_fields(self):
        for var in [self.book_name, self.genre, self.author, self.quantity, self.publication, self.price]:
            var.set('')
    
    def create_customer(self):
        if self.customer_name.get() and self.phone.get():
            self.current_customer = Customer(self.customer_name.get(), self.phone.get())
            print(f"Customer '{self.customer_name.get()}' created successfully!")
        else:
            print("Please enter customer name and phone number!")
    
    def add_to_cart(self):
        if not self.current_customer:
            print("Please create a customer first!")
            return
        
        book_details = self.db_manager.get_book_details(self.bill_book_name.get())
        if book_details:
            book = Book(
                book_details[0],  #name
                book_details[1],  #genre
                book_details[2],  #author
                book_details[3],  #quantity
                book_details[4],  #publication
                book_details[5]   #price
            )
            self.current_customer.add_to_cart(book)
            print(f"'{book.name}' added to cart!")
            self.bill_book_name.set('')
        else:
            print("Book not found!")
    
    def generate_bill(self):
        if not self.current_customer:
            print("Please create a customer first!")
            return
        
        if not self.current_customer.cart:
            print("Cart is empty! Please add books to cart.")
            return
        
        print("\n" + "="*50)
        print("BOOK STORE MANAGEMENT SYSTEM")
        print("="*50)
        print(f"Customer Name: {self.current_customer.name}")
        print(f"Phone No.: {self.current_customer.phone}")
        print("-"*50)
        print("BOOKS PURCHASED:")
        print("-"*50)
        
        for book in self.current_customer.cart:
            print(f"{book.name} | {book.author} | ₹{book.price}")
        
        total_amount = self.current_customer.calculate_total()
        print("-"*50)
        print(f"Total Amount: ₹{total_amount}")
        print("="*50)
        print("Thank You for Shopping with Us!")
        print("="*50)
        
        # Clear customer data after bill generation
        self.current_customer = None
        self.customer_name.set('')
        self.phone.set('')
    
    def exit_app(self):
        self.window.destroy()
    
    def run(self):
        self.window.mainloop()

# Main execution
if __name__ == "__main__":
    # Create and run the Book Store Management System
    app = BookStoreGUI()
    print("Book Store Management System Started!")
    print("="*50)
    app.run()

