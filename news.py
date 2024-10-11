api_key="84e62be03d2e4090b7b4a5b069cad710"
import requests
import json
from datetime import date

query=input("What news are you interested in? ")
url=f"https://newsapi.org/v2/top-headlines?q={query}&from={date.today()}&sortBy=popularity&apiKey={api_key}"
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