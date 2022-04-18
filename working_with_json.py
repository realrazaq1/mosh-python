import json
from pathlib import Path

f = open("names.json")
# json to python object(list)
names = json.loads(f.read())
names.append("faith")
print(names)
# python object(list) to json
print(json.dumps({'name': 'raz', 'age': 20}))
