import json


with open('object.json', 'r') as file:
    data = json.load(file)


for ex5 in data:
    if ex5['name'] == 'Old Fashioned':
       
       
        ex5['batters']['batter'].append({'id': str(int(ex5['batters']['batter'][-1]['id']) + 1), 'type': 'Coffee'})
        break  
   
with open('object.json', 'w') as file:
    json.dump(data, file, indent=4)