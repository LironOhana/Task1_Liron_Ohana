def revword(word):
    word = word[::-1].lower()
    return word

def countword(fname):
    counter = 1
    PATH = "C:/Users/liron/Downloads/"
    fname = PATH + fname + ".txt"
    text = open(fname)
    text_lst = []
    for line in text:
        line = line.rstrip()
        lst = line.split(" ")
        text_lst.append(lst)
    f_word = text_lst[0][0]
    new_text = [f_word]
    for line in range(1,len(text_lst)):
        new_text.append([])
        for temp_word in text_lst[line]:
            temp_word = revword(temp_word)
            if temp_word == f_word:
                counter+=1
            new_text[line].append(temp_word)
    return counter


print(countword("text"))
