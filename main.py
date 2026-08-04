import sys
from stats import word_count, count_characters, chars_dict_to_sorted_list

def get_book_text(path: str) -> str:
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path:str, w_count: int, sorted_list: list[(str, int)]):

    print("============ BOOKBOT ============")

    print("Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")

    print(f"Found {word_count(get_book_text(book_path))} total words")

    print("--------- Character Count -------")

    for key, value in sorted_list:
        if key.isalpha():
            print(f"{key}: {value}")

    print("============= END ===============")


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    path = sys.argv[1]
    text = get_book_text(path)


    dic = count_characters(text);
    sorted_chars = chars_dict_to_sorted_list(dic);

    print_report(path, word_count(text),sorted_chars )

if __name__ == "__main__":
    main()

