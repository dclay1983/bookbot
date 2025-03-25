def word_count(text):
    return len(text.split())

def char_count(text):
    char = {}
    for c in text:
        c = c.lower()
        char[c] = char[c] + 1 if c in char else 1
    return char

def sort_chars(char_dict):

    def comp(dict):
        return dict["value"]

    list = []
    for c, v in char_dict.items():
        if c.isalpha():
            list.append({"char": c, "value": v})

    list.sort(key=comp, reverse=True)
    return list
