'''
The program is written to trace price
'''
import time

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

PRODUCT_URL = "https://www.amazon.in/Samsung-Galaxy-Smartphone-128GB-Storage/dp/B0DHL98QM2/"
TARGET_PRICE_THRESHOLD = 50000.00
HEADERS = {
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0",
    "Accept-Language":"en-US,en;q=0.9",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "DNT":"1",
    "Connection":"keep-alive",
    "Upgrade-Insecure-Requests":"1"
}
def get_product_details(url,headers):
    product_name = None
    concurrent_price = None
    try:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Checking:{url}")
        response = requests.get(url,headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        title_tag = soup.find('span',id='productTitle')
        if title_tag:
            product_name = title_tag.get_text(strip=True)
        else:
            print(f"Warning: product title tag (id='productTitle') not found.")
        price_span = soup.find('span', class_='a-offscreen')
        if price_span:
            price_text = price_span.get_text(strip=True)
            cleaned_price_text = re.sub(r'[₹,]', '', price_text)
            try:
                current_price = float(cleaned_price_text)
            except ValueError:
                print(f" Error: Could not convert cleaned price '{cleaned_price_text}' to number.")
            else:
                price_tag_alt = soup.find('span', class_='a-price-whole')
                if price_tag_alt:
                    whole_part = re.sub(r'[₹,]', '',
                            price_tag_alt.get_text(strip=True))
                    fraction_tag = soup.find('span', class_='a-price-fraction')
                    fraction_part = fraction_tag.get_text(strip=True) if fraction_tag else "00"
                    try:
                        current_price = float(f"{whole_part}.{fraction_part}")
                    except ValueError:
                        print(f" Error: Could not combine price parts '{whole_part}.{fraction_part}' to number.")
                    else:
                        print(" Warning: Price tag (class='a-offscreen' or 'a-price-whole') not found.")
                return product_name, current_price
    except requests.exceptions.RequestException as e:
        print(f"Network error or bad HTTP response: {e}")
        return None, None
    except Exception as e:
        print(f"An unexpected error occurred during product detail retrieval: {e}")
        return None, None
def notify_price_drop(product_name, current_price,target_price):
    print(f"\n{'=' * 30}")
    print(f"PRICE ALERT!")
    print(f"{'=' * 30}")
    print(f"Product: {product_name if product_name else 'N/A'}")
    print(f"Current Price: ₹{current_price:,.2f}")
    print(f"Target Price: ₹{target_price:,.2f}")
    print(f"Action: Grab it now! {PRODUCT_URL}")
    print(f"{'=' * 30}\n")
def price_tracker_loop():
    print("----------Starting Amazon Price Tracker----------")
    while True:
        product_name, current_price = get_product_details(PRODUCT_URL,HEADERS)
        if current_price is not None:
            print(f"Current Price of '{product_name if product_name else 'Unknown Product'}':  ₹ {current_price:,.2f}")
            if current_price <= TARGET_PRICE_THRESHOLD:
                notify_price_drop(product_name,current_price,TARGET_PRICE_THRESHOLD)
            else:
                print(f"Price ₹{current_price:,.2f}) is still above target (₹{TARGET_PRICE_THRESHOLD:,.2f}).")
        else:
            print(f"Could not retrieve valid price. Retrying...")
            sleep_duration_seconds = 7200
            print(f"Waiting for {sleep_duration_seconds/7160:.if} hours before next check....")
            time.sleep(sleep_duration_seconds)

if __name__ == "__main__":
    price_tracker_loop()