import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://books.toscrape.com/"

url1="https://www.buddy4study.com/scholarships?filter=eyJFRFVDQVRJT04iOlsiMjIiXSwiR0VOREVSIjpbIjExMSJdLCJSRUxJR0lPTiI6W10sIkZPUkVJR04iOlsiODIwIl19"

r=requests.get(url1)

soup=BeautifulSoup(r.text,'html.parser')

# print(soup.prettify())
# print(soup.find_all("article"))
# print(soup.find_all("span"))
# <article class="scholarshipslistFeaturedcard_scholarshipName__crtbm"><h4><a href="/page/reliance-foundation-scholarships?ref=featuredBlocks"><a><span>Reliance Foundation Undergraduate Scholarships 2023-24</span></a></a></h4></article>

print(soup.find_all("article.scholarshipslistFeaturedcard_scholarshipName__crtbm"))