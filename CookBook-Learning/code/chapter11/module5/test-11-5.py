import requests

r = requests.get('http://localhost:8080/hello?name=Guido')
print(r.text)