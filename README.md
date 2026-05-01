# Library App

## Library Management System with AI Features

An advanced Command-Line Library Management System built in Python, enhanced with AI/ML capabilities, smart search, recommendations, and automation features. The system uses file-based storage and optional modern AI tools for an improved user experience.


## Features

User Management
- Register new users
- Secure login with password masking
- Persistent user data storage
- Borrowing history tracking

Book Management (Admin Only)
- Add books with automatic category classification
- Track availability status
- Maintain borrow count analytics
- Persistent storage using pickle

Borrowing System (User Only)
- Borrow books
- Return books
- Automatic history logging
- Suspicious activity detection (based on usage patterns)

Data Persistence
- Stores data using Python pickle
- Separate storage for :
    - Users (users.pkl)
    - Library books (library.pkl)


## AI & Smart Features

Smart Search (Fuzzy Matching)

- Suggests similar book titles even with typos
- Powered by difflib

Trending Books

- Displays most borrowed books
- Based on real usage data

Recommendation System (ML)

- Uses TF-IDF + Cosine Similarity
- Suggests books based on user history

Transformer-Based AI (Optional)

- Uses transformers (GPT-2)
- Generate intelligent book recommendations

Chatbot Assistant

- Simple built-in chatbot for guidance
- Helps users navigate features


## QR Code Scanner

- Scan QR codes using webcam
- Built with OpenCV



## Technologies Used

- Python 3.x
- Pickle (data persistence)
- OS module
- Getpass (secure password input)
- Difflib (fuzzy search)
- Scikit-learn (ML recommendations)
- Transformers (optional AI model)
- OpenCV (QR scanning)


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

3. Install Dependencies

```
pip install scikit-learn transformers opencv-python
```
(Optional: install only what you need — app works without transformers & QR)

## Usage

Run the application :

```
python updated_library_app.py
```

## Main Menu

```
1. Register
2. Login
3. Exit
```


## Screenshots

<img width="805" height="325" alt="1" src="https://github.com/user-attachments/assets/237a5fae-a443-41f0-97b9-2b86ec2b7699" />

### Updated Project

<img width="1358" height="593" alt="output" src="https://github.com/user-attachments/assets/b9e0361b-ec13-4985-bbcf-0641b950b1ca" />


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

- AI-based book classification
- Smart fuzzy search suggestions
- ML-powered recommendation engine
- Trending analysis via borrow count
- Suspicious activity detection
- Optional deep learning integration
- QR-based interaction support
- Modular and scalable CLI structure


## Future Improvements

- Password hashing (security enhancement)
- Role-based system (Admin/User reintroduction)
- GUI (Tkinter / Web App)
- Database integration (SQLite / MongoDB)
- Book metadata enrichment (ISBN, cover images)
- Real chatbot using NLP APIs
- Mobile app integration## Contributing

## Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is open-source and available under the MIT License.

## Acknowledgements

- Python Documentation
- Scikit-learn
- Hugging Face Transformers
- OpenCV Community

## Author

Abhinav Dixit

Python Developer | Data & ML Enthusiast
