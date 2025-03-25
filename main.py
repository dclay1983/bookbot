import sys
from stats import word_count, char_count, sort_chars
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    book_text = get_book_text(book)
    count = word_count(book_text)
    char = char_count(book_text)
    sorted_chars = sort_chars(char)
    print("""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
""")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for c in sorted_chars:
        print(f"{c["char"]}: {c["value"]}")
    print("============= END ===============")

main()

