def reverse_words(text):
    s = text.split(' ')  # split the string into a list of words
    w = []

    for i in s:
        w.append(i[::-1])

    return " ".join(w)