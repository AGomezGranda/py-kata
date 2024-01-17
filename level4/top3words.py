import re

def top_3_words(text):
    clean_text = re.sub(r"(?<!\w)'(?!\w)|[^A-Za-z']+", ' ', text.lower())
    words = clean_text.split()
    count = dict()

    for word in words:
        count[word] = count.get(word, 0) + 1

    # It would be more efficient if uses list comprenhensions
    lst = sorted([(v, k) for k, v in count.items()], reverse=True)
    new_list = [v for k, v in lst[:3]]

    """
    Basic method:

        lst = list()
        for k, v in count.items():
            new_tuple = (v, k)
            lst.append(new_tuple)

        lst = sorted(lst, reverse=True)

        new_list = []
        for k, v in lst[:3]:
            new_list.append(v)
            print(new_list)
    """

    return new_list
