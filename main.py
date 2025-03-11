from stats import get_num_words
from stats import get_character_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    #print(book_text)
    word_count = get_num_words(book_text)
    print(f"{word_count} words found in the document")
    character_count = get_character_count(book_text)
    print(character_count)

main()