import sys
from stats import get_num_words
from stats import count_character
from stats import sort_character

# Reads entire book into memory at once since we need the complete text
# for accurate word count and the file size is manageable
def get_book_text(filepath: str) -> str:
    with open(filepath) as book:
        book_contents = book.read()
    return book_contents

# Coordinates the program flow by keeping functions separate and focused:
# get_book_text handles file operations while get_word_count focuses on text analysis
def main():
    # Checks if there are 2 entries total
    if len(sys.argv) != 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    num_char = count_character(book_text)
    sorted_char_counts = sort_character(num_char)

    # Title section
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")

    # Word count section
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Character count section
    print("--------- Character Count -------") 
    
    # Print character counts in descending order, alphabetical characters only
    for char, count in sorted_char_counts:
        if char.isalpha():
            print(f"{char}: {count}")
    
    # Footer section
    print("============= END ===============")

# Guards against running main() if this file is imported as a module
if __name__ == "__main__":
    main()