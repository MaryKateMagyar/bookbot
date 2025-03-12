import stats as s

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_location ="books/frankenstein.txt"
    book_text = get_book_text("books/frankenstein.txt")
    #book_location = "books/test.txt"
    #book_text = get_book_text("books/test.txt")
    #print(book_text)
    word_count = s.get_num_words(book_text)
    #print(f"{word_count} words found in the document")
    character_count = s.get_character_count(book_text)
    dictionary = s.split_character_count(character_count)
    formatted_characters =s.format(book_location, word_count, dictionary)
    return formatted_characters

main()