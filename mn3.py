import json

a = {"name" : "GeeksforGeeks", "Topic" : "Json to String", "Method": 1}

print(type(a))
y = json.dumps(a)
print(y)
print(type(y))
