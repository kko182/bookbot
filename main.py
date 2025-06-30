import sys
import string

def count_letters(text):
    # Convert text to lowercase
    text = text.lower()
    # Create a dictionary to hold letter frequencies
    letter_counts = {char: 0 for char in string.ascii_lowercase}

    # Count each letter
    for char in text:
        if char in letter_counts:
            letter_counts[char] += 1

    return letter_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    try:
        with open(book_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at '{book_path}'")
        sys.exit(1)

    counts = count_letters(text)

    for letter in sorted(counts):
        print(f"{letter}: {counts[letter]}")

if __name__ == '__main__':
    main()

