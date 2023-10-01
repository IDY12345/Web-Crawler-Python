import requests

def fetchAndSaveToFile(url,path):
    r=requests.get(url)
    with open(path,"w") as f:
        f.write(r.text)

url="https://books.toscrape.com/"

r=requests.get(url)
print(r.text)


fetchAndSaveToFile(url,"data/times.html")