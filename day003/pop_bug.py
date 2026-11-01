nums = [10, 20, 30]
idx = int(input("index: "))
if 0<= idx < len(nums):
    x = nums.pop(idx)
    print(x)
    print(nums)
else:
    print("索引超出范围")