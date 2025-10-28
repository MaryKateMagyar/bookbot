from stats import get_num_words, get_character_count, sort_characters
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    character_count = get_character_count(book_text)
    sorted_characters = sort_characters(character_count)

    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")
    for c in sorted_characters:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")
    

def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
        return book_text

    
main()