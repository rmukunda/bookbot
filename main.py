# print("greetings boots")
import sys
from stats import get_book_word_count, count_characters, sort_dict

def get_book_text(path):
    with open(path, "r") as f:
        return f.read() 


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = (get_book_word_count(book_text))
    header = f'''
============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ---------  '''
    print(header)
    print(f"Found {num_words} total words")
    num_chars = count_characters(book_text)
    sorted_chars = sort_dict(num_chars)
    for char in sorted_chars:
        if not char['char'].isalpha():
            continue
        print(f"{char['char']}: {char['num']}")



if __name__ == "__main__":
    main()