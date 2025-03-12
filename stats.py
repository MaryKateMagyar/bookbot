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
            character_count[f"{c}"] = count

    return character_count

def sort_on(dict):
    return dict["count"]

def split_character_count(character_count):
    dictionary_list = []

    for character in character_count:
        if character.isalpha() == True:
            dictionary = {}
            number = character_count[character]
            dictionary["character"] = character
            dictionary["count"] = number
            dictionary_list.append(dictionary) 

    dictionary_list.sort(reverse=True, key=sort_on)

    return dictionary_list

def format(book_location, word_count, dictionary_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for dictionary in dictionary_list:
        character = dictionary["character"]
        number = dictionary["count"]
        label = f"{character}: {number}"
        print(label)

    print("============= END ===============")
