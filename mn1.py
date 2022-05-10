import json
dict = '{"name" : "ayushi","subject" : "json","city" : "ktg","phone" : 9984758787}'
print(type(dict))
py = json.loads(dict)
print(py)
print(type(py))
print(py["subject"])
print(py["city"])
print(py["phone"])