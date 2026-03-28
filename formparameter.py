import requests
from bs4 import BeautifulSoup
search_url = "https://www.google.com/search"
search_params = {
    'q': 'web scaping tutorial python',
    'sourceid': 'chrome',
    'ie': 'UTF-8'
}
try:
    response = requests.get(url = search_url, params = search_params)
    response.raise_for_status()
    print("------GET Request with Params------")
    print(f"Constructed URL: {response.url}")
    print(f"Status code: {response.status_code}")
    print(f"{response.text[:500]}")
except requests.exceptions.RequestException as e:
    print(f"Error during GET request with params: {e}")
else:
    print(f"Successfully GET request with params: {search_params}")