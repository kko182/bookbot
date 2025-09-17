# 📚 BookBot

BookBot is a Python command-line tool for analyzing text files (such as eBooks).  
It provides statistics like word and sentence counts, average lengths, character frequencies, and the most common words.

---

## ✨ Features

- 📖 Word count and character frequency  
- 📝 Sentence count and average sentence length  
- 🔠 Average word length (in characters)  
- 📊 Sorted character usage report (A–Z)  
- 🏆 Top N most common words (`--top` flag)  

---

## ▶️ Usage

Run the program with a text file as input:

python main.py path/to/book.txt


Example:

python main.py books/frankenstein.txt

Options

--top N → Show the top N most common words (default: 20)

Example:

python main.py books/frankenstein.txt --top 50

---

## 📊 Example Output
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...

----------- Word Count ----------
Found 78,532 total words

------ Sentence & Word Stats ----
Sentence count: 4,562
Average sentence length: 17.22 words
Average word length: 4.57 characters

--------- Top 20 Words ----------
the: 5321
and: 4102
to: 3795
...

--------- Character Count -------
a: 45321
b: 3812
c: 5123
...

============= END ===============

---

## 🛠 Project Structure
bookbot/
│── main.py        # Entry point for CLI usage
│── stats.py       # Text analysis helper functions
│── README.md      # Documentation

---

## 📜 License

MIT License. Free to use, modify, and share.

---

## 🚀 Installation

Clone the repository and navigate into it:

```bash
git clone https://github.com/kko182/bookbot.git
cd bookbot
