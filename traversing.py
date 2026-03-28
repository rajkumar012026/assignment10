'''
Finding a book's rating and then traversing up to its parent article
'''
import requests
from bs4 import BeautifulSoup

#dummy web site for practice
url = "https://books.toscrape.com/"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
first_book_rating_tag = soup.find('p', class_='star-rating')
if first_book_rating_tag:
    parent_article = first_book_rating_tag.find_parent('article')
    if parent_article:
        title_from_parent = parent_article.h3.a.get('title')
        print(title_from_parent)