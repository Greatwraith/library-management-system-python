# 📚 Library Management System

A lightweight, beginner-friendly library management system program built entirely with Python, no external dependencies required.

---

## ✨ Features

- 📖 **View all books** — Browse the complete list of available books in the library
- 🤝 **Borrow a book** — Check out a book by entering its title and your name
- ➕ **Add a new book** — Expand the library collection on the fly
- 🔄 **Return a book** — Return a previously borrowed book back to the library
- 🔒 **Borrow tracking** — Keeps track of who has borrowed which book, preventing double borrowing

---

## 🚀 Getting Started

### Prerequisites

All you need is **Python 3** installed on your machine. No third-party packages or pip installs required.

Check your Python version:
```bash
python --version
```

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/your-username/library-management-system-python.git
```

**2. Navigate into the project directory**
```bash
cd library-management-system-python
```

**3. Run the application**
```bash
python library.py
```

That's it. The library is ready to use. ✅

---

## 🖥️ How to Use

Once the program starts, you'll be greeted with a menu like this:

```
Welcome to the Python Library. Please select an option.
1. Show all books
2. Borrow a book
3. Add a new book
4. Return a book
press 'q' to quit the program.
```

Simply type the number corresponding to your desired action and press **Enter**.

---

### Option 1 — Show All Books

Displays the full list of books currently in the library.

```
1. Atomic Habits
2. Rich Dad Poor Dad
3. The Alchemist
4. Think and Grow Rich
...
```

---

### Option 2 — Borrow a Book

You'll be prompted to enter the book title and your name.

```
Enter the book title: Atomic Habits
Enter your name: John
```

**Possible responses:**

| Scenario | Message |
|---|---|
| Book is available | `Borrowing successful. You can take the book.` |
| Book is already borrowed | `This book is currently unavailable. Borrowed by John.` |
| Book doesn't exist | `The selected book does not exist in the library collection.` |

> ⚠️ **Note:** Book titles are **case-sensitive**. Enter the title exactly as it appears in the list.

---

### Option 3 — Add a New Book

Adds a new book to the library's collection permanently (for the current session).

```
Enter the title of the book to add: The Lean Startup
```

```
The book has been successfully added to the library collection.
```

---

### Option 4 — Return a Book

Returns a borrowed book back to the library, making it available for others.

```
Enter the title of the book to return: Atomic Habits
```

**Possible responses:**

| Scenario | Message |
|---|---|
| Successfully returned | `Book has been returned, thank you!` |
| Book wasn't borrowed | `The book 'Atomic Habits' is not currently borrowed.` |
| Book doesn't exist in system | `This book is not registered in the library system.` |

---

### Continuing or Quitting

After every action, the program will ask:

```
Press 'c' to continue or 'q' to quit.
```

- Press **`c`** → Go back to the main menu
- Press **`q`** → Exit the program gracefully

---

## 📦 Default Book Collection

The library comes pre-loaded with **10 popular books**:

| # | Title |
|---|-------|
| 1 | Atomic Habits |
| 2 | Rich Dad Poor Dad |
| 3 | The Alchemist |
| 4 | Think and Grow Rich |
| 5 | How to Win Friends and Influence People |
| 6 | The Psychology of Money |
| 7 | Deep Work |
| 8 | The 7 Habits of Highly Effective People |
| 9 | Start With Why |
| 10 | The Subtle Art of Not Giving a F*ck |

---

## 🗂️ Project Structure

```
library-management-system-python/
│
└── library.py        # Main application file (Library class + CLI logic)
```

---

## 🔧 How It Works (Under the Hood)

The entire system is powered by a single `Library` class with three core data structures:

| Attribute | Type | Purpose |
|---|---|---|
| `name` | `str` | The name of the library |
| `bookList` | `list` | Stores all available book titles |
| `lendDict` | `dict` | Maps borrowed books → borrower names |

**Borrowing logic:** When a book is borrowed, it's added to `lendDict` as `{ "Book Title": "Borrower Name" }`. When returned, it's removed from `lendDict`. The `bookList` itself never shrinks — it always reflects the full catalog.

---

## ⚠️ Known Limitations

- **Data is not persistent** — All changes (added books, borrow records) reset when the program exits. There is no database or file storage.
- **Case-sensitive input** — Book titles must be typed exactly as they appear.
- **Single-copy tracking** — The system assumes one copy per book title.

---

## 🛠️ Possible Future Improvements

- [ ] Save data to a JSON or SQLite database for persistence
- [ ] Case-insensitive book search
- [ ] Support for multiple copies of the same book
- [ ] Due dates and overdue tracking
- [ ] A graphical user interface (GUI) or web interface

---

## 🧑‍💻 by Author

This project is a form of my final Python OOP course project. There are still many things to improve.
Feel free to fork, improve, and make it your own!
**README.md is written by Claude AI with an engineered prompt. Thanks to Claude AI for helping me.**

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
