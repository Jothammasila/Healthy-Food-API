import requests as re


url = 'http://127.0.0.1:8000/foods'
response = re.get(url)

print(response.json())