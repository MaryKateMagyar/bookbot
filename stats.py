def get_num_words(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

def get_character_count(book_text):
    all_lower = book_text.lower()
    character_count = {}

    for c in all_lower:
        character = c
        count = all_lower.count(c)

        if c not in character_count:
            character_count[f"{c}"] = f"{count}"

    return character_count


