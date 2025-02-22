from stats import get_num_words

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
    print(f"{num_words} words found in the document")

# Guards against running main() if this file is imported as a module
if __name__ == "__main__":
    main()