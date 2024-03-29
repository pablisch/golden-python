def make_snippet(string):
    space = ' '
    words_list = string.split(' ')
    if len(words_list) <= 5:
        return space.join(words_list)
    five_words_list = words_list[0:5]
    five_word_string = space.join(five_words_list)
    return five_word_string + '...'