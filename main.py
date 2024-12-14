# TODO 1:
# - Use a main function to wrap the logic and call main() at the bottom of your file 
#   to execute your program.
# - Change main.py so that instead of printing "hello world", it reads the contents 
#   of the "frankenstein.txt" and prints it all to the console.

def main():
    book_path = "books/frankenstein.txt"
    text = read_file(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("\nCharacter counts:")
    print_character_count(character_count)
    print(f"--- End report ---")

# TODO 2:
# - Add a new function to your script that takes the text from the book as a string, and returns the number of words in the string.

def get_word_count(text):
    words = text.split()
    return len(words)

def read_file(filepath):
    with open(filepath) as f:
        return f.read()
    
# TODO 3:
# - Add a new function to your script that takes the text from the book as a string, 
#   and returns the number of times each character appears in the string. Convert any 
#   character to lowercase, we don't want duplicates.

def get_character_count(text):
    text = text.lower()
    character_count = {}
    for char in text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def print_character_count(character_count):
    # Sort by count (highest occurrence first) saved for later use
    # sorted_chars = sorted(character_count.items(), key=lambda x: x[1], reverse=True)

    # Sort by using a lambda function that takes each key-value tuple (x) and returns the value (x[1])
    # This makes the sort compare the counts rather than the characters themselves
    # Sort alphabetically (a to z)
    sorted_chars = sorted(character_count.items(), key=lambda x: x[0])
    for char, count in sorted_chars:
        if char.isalpha():  # Only print alphabetic characters
            print(f"The '{char}' character was found {count} times")

# This conditional check ensures the code only runs when the script is executed directly
# (not when imported as a module). When Python runs a file, it sets the special __name__ 
# variable to "__main__" if it's the main program being run. If the file is being 
# imported by another module, __name__ will be set to the module's name instead.
#
# Using this conditional is better than directly calling main() because:
# 1. It prevents code from running automatically if this file is imported as a module
# 2. It allows the same file to be both imported and run as a script
# 3. It's a common Python pattern that makes code more modular and reusable
# 4. It helps avoid unintended side effects when testing or importing functions
if __name__ == "__main__":
    main()

