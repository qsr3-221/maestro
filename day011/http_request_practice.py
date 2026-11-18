import requests
response = requests.get("https://httpbin.org/get")
print(response.status_code)
print(type(response))
print(type(response.status_code))
# 响应头里的 Content-Type
print(response.headers["content-type"])

# 原始 body 前 100 字符
print(response.text[:100])

# 解析 JSON
data = response.json()
print(type(data))
print(data.keys())