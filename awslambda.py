import requests

url = 'https://ygyofmvymi.execute-api.us-east-1.amazonaws.com/default/pyth'
myobj = {'TOKEN': 'Hazem'}


x = requests.post(url, data = myobj, headers = {'TOKEN': 'Hazem'})

print(x.text)
