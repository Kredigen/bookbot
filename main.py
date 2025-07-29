from stats import count_words
from stats import count_char
from stats import sort
import sys


def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
    return file_contents   

def main():
    text = get_book_text(sys.argv[1])
    word_count  = count_words(text) 
    character_count = count_char(text)
    sorted_chars = sort(character_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]} ...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words ")
    print("--------- Character Count -------")
    for dictionary in sorted_chars:
        # dictionary is now one of the dictionaries from the list
        character = dictionary["char"]
        count = dictionary["num"]
        print(f"{character}: {count}")
    print("============= END ===============")

if len(sys.argv) == 2:
    main()
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)