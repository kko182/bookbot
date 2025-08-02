import sys

# Import functions from the stats module
from stats import word_count
from stats import char_count
from stats import sorted_list

def get_book_text(path_to_file):
    # Open the file at the given path and read its contents
    with open(path_to_file) as f:
        file_contents = f.read()  # Read the entire file into a string
    return file_contents  # Return the text content of the file

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the text content from the book file
    text = get_book_text(sys.argv[1])

    # Count the total number of words in the text
    count = word_count(text)
    
    # Create a dictionary with character counts
    chars_dict = char_count(text)
    
    # Convert the character dictionary to a sorted list
    chars_list = sorted_list(chars_dict)
    
    # Print the report header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    
    # Print word count section
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    
    # Print character count section
    print("--------- Character Count -------")
    # Loop through each character in the sorted list
    for char_info in chars_list:
        char = char_info["char"]  # Extract the character
        num = char_info["num"]    # Extract the count
        if char.isalpha():        # Only print alphabetical characters (skip spaces, punctuation, etc.)
            print(f"{char}: {num}")
    
    # Print the report footer
    print("============= END ===============")

# Call the main function to run the program
main()
