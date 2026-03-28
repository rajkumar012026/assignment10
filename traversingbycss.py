'''
Finding books using css: article tag with class 'product_pod'
'''
import requests
from bs4 import BeautifulSoup

#dummy web site for practice
url = "https://books.toscrape.com/"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
titles_css = soup.select('article.product_pod h3 a')
print(f"\nTitles found with css selector: {[t.get('title') for t in titles_css[:3]]}....")
price_css = soup.select('article.product_pod p.price_color')
print(f"Prices found with css selector: {[p.get_text(strip=True) for p in price_css[:3]]}....")
first_book_rating_css = soup.select_one('article.product_pod p.star-rating')
if first_book_rating_css:
    rating_class_css = first_book_rating_css['class'][-1]
    print(f"First book rating with css selector: {rating_class_css}")