import json

with open("front/pages/test.json", 'r') as js:
     data = json.load(js)


print(data['results'][0])