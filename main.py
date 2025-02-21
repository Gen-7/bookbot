def get_book_text(filepath):
    with open(filepath) as book:
        book_contents = book.read()
    return book_contents

def main():
    print(get_book_text("books/frankenstein.txt"))

if __name__ == "__main__":
    main()