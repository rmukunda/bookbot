def get_book_word_count(str):
    return len(str.split())

def count_characters(str):
    charmap = {}
    for c in str:
        c = c.lower()
        if c in charmap:
            charmap[c] += 1
        else:
            charmap[c] = 1
    return charmap

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    char_dict = []
    for k,v in dict.items():
        char_dict.append({"char":k, "num":v}) 
    char_dict.sort(reverse = True, key=sort_on)
    return char_dict