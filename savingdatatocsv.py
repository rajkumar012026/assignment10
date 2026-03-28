'''
Extracting book data to CSV file'
'''
import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd

#dummy web site for practice
url = "https://books.toscrape.com/"
response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

books_data = []
product_articles = soup.find_all('article',class_='product_pod')
for article in product_articles:
    title = article.h3.a.get('title')
    price = article.find('p',class_='price_color').get_text(strip=True)
    rating_tag = article.find('p',class_='star_rating')
    rating_class = rating_tag['class'][-1] if rating_tag else "N/A"

    books_data.append(
        {
            'title': title,
            'price': price,
            'Rating': rating_class
        })
    CSV_file = 'scraped_books.csv'
    err = False
    if books_data:
        CSV_headers = books_data[0].keys()
    else:
        CSV_headers = ['title', 'price', 'Rating']
    try:
        with open(CSV_file, 'w', newline='',encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=CSV_headers)
            writer.writeheader()
            writer.writerows(books_data)

    except IOError as e:
        err = True
        print(f"Error while writing to CSV file: {e}")

if err:
   pass
else:
    print("\nData successfully saved to CSV file")
    df = pd.read_csv('scraped_books.csv')
    print(df)
