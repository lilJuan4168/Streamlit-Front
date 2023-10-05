import json

with open("front/pages/test2.json", 'r') as js:
     data = json.load(js)


with open("front/pages/json3.json", 'w') as js2:
     json.dump(data, js2)


print(data['results'][0])