def input_read(input):
    clean_input = ""
    result = {}
    word = ""

    for c in input:
        if not c.isalpha() and not c.isspace():
            c = " "
        clean_input += c

    input = clean_input
    clean_input = ""

    for c in input:
        if c.isupper():
            c = c.lower()
        clean_input += c

    for c in clean_input:
        if c.isspace():
            if len(word) > 0:
                if word in result:
                    result.update({word: result.get(word) + 1})
                else:
                    result.update({word: 1})
                word = ""
        else:
            word += c

    if len(word) > 0:
        if word in result:
            result.update({word: result.get(word) + 1})
        else:
            result.update({word: 1})

    return result


print input_read('We came, we saw, we conqueredthen we ate Bill\'s (Mille-Feuille) cake.'
                 'The bill came to five dollars.')
