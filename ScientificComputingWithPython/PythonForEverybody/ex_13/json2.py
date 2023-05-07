import json

print("PY4E - Exercise 13.2")

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
print('\nUser count:', len(info))

for item in info:
    print('\nName', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
