def count_words(text):
    count = 0
    for word in text.split():
        count += 1
    return count

def char_count(text):
    char = {}
    for c in text:
        c = c.lower()
        if c not in char:
            char[c] = 0
        char[c] += 1
    return char

def sort_on(items):
    return items["num"]

def sort_dic(dic):
    mass = []
    for k, v in dic.items ():
        mass.append({"name":k,"num":v})
    mass.sort(reverse=True, key=sort_on)
    return mass

