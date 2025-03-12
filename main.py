import stats as s
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_location = sys.argv[1]
    book_text = get_book_text(book_location)
    word_count = s.get_num_words(book_text)
    character_count = s.get_character_count(book_text)
    dictionary = s.split_character_count(character_count)
    formatted_characters =s.format(book_location, word_count, dictionary)
    return formatted_characters

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()