nums = [1, 2, 3, 4, 5, 6]
count = 0
total = 0
for n in nums:
    if n % 2 == 0:
        count += 1
        total  += n
print(f"偶数个数:{count}")
print(f"偶数和:{total }")
