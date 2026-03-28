import requests
post_test_url = "https://httpbin.org/post"
payload = {
    'username': 'my_test_user',
    'password': 'secure_password123',
    'remember_me': 'on'
}
try:
    response = requests.post(post_test_url, data=payload)
    response.raise_for_status()
    print(response.json())
    print(f"Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error during post request: {e}")