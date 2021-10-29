import requests
res = requests.post('http://localhost:8000/abc', data = {'key':'value'})
print(res)
