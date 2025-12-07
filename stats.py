def get_num_words(text):
    words_list = list(text.split())
    print(f"Found {len(words_list)} total words")


def get_num_char(text):

    # Split the text into words
    words_list = list(text.split())

    # Create empty dict
    char_count = {}

    for word in words_list:
        # Loop each character in a word
        for char in word:
            # Count the characters in the word
            std_char = char.lower()

            if std_char in char_count:
                char_count[std_char] = char_count[std_char] + 1
            else:
                char_count[std_char] = 1

    return char_count


def convert_dict_to_listdict(num_char_dict):
    """
    Converts num_char_dict dictionary into a list of dictionaries,
    each containing the character and its number of occurences

    :param num_char_dict: dictionary of characters and their number of occurrences
    """
    num_char_list = []

    for char in num_char_dict:
        num = num_char_dict[char]

        num_char_list.append({"char": char, "num": num})

    return num_char_list


def get_num(num_char_list):
    # Helper function to get the number of occurrences of a character
    return num_char_list["num"]


def sort_num_char(num_char_dict):
    """
    Converts the dictionary into a list of dictionary and then sorts
    based on the number of occurrences of the character

    :param num_char_dict: dictionary of characters and their occurrences
    """
    listdict = convert_dict_to_listdict(num_char_dict)

    # Sort the list of dictionaries by number of occurences, from greatest to lowest number of occurrences
    listdict.sort(reverse=True, key=get_num)
    return listdict
