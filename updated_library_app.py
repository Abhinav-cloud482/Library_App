import pickle
import os
import getpass
from difflib import get_close_matches
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- SAFE FILE PATH ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LIBRARY_FILE = os.path.join(BASE_DIR, 'library.pkl')
USERS_FILE = os.path.join(BASE_DIR, 'users.pkl')


# ---------------- File Handling ----------------

def load_data(file):
    try:
        if os.path.exists(file):
            with open(file, 'rb') as f:
                return pickle.load(f)
    except Exception as e:
        print("Error loading file:", e)
    return {}

def save_data(file, data):
    try:
        with open(file, 'wb') as f:
            pickle.dump(data, f)
    except PermissionError:
        print("Permission denied. Run program from your project folder.")
    except Exception as e:
        print("Error saving data:", e)


# ---------------- AI FEATURES ----------------

def classify_book(title):
    title = title.lower()
    if "python" in title:
        return "Programming"
    elif "history" in title:
        return "History"
    elif "love" in title:
        return "Romance"
    return "General"


def detect_suspicious(users, username):
    if len(users[username]['history']) > 15:
        print("⚠ Suspicious activity detected!")


def smart_search(books):
    query = input("Search: ")
    matches = get_close_matches(query, books.keys(), n=5, cutoff=0.3)

    if not matches:
        print("No matches found.")
    else:
        print("\nSuggestions:")
        for m in matches:
            print("-", m)


def trending_books(books):
    if not books:
        print("No books available.")
        return

    sorted_books = sorted(
        books.items(),
        key=lambda x: x[1].get("borrow_count", 0),
        reverse=True
    )

    print("\nTrending Books:")
    for title, info in sorted_books[:5]:
        print(f"{title} ({info.get('borrow_count',0)} borrows)")


def recommend_books(books, users, username):
    history = users[username]['history']
    borrowed = [h.split(": ")[1] for h in history if "Borrowed" in h]

    if not borrowed or not books:
        print("No history or books.")
        return

    titles = list(books.keys())

    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform(titles)

    last = borrowed[-1]
    if last not in titles:
        return

    idx = titles.index(last)
    sim = cosine_similarity(vectors[idx], vectors).flatten()

    indices = sim.argsort()[-5:][::-1]

    print("\nRecommended:")
    for i in indices:
        if titles[i] != last:
            print("-", titles[i])


# ---------------- User Management ----------------

def register(users):
    u = input("Username: ").strip()

    if u in users:
        print("User already exists.")
        return

    p = getpass.getpass("Password: ")

    users[u] = {"password": p, "history": []}
    save_data(USERS_FILE, users)
    print("Registered successfully.")


def login(users):
    u = input("Username: ")
    p = getpass.getpass("Password: ")

    if u in users and users[u]['password'] == p:
        print("Login successful.")
        return u

    print("❌ Invalid login")
    return None


# ---------------- Book Operations ----------------

def add_book(books):
    t = input("Title: ")
    a = input("Author: ")

    if t in books:
        print("Book already exists.")
        return

    books[t] = {
        "author": a,
        "available": True,
        "category": classify_book(t),
        "borrow_count": 0
    }

    save_data(LIBRARY_FILE, books)
    print("Book added.")


def borrow(books, users, u):
    t = input("Book: ")

    if t in books and books[t]["available"]:
        books[t]["available"] = False
        books[t]["borrow_count"] += 1

        users[u]['history'].append(f"Borrowed: {t}")
        detect_suspicious(users, u)

        save_data(LIBRARY_FILE, books)
        save_data(USERS_FILE, users)

        print("Book borrowed.")
    else:
        print("Unavailable")


def return_book(books, users, u):
    t = input("Book: ")

    if t in books:
        books[t]["available"] = True
        users[u]['history'].append(f"Returned: {t}")

        save_data(LIBRARY_FILE, books)
        save_data(USERS_FILE, users)

        print("Book returned.")
    else:
        print("Book not found.")


# ---------------- Menus ----------------

def user_menu(books, users, u):
    while True:
        print("\n1 Borrow\n2 Return\n3 Recommend\n4 Smart Search\n5 Trending\n6 Add Book\n7 Exit")
        c = input("Choice: ")

        if c == '1':
            borrow(books, users, u)
        elif c == '2':
            return_book(books, users, u)
        elif c == '3':
            recommend_books(books, users, u)
        elif c == '4':
            smart_search(books)
        elif c == '5':
            trending_books(books)
        elif c == '6':
            add_book(books)
        elif c == '7':
            break


def main():
    books = load_data(LIBRARY_FILE)
    users = load_data(USERS_FILE)

    while True:
        print("\n1 Register\n2 Login\n3 Exit")
        c = input("Choice: ")

        if c == '1':
            register(users)
        elif c == '2':
            u = login(users)
            if u:
                user_menu(books, users, u)
        elif c == '3':
            break


if __name__ == "__main__":
    main()