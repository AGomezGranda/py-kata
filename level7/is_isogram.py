def is_isogram(string):
    # your code here

    word = set()

    for i in string.lower():
        word.add(i)

    return len(string) == len(word)
