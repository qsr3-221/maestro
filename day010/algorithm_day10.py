words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
repeated = [word for word, count in counts.items() if count >= 2]
print(counts)
print(repeated)
scores = {"a": 3, "b": 7, "c": 5}
max_key = max(scores, key=scores.get)
max_items = max(scores.items(), key=lambda x: x[1])
print(max_key)
print(max_items)