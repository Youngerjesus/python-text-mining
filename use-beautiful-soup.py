import requests
from bs4 import BeautifulSoup

url = "https://ko.wikipedia.org/wiki/%EB%94%94%EC%9E%90%EC%9D%B8_%ED%8C%A8%ED%84%B4"

r = requests.get(url)

soup = BeautifulSoup(r.text)
print(type(soup))

soup = BeautifulSoup(soup.prettify())

for a in soup.find_all("a"):
    if 'href' in a.attrs:
        if 'http' not in a.attrs['href']:
            print(a.attrs['href'])
