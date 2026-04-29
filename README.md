# Library App

## Library Management System (CLI)

A simple Library Management System built in Python that supports user authentication, book management, and borrowing functionality. The system runs in the command line and uses file-based storage for persistence.

## Features

User Management
- Register new users (Admin/User roles)
- Secure login with password masking
- Password reset functionality
- Role-based access control

Book Management (Admin Only)
- Add new books
- Remove existing books
- View all books
- Search books by title or author

Borrowing System (User Only)
- Borrow books
- Return books
- Track personal borrowing history

Data Persistence
- Stores data using Python pickle
- Separate storage for :
    - Users (users.pkl)
    - Library books (library.pkl)

 
## Technologies Used

- Python 3.x
- Pickle (data serialization)
- OS module (file handling)
- Getpass (secure password input)

## Installation

1. Clone the repository :

```
git clone https://github.com/your-username/library_app.git
cd library_app
```

2. Ensure Python is installed :

```
python 3
```

## Usage

Run the application :

```
python Library.py
```

## Main Menu

```
1. Register
2. Login
3. Reset Password
4. Exit
```


## Screenshots

<img width="805" height="325" alt="1" src="https://github.com/user-attachments/assets/237a5fae-a443-41f0-97b9-2b86ec2b7699" />



## Roles & Permissions

Admin

- Add books
- Remove books
- View all books
- Search books
- View all registered users

User

- Borrow books
- Return books
- View available books
- Search books
- View personal borrowing history


## Book Data Format

```
{
    "Book Title": {
        "author": "Author Name",
        "available": True
    }
}
```

## User Data Format

```
{
    "username": {
        "password": "user_password",
        "role": "admin/user",
        "history": [
            "Borrowed: Book Name",
            "Returned: Book Name"
        ]
    }
}

```

## Functionality Overview

- Authentication System with limited login attempts
- Search Feature using keyword matching
- Borrowing Logic with availability tracking
- History Tracking for each user
- Error Handling for file operations

## Future Improvements

- Password hashing for better security
- GUI version (Tkinter / Web-based)
- Book categories & filtering
- Due dates and fine calculation
- Multi-user concurrency support
- Database integration (SQLite/MySQL)

## Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is open-source and available under the MIT License.

## Acknowledgements

- Python official documentation

- Inspiration from basic library systems


## Author

Abhinav Dixit

Python Developer | Data & ML Enthusiast
