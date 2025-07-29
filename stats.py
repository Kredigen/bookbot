def count_words(book_text):
    #words = book_text.split()
    #total_words = len(words)
    return len(book_text.split()) #optimized

def count_char(book_text):
    lowercase = book_text.lower()
    char_dir = {}
    for char in lowercase:
        if char not in char_dir:
            char_dir[char] = 1
        else:
            char_dir[char] += 1
    return char_dir

def sort(char_dict):
    def sort_on(item):
        return item["num"]
    char_list = []
    for char, num in char_dict.items():
        if char.isalpha():
            new_dict = {"char": char, "num": num}
            char_list.append(new_dict)

    char_list.sort(reverse=True, key=sort_on)
    return char_list