import sys
from stats import count_words_in_string, count_characters_in_string, helper

def get_book_text(file_path):
    with open(file_path) as file_ptr:
        file_contents = file_ptr.read()
    return file_contents

def main(file_path):
    book_content = get_book_text(file_path)
    words_count = count_words_in_string(book_content)
    char_count = count_characters_in_string(book_content)
    char_count_list = helper(char_count)
    print("=================== BOOKBOT ====================")
    print(f"Analyzing book found at {file_path}")
    print("------------------- Word Count -----------------")
    print(f"Found {words_count} total words")
    print("-------------- Character Count -----------------")
    for char_count in char_count_list:
        char = char_count["char"]
        count = char_count["num"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("=================== END =======================")

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])