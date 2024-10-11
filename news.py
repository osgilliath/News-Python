api_key="" #Enter your api key
import requests
import json

query=input("What news are you interested in? ")
url=f"https://newsapi.org/v2/top-headlines?q={query}&from=2024-09-11&sortBy=popularity&apiKey={api_key}"
r=requests.get(url)
news=json.loads(r.text)
i=1
for article in news["articles"]:
    if article["title"]=="[Removed]" or article["description"]==None:
        continue
    else:
        print(f'{i}.{article["title"]}')
        print(article["description"])
        print("----------------------------------------------------------------------")
        i+=1
