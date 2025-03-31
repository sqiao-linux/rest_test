import requests
#api_url = "https://jsonplaceholder.typicode.com/todos"
api_url = "http://api.open-notify.org/astros.json"
response = requests.get(api_url)
print(response.status_code)
print(response.json())
