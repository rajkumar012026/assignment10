import requests
from bs4 import BeautifulSoup

#dummy web site for practice
url = "https://books.toscrape.com/"
response = requests.get(url = url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
page_title = soup.title.string #Title of the web page
print(f"\nPage Title: {page_title}")
#Finding first h1 tag of the content
first_h1 = soup.find('h1')
if first_h1:
    print(f"\nFirst H1 Tag: {first_h1.get_text(strip = True)}")
#Finding all the links
all_link = soup.find_all('a')
print(f"Total numbers of linlks are: {len(all_link)}")
print("First 5 links are as follows:")

print(f"Link Text \t\t\t\tLink href")
print("---------------------------------------------")
for l in all_link[0:5]:
    link_text = l.get_text(strip = True)
    link_href = l.get('href')
    print(f"{link_text}\t\t\t{link_href}")
print("---------------------------------------------")
#Finding elements by tag
first_product_article = soup.find('article',class_ = 'product_pod')
print("First product in the content")
if first_product_article:
    product_title = first_product_article.h3.a.get('title')
    product_price = first_product_article.find('p',class_ = 'price_color').get_text(strip = True)
    print(f"\nProduct Title: {product_title}")
    print(f'Price is {product_price}')

