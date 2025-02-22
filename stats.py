# Uses whitespace (spaces, tabs, newlines) to identify word boundaries,
# which works well for English text. split() without arguments 
# treats multiple spaces the same as one space for accurate word counting
def get_num_words(book):
    words = book.split()
    num_words = len(words)
    return num_words