import stats
import sys

def main():
    book_location = sys.argv[1]
    book_text = stats.get_book_text(book_location)
    num_words = stats.get_num_words(book_text)
    character_count = stats.get_character_count(book_text)
    dictionary = stats.sort_character_count(character_count)

    stats.format(book_location, num_words, dictionary)


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()