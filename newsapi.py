import requests
import secrets as NEWSAPI_KEY

base_url = 'https://newsapi.org/v2/top-headlines'
params = {"apiKey": NEWSAPI_KEY, "q": "covid"}
response = requests.get(base_url, params)
result = response.json()
articles_list = result['articles']

for dict in articles_list:
    print(dict['source']['name'], dict['title'])

print("Hello, World!")
