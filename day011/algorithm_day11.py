# 题 1：按键比较
scores = {"alice": 90, "bob": 85, "carol": 95}
# 预测输出：('carol': 95)   ← 格式错，元组用逗号
# 实际输出：('carol', 95)   ← 按键比，'carol' > 'bob' > 'alice'
print(max(scores.items(), key=lambda x: x[0]))

# 题 2：按值比较
scores = {"alice": 90, "bob": 85, "carol": 95}
# 预测输出：('carol': 95)   ← 格式错
# 实际输出：('carol', 95)   ← 按值比，95 > 90 > 85
print(max(scores.items(), key=lambda x: x[1]))

# 题 3：按值找最大值，值相同时 max 返回第一个遇到的
data = [("a", 5), ("b", 5), ("c", 3)]
# 预测输出：('a', 5)
# 实际输出：('a', 5)        ← 5 和 5 相同，max 保留先出现的 'a'
print(max(data, key=lambda x: x[1]))