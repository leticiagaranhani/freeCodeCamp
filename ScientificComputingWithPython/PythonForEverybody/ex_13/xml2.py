import xml.etree.ElementTree as ET
print("PY4E - Exercise 13.4")
input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('\nName', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))
