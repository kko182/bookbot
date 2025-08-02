def word_count(text):
    # Split the text by whitespace and count the resulting words
    return len(text.split())

def char_count(text):
    count = {}  # Initialize an empty dictionary to store character counts
    # Loop through each character in the text (converted to lowercase)
    for i in text.lower(): 
        if i in count:      # If character already exists in dictionary
            count[i] += 1   # Increment its count
        else:               # If character doesn't exist in dictionary
            count[i] = 1    # Add it with a count of 1
    
    return count  # Return the dictionary of character counts

def sort_on(dict_item):
    # Helper function that returns the "num" value from a dictionary
    # This is used as the key for sorting
    return dict_item["num"]

def sorted_list(text):
    chars_list = []  # Initialize an empty list to store character dictionaries
    # Loop through each character and count pair in the input dictionary
    for char, count in text.items():
        # Create a dictionary for each character with its count
        char_dict = {"char": char, "num": count}
        chars_list.append(char_dict)  # Add the dictionary to the list
    
    # Sort the list in descending order (highest count first) using the sort_on function
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list  # Return the sorted list of character dictionaries

