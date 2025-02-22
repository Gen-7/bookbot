# Reads entire book into memory at once since we need the complete text
# for accurate word count and the file size is manageable
def get_book_text(filepath):
    with open(filepath) as book:
        book_contents = book.read()
    return book_contents

# Uses whitespace (spaces, tabs, newlines) to identify word boundaries,
# which works well for English text. split() without arguments 
# treats multiple spaces the same as one space for accurate word counting
def get_word_count(book):
    words = book.split()
    num_words = len(words)
    return num_words

# Coordinates the program flow by keeping functions separate and focused:
# get_book_text handles file operations while get_word_count focuses on text analysis
def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_word_count(book_text)
    print(f"{num_words} words found in the document")

# Guards against running main() if this file is imported as a module
if __name__ == "__main__":
    main()