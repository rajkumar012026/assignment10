import requests
#dummy web site for practice
url = "https://books.toscrape.com/"
try:
    response = requests.get(url = url)
    response.raise_for_status()
    print(f"Status: {response.status_code}")
    #First 500 characters of the HTML content
    print("\n----------First 500 characters of the retrieved HTML content---------\n")
    print(response.text[0:500])
except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")