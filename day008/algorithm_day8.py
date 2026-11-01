nums = [1, 2, 3, 4, 5]
squares = [num * num for num in nums]
print(squares)
text = "apple banana apple cherry banana apple"
dl = text.split()
counts = {}
for d in dl:
    counts[d] = counts.get(d, 0) + 1
print("题目2统计字典:", counts)
print("题目2出现最多的:", max(counts, key=counts.get)) 