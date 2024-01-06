

def main():
    
    frank_path = "books/frankenstein.txt"
    frank_text = get_book_text(frank_path)
    frank_num_words = get_num_words(frank_text)

    letter_count_dict = create_letter_count_dict(frank_text)

    

    print_report(frank_text, letter_count_dict)







def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)


def create_letter_count_dict(text):
    lowered = text.lower()
    l_dict = {}
    for char in lowered:
        if char in l_dict:
            l_dict[char] += 1
        else:
            l_dict[char] = 1
    return l_dict
    

def print_report(text, dict):
    print("--------------report begin------------")                                                                                                     
    print(f"This text consist of {get_num_words(text)} number of words")
    for char in dict:
        if char.isalpha() == False:
            continue
        count = dict[char]
        print(f"Character {char} was found {count} times")
    print("--------------report end----------------")









main()