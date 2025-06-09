from collections import OrderedDict
def count_words(words):
    word_count = OrderedDict()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return len(word_count), list(word_count.values())
