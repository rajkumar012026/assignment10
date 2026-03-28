import requests
from bs4 import BeautifulSoup

#dummy web site for practice
url = "https://books.toscrape.com/"
response = requests.get(url = url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
books_data = []
product_article = soup.find_all('article',class_='product_pod')
for article in product_article:
    title = article.h3.a.get('title')
    price = article.find('p',class_='price_color').get_text(strip = True)
    rating = article.find('p',class_='star-rating')
    if rating:
        rating_class = rating['class'][-1]
    else:
        rating_class = "N/A"
    book_info = {
        "title" : title,
        "price" : price,
        "rating" : rating_class,
    }
    books_data.append(book_info)
print("\n--------Extracted Books Data (First 3)------")
print("Title\t\t\t\tPrice\t\t\t\tRating")

for book in books_data[0:3]:
    print(f"{book['title']}\t\t\t\t{book['price']}\t\t\t\t{book['rating']}")
print(f"\nTotal numbers of books extracted are: {len(books_data)}")