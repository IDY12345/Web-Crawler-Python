import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://books.toscrape.com/"

url1="https://www.buddy4study.com/"

r=requests.get(url)

soup=BeautifulSoup(r.text,'html.parser')

data={'Title':[],'Price':[]}
# print(soup.prettify())
articles=soup.select("article.product_prod")
# for article in soup.find_all(class_="product_prod"):
    # titles=soup.find(title="A Light in the Attic")
    # for link in soup.find_all("a"):
        # print(link.get("title"))

re= soup.find_all(class_="col-xs-6")
for r in re :
    for H3 in r.find_all("h3"):
        for link in H3.find_all('a'):
            data["Title"].append(link.get('title'))
            # print(link.get('title'))

for r in re:
    for price in r.find_all(class_="product_price"):
        for value in price.find_all(class_="price_color"):
            data["Price"].append(value.get_text())
            # print(value.get_text())
        
# print(articles)

df=pd.DataFrame.from_dict(data)
df.to_csv("data1.csv",index=False)