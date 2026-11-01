def count_words(text):
    words = text.split()
    d = {}
    for word in words:
        d[word] = d.get(word, 0) + 1
    return d
if __name__ == "__main__":
    print(count_words("a b a c a b"))