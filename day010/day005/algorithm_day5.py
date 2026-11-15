def top_word(text):
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word,0) + 1
    for k, v in counts.items():
        print(f"{k}: {v}")
    max_word=max(counts, key=counts.get)
    return max_word,counts[max_word]
if __name__ == "__main__":
    print(top_word("a b a c a b"))