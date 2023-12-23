def spin_words(sentence):
    new_sentence = ""
    word = sentence.split()
    for i in word:
        if len(i) >= 5:
            new_word = i[::-1]
            # new_sentence = new_sentence + ' ' + new_word
            new_sentence = '{} {}'.format(new_sentence, new_word)
        else:
            # new_sentence = new_sentence + ' ' + i
            new_sentence = '{} {}'.format(new_sentence, i)
    return new_sentence.strip()

# Other solution, more efficient
def spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
