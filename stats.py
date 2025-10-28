def get_num_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def get_character_count(book_text):
    character_count = {}
    lower_text = book_text.lower()
    for c in lower_text:
        if c in character_count:
            character_count[c] += 1
        else:
            character_count[c] = 1
    return character_count

def sort_characters(character_count):
    paired_characters = []
    for k in character_count:
        pair = {"char": k, "num": character_count[k]}
        paired_characters.append(pair)
    paired_characters.sort(reverse=True,key=sort_on)
    return paired_characters

def sort_on(items):
    return items["num"]