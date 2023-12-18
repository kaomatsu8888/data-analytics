from bs4 import BeautifulSoup
import requests

html = requests.get("http://www.pythonscraping.com/pages/warandpeace.html")
soup = BeautifulSoup(html.text, 'html.parser')

# h1~h6タグを取得して表示する
headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
for header in headers:
    print(header.text)

# classがgreenのspanタグを取得して表示する
intro = soup.find_all('span', {'class': 'green'})
for item in intro:
    print(item.text)
