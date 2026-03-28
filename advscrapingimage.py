'''
The program is written to download image
'''
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import time

#dummy web site for practice
base_url = "https://books.toscrape.com/"

download_directory = "downloaded_book_cover"
#Create directory if it doesn't exist
if not os.path.exists(download_directory):
    os.makedirs(download_directory)
    print(f"{download_directory} directory created")
try:
    response = requests.get(base_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    for img_tag in img_tags:
        img_src = img_tag.get('src')
        if img_src:
            abs_img_url = urljoin(base_url, img_src)
            filename = os.path.basename(abs_img_url)
            filepath = os.path.join(download_directory, filename)
            try:
                img_response = requests.get(abs_img_url,stream=True)
                img_response.raise_for_status()
                with open(filepath, 'wb') as f:
                    for chunk in img_response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"{filename} downloaded")
            except requests.exceptions.RequestException as e:
                print(f"Error in downloading {abs_img_url}: {e}")
            except IOError as e:
                print(f"Error saving '{filename}': {e}")
            time.sleep(.5)
except requests.exceptions.RequestException as e:
    print(f"Error in downloading {base_url}: {e}")
print("\n-----Image download Process Complete-----")

