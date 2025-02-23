# Uses whitespace (spaces, tabs, newlines) to identify word boundaries,
# which works well for English text. split() without arguments 
# treats multiple spaces the same as one space for accurate word counting
def get_num_words(book):
    words = book.split()
    num_words = len(words)
    return num_words

#Uses a dictionary and for loop to go through the text of a book
#and count the characters. Adds 1 if a character is already in 
#the dictionary, else sets to 1 if character is not in the dictionary.
def count_character(book):
    char_count = {}
    for char in book:
        char = char.lower()
        if char == '\n': #skip newlines
            continue
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_character(unsorted_char_count):
    count_pairs = unsorted_char_count.items()
    list_of_pairs = list(count_pairs)
    list_of_pairs.sort(key=lambda x: x[1], reverse=True)
    count_dict = [{char: count} for char, count in list_of_pairs]
    return count_dict