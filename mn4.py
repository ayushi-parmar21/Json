import json
str = {'4': 5, '6': 7, '1': 3, '2': 4}
print("Original String:")
print(str)
print("\nJSON data:")
print(json.dumps(str, sort_keys=True))
    