import json
text = '{"id": 1, "title": "a"}'
data = json.loads(text)
print(type(data))
print(data["title"])
print(data.to_dict())