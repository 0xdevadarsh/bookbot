def count_words_in_string(string, delimiter=None):
    words_list = string.split(sep=delimiter)
    return len(words_list)

def count_characters_in_string(string):
    char_dict = {}
    lowercased_string = string.lower()
    for char in lowercased_string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def sort_on(items):
    return items["num"]

def helper(dict):
    char_count_list = []
    for key, val in dict.items():
        char_count = {
            "char": key,
            "num": val
        }
        char_count_list.append(char_count)

    char_count_list.sort(reverse=True, key=sort_on)
    return char_count_list
