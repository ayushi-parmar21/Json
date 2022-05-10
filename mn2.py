# python object to json data
import json
# a Python object (dict):
dict = {"name" : "ayushi","subject" : "json","city" : "ktg","phone" : 9984758787}
print(type(dict))
j = json.dumps(dict)
print(j)
print(type(j))