from stats import print_report
from stats import get_num_words
from stats import get_num_chars
import sys

def get_book_text(path):
    with open(path) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    contents = get_book_text(path)
    num_words = get_num_words(contents)
    char_dict_list = get_num_chars(contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print_report(char_dict_list)
    print("============= END ===============")
    sys.exit(0)


if __name__ == '__main__':
    main()
