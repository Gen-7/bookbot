from stats import get_num_words
from stats import count_character
from stats import sort_character

# Reads entire book into memory at once since we need the complete text
# for accurate word count and the file size is manageable
def get_book_text(filepath):
    with open(filepath) as book:
        book_contents = book.read()
    return book_contents

# Coordinates the program flow by keeping functions separate and focused:
# get_book_text handles file operations while get_word_count focuses on text analysis
def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    num_char = count_character(book_text)
    sorted_char_counts = sort_character(num_char)

    # Title section
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    # Word count section
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Character count section
    print("--------- Character Count -------") 
    
    # Loop through the sorted list of dictionaires and print each key-value pair from largets to smallest
    for char_dict in sorted_char_counts:
        for char, count in char_dict.items(): #Unpack the single key-value pair
            if char.isalpha(): # Skip non-alphabetical characters
                print(f"{char}: {count}")
    
    # Footer section
    print("============= END ===============")

# Guards against running main() if this file is imported as a module
if __name__ == "__main__":
    main()