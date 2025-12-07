import sys
from stats import get_num_words
from stats import get_num_char
from stats import sort_num_char


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")

    # Get the book text
    book_text = get_book_text(f"{file_path}")
    print("----------- Word Count ----------")
    get_num_words(book_text)
    print("--------- Character Count -------")

    # Print the sorted list
    sorted_list = sort_num_char(get_num_char(book_text))

    for item in sorted_list:
        # Skip if it is not an alphabetical (a-z) character
        if not item["char"].isalpha():
            continue

        print(f'{item["char"]}: {item["num"]}')

    print("============= END ===============")


main()
