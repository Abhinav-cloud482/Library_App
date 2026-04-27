import pickle
import os
import getpass

LIBRARY_FILE = 'library.pkl'
USERS_FILE = 'users.pkl'


# ---------------- File Handling ----------------

def load_data(file):
    if os.path.exists(file):
        try:
            with open(file, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            print(f"Error loading {file}:", e)
    return {}

def save_data(file, data):
    try:
        with open(file, 'wb') as f:
            pickle.dump(data, f)
    except Exception as e:
        print(f"Error saving {file}:", e)


# ---------------- User Management ----------------

def register_user(users):
    username = input("Choose a username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return

    if username in users:
        print("Username already exists.")
        return

    password = getpass.getpass("Choose a password: ").strip()
    if not password:
        print("Password cannot be empty.")
        return

    role = input("Enter role (admin/user): ").strip().lower()
    if role not in ['admin', 'user']:
        print("Invalid role. Must be 'admin' or 'user'.")
        return

    users[username] = {
        'password': password,
        'role': role,
        'history': []
    }
    save_data(USERS_FILE, users)
    print(f"User '{username}' registered as {role}.")

def login_user(users):
    attempts = 3
    while attempts > 0:
        username = input("Username: ").strip()
        password = getpass.getpass("Password: ").strip()

        if username in users and users[username]['password'] == password:
            print(f"Login successful. Welcome, {username} ({users[username]['role']})!")
            return username, users[username]['role']
        else:
            attempts -= 1
            print(f"Invalid credentials. {attempts} attempt(s) remaining.")
    print("Too many failed login attempts.")
    return None, None

def reset_password(users):
    username = input("Enter your username to reset password: ").strip()
    if username not in users:
        print("Username not found.")
        return
    new_password = getpass.getpass("Enter new password: ").strip()
    if not new_password:
        print("Password cannot be empty.")
        return
    users[username]['password'] = new_password
    save_data(USERS_FILE, users)
    print("Password reset successfully.")


# ---------------- Book Operations ----------------

def add_book(books):
    title = input("Enter book title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    if title in books:
        overwrite = input("Book exists. Overwrite? (y/n): ").strip().lower()
        if overwrite != 'y':
            return

    author = input("Enter author name: ").strip()
    if not author:
        print("Author name cannot be empty.")
        return

    books[title] = {"author": author, "available": True}
    save_data(LIBRARY_FILE, books)
    print("Book added successfully.")

def remove_book(books):
    title = input("Enter book title to remove: ").strip()
    if title in books:
        del books[title]
        save_data(LIBRARY_FILE, books)
        print("Book removed.")
    else:
        print("Book not found.")

def borrow_book(books, users, username):
    title = input("Enter book title to borrow: ").strip()
    if title not in books:
        print("Book not found.")
        return

    if not books[title]["available"]:
        print("Book is already borrowed.")
    else:
        books[title]["available"] = False
        users[username]['history'].append(f"Borrowed: {title}")
        save_data(LIBRARY_FILE, books)
        save_data(USERS_FILE, users)
        print(f"You have borrowed '{title}'.")

def return_book(books, users, username):
    title = input("Enter book title to return: ").strip()
    if title not in books:
        print("Book not found.")
        return

    if books[title]["available"]:
        print("This book was not borrowed.")
    else:
        books[title]["available"] = True
        users[username]['history'].append(f"Returned: {title}")
        save_data(LIBRARY_FILE, books)
        save_data(USERS_FILE, users)
        print(f"You have returned '{title}'.")

def list_books(books):
    if not books:
        print("No books in the library.")
        return

    print("\nLibrary Catalog:")
    for title in sorted(books):
        info = books[title]
        status = "Available" if info["available"] else "Borrowed"
        print(f"- {title} by {info['author']} [{status}]")

def search_books(books):
    keyword = input("Enter keyword to search: ").strip().lower()
    if not keyword:
        print("Search keyword cannot be empty.")
        return

    results = {
        title: info for title, info in books.items()
        if keyword in title.lower() or keyword in info["author"].lower()
    }

    if not results:
        print("No matching books found.")
    else:
        print("\nSearch Results:")
        for title in sorted(results):
            info = results[title]
            status = "Available" if info["available"] else "Borrowed"
            print(f"- {title} by {info['author']} [{status}]")


# ---------------- Panels ----------------

def admin_panel(books, users):
    while True:
        print("\n--- Admin Panel ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Books")
        print("5. View Users")
        print("6. Logout")
        choice = input("Choose an option: ")

        if choice == '1':
            add_book(books)
        elif choice == '2':
            remove_book(books)
        elif choice == '3':
            list_books(books)
        elif choice == '4':
            search_books(books)
        elif choice == '5':
            print("\nRegistered Users:")
            for username, info in users.items():
                print(f"- {username} ({info['role']})")
        elif choice == '6':
            print("Logging out.")
            break
        else:
            print("Invalid choice.")

def user_panel(books, users, username):
    while True:
        print("\n--- User Panel ---")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. List Books")
        print("4. Search Books")
        print("5. View My Borrow History")
        print("6. Logout")
        choice = input("Choose an option: ")

        if choice == '1':
            borrow_book(books, users, username)
        elif choice == '2':
            return_book(books, users, username)
        elif choice == '3':
            list_books(books)
        elif choice == '4':
            search_books(books)
        elif choice == '5':
            history = users[username].get('history', [])
            if not history:
                print("No borrow history yet.")
            else:
                print("\nYour Borrow History:")
                for action in history:
                    print(f"- {action}")
        elif choice == '6':
            print("Logging out.")
            break
        else:
            print("Invalid choice.")


# ---------------- Main Menu ----------------

def main():
    books = load_data(LIBRARY_FILE)
    users = load_data(USERS_FILE)

    while True:
        print("\n=== Welcome to the Library Management System ===")
        print("1. Register")
        print("2. Login")
        print("3. Reset Password")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            register_user(users)
        elif choice == '2':
            username, role = login_user(users)
            if role == 'admin':
                admin_panel(books, users)
            elif role == 'user':
                user_panel(books, users, username)
        elif choice == '3':
            reset_password(users)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
