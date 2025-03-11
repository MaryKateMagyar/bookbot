def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def word_count(book_text):
    words = book_text.split()
    num_of_words = len(words)
    return num_of_words

def main():
    book_text = get_book_text("books/frankenstein.txt")
    #print(book_text)
    num = word_count(book_text)
    print(f"{num} words found in the document")

main()