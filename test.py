import requests 

# r = requests.post('http://127.0.0.1:5000/add?chef=kfc&name=pizza&price=400')
# a= r.json() 

# print(a)

r = requests.get('http://127.0.0.1:5000/chef') 
print(r.json())