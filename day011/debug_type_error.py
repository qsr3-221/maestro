# 题 1：按键比较
scores = {"alice": 90, "bob": 85, "carol": 95}
# 预测输出：______
print(max(scores.items(), key=lambda x: x[0]))

# 题 2：按值比较
scores = {"alice": 90, "bob": 85, "carol": 95}
# 预测输出：______
print(max(scores.items(), key=lambda x: x[1]))

# 题 3：按值找最大值，但数字相同时按键比
data = [("a", 5), ("b", 5), ("c", 3)]
# 预测输出：______
print(max(data, key=lambda x: x[1]))

