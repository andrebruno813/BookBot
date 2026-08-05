# 📚 BookBot

BookBot is a text analysis tool developed in Python as part of the [Boot.dev](https://www.boot.dev) backend development curriculum.

The application reads a book text file and generates a statistical report containing the total number of words and the frequency of each character found in the document.

This project was created to practice fundamental Python concepts, including file handling, string manipulation, dictionaries, lists, sorting algorithms, and code organization.

---

## 🚀 Features

- Read and process text files
- Count the total number of words in a book
- Analyze character frequency
- Sort characters by occurrence
- Generate a formatted text report
- Ignore non-alphabetic characters in the final analysis

---

## 🛠️ Technologies Used

- Python 3
- File I/O
- Dictionaries (`dict`)
- Lists and tuples
- Custom sorting functions
- Modular programming

---

## 📂 Project Structure

```
bookbot/
│
├── main.py          # Application entry point
├── stats.py         # Text analysis functions
├── books/            # Text files used for analysis
│   └── frankenstein.txt
│
└── README.md
```

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/bookbot.git
```

Navigate to the project directory:

```bash
cd bookbot
```

Run the program:

```bash
python3 main.py books/frankenstein.txt
python3 main.py books/mobydick.txt
...
```

---

## 📊 Example Output

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...

----------- Word Count ----------
Found 75767 total words

--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494

============= END ===============
```

---

## 📚 Concepts Practiced

- Reading and processing files
- String manipulation
- Dictionary-based counting
- List sorting using custom keys
- Modular Python programming
- Separation of concerns

---

## 🧠 What I Learned

- How to structure a small Python project into separate, reusable modules
- How to design functions that transform raw data into readable reports
- Practical use of dictionaries for frequency counting
- How to write custom sort keys to order results meaningfully
- The importance of clean, modular code organization for maintainability

---

## 👨‍💻 Author

**Bruno André**
Telecommunications Engineering student · 42 Luanda student