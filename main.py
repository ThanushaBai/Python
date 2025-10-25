#dictionary - collection of unique value pairs


capitals ={'usa':'washington',
           'india':'new delhi',
           'china':'chicago',
           'russia':'moscow'}

capitals.update({"germany":"berlin"})
capitals.update({'usa':'las vegas'})

capitals.pop('usa')
capitals.clear()

print(capitals['usa'])
print(capitals['india'])
print(capitals['china'])
print(capitals['russia'])

print(capitals.get('germany')) #none
print(capitals.get('china'))   #chicago

print(capitals.keys())
print(capitals.values())

print(capitals.items())

for key, value in capitals.items():
    print(key, value)