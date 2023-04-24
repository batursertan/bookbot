




def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dict = get_char_dict(text)
    char_sorted_list = char_dict_to_sorted_list(char_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")  
    print()
    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"the '{item['char']}' character was found {item['num']} times")
    


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):  
    words = text.split()
    return len(words)

def get_char_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def char_dict_to_sorted_list(num_char_dict):
    sorted_list = [{"char": ch, "num": num_char_dict[ch]} for ch in num_char_dict]
    sorted_list.sort(reverse=True, key=lambda x: x["num"])
    return sorted_list
   
   





main()