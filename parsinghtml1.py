import requests
from bs4 import BeautifulSoup

#dummy web site for practice
url = "https://books.toscrape.com/"
response = requests.get(url)
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
price_tags = soup.find_all('p',class_ = 'price_color')
print(f"Price found by (class): {[p.get_text(strip = True) for p in price_tags[:3]]}....")
main_content_div = soup.find('div',id = 'main-content')
if main_content_div:
    print(f"Content from main-content : {main_content_div.get_text(strip = True)[:100]}....")
print("Find element with attribute")
elements_with_data_attr = soup.find_all(attrs={'id':'promotions_left'})
print(f"Elemennts with data-category: {elements_with_data_attr}")
for l in elements_with_data_attr:
    print(l)

