def get_book_text(path_to_file):
    #converts the text of a file to a string to be compatible with other functions
    try:
        with open(path_to_file) as f:
            book_text = f.read()
        return book_text
    except FileNotFoundError:
        print(f"Error: {path_to_file} not found.")

def get_num_words(book_text):
    #gets the number of words in a string
    words = book_text.split()
    word_count = len(words)
    return word_count

def get_character_count(book_text):
    #creates a dictionary of all characters within a string in order of first appearance 
    #and in a format of {"c1": number1, "c2": number2}
    all_lower = book_text.lower()
    character_count = {}

    for c in all_lower:
        character = c
        count = all_lower.count(c)

        if c not in character_count:
            character_count[f"{c}"] = count

    return character_count

def sort_on(dict):
    #tells the sort method in sort_character_count to use the number of instances of a character as what to sort by
    return dict["count"]

def sort_character_count(character_count):
    #Creates a list of dictionaries in the format of {"character": character, "count": number of times the character occurs}
    #then sorts from most to least occurances
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

def format(book_location, num_words, dictionary_list):
    #outputs results of analysis in a pretty layout
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for dictionary in dictionary_list:
        character = dictionary["character"]
        number = dictionary["count"]
        label = f"{character}: {number}"
        print(label)

    print("============= END ===============")
