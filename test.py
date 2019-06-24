import requests
import json
import ast

token = '2e25df4dfd8b5187937cf6f842ad066113ed949b'
url_pulls = 'https://api.github.com/repos/alenaPy/devops_lab/pulls'
url = 'https://api.github.com/users'
url1 = 'https://api.github.com/users/'
headers = {'Authorization': 'token %s' % token}
r = requests.get(url_pulls, headers=headers)
a = r.json()

print(a[0]['id'],'\n',a[1])
