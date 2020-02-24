import requests

# url = 'http://httpbin.org/get'

# params = {'name1': 'value1', 'name2': 'value2'}
# headers = {'User-agent': 'none/ofyourbusiness', 'Spam': 'Eggs'}

# resp = requests.get(url, params=params, headers=headers)
# print(resp.content, '\n', resp.content.decode('utf-8'))
# print('-' * 70)

# print(resp.text)
# print('-' * 70)

# print(resp.json)

# # print('-' * 70)

# # resp1 = requests.get('http://www.python.org/index.html')
# # print(resp1.status_code, '\n', resp1.headers)
# # https://requests.readthedocs.io/en/master/api/

# print('-' * 70)

# files = {'file': ('tmp\data.json', open('tmp\data.json', 'rb'))}
# resp = requests.post(url, files=files)
# print(resp.text)

# print('-' * 70)


url = 'http://httpbin.org/get?name=Dave&n=37'
headers = {'User-agent': 'goaway/1.0'}
resp = requests.get(url, headers=headers).json()
print(resp)
print(resp['headers'])
print(resp['args'])
