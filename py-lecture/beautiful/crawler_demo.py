import requests
from bs4 import BeautifulSoup
DEP_ID = 'E9'

headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
#response = requests.get('http://www.kghs.kh.edu.tw/home', headers=headers)
response = requests.get('https://hackmd.io/@yencheng/H1RpBndzP', headers=headers)
if response.status_code == 200:
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify())
    print(soup.title)
    view = soup.find_all('dl', class_='main_nav')[1].select("dd")
    for v in view:
        print(v.find('span').get_text())
