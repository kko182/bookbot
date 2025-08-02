import sys  # sys is used to access command-line arguments

# Import functions from the stats module
from stats import (
    word_count,
    char_count,
    sorted_list,
    average_word_length,
    sentence_count,
    average_sentence_length
)

def get_book_text(path_to_file):
    # Open the file at the given path and read its contents
    with open(path_to_file) as f:
        file_contents = f.read()  # Read the entire file into a string
    return file_contents  # Return the text content of the file

def main():
    """
    Main function to run the BookBot text analyzer.
    It reads a book file, performs multiple analyses, and prints a report.
    """

    # Check if the correct number of arguments was provided (1 argument + script name)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")  # Show usage if incorrect
        sys.exit(1)  # Exit with an error code

    # Get the text content from the book file
    text = get_book_text(sys.argv[1])

    # Count the total number of words in the text
    count = word_count(text)
    
    # Create a dictionary with character counts
    chars_dict = char_count(text)
    
    # Convert the character dictionary to a sorted list
    chars_list = sorted_list(chars_dict)
    
    # === Output the report ===
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    
    # --- Word Count Section ---
    print("----------- Word Count ----------")
    print(f"Found {count} total words") # Output the total word count
    
    # --- Sentence & Word Stats Section ---
    print("------ Sentence & Word Stats ----")
    print(f"Sentence count: {sentence_count(text)}") # Number of sentences
    print(f"Average sentence length: {average_sentence_length(text):.2f} words") # Avg words per sentence
    print(f"Average word length: {average_word_length(text):.2f} characters") # Avg chars per word

    # --- Character Frequency Section ---
    print("--------- Character Count -------")
    # Loop through each character in the sorted list
    for char_info in chars_list:
        char = char_info["char"]  # Extract the character
        num = char_info["num"]    # Extract the count
        if char.isalpha():        # Only print alphabetical characters (skip spaces, punctuation, etc.)
            print(f"{char}: {num}") # Output each character's frequency
    
    # Print the report footer
    print("============= END ===============")

# Call the main function to run the program
main()
