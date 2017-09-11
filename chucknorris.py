import requests

r = requests.get('http://api.icndb.com/jokes/random')


data = r.json()

print("joke #{}".format(data['value']['id']))
print(data['value']['joke'])

# print(type(r.json()))

