import requests
#dummy web site for practice
imgage_url = "https://images.pexels.com/photos/14433849/pexels-photo-14433849.jpeg/"
#https://images.pexels.com/photos/14433849/pexels-photo-14433849.jpeg
try:
    image_response = requests.get(imgage_url)
    image_response.raise_for_status()
    image_bytes = image_response.content
    print(f"\nSize of image content in bytes: {len(image_bytes)}")
    #First 50 bytes of the image content
    print(f"First 50 bytes of the image is : {image_bytes[:50]}")
    #saving image in the project directory
    with open("pexels-photo-14433849.jpeg", "wb") as f:
        f.write(image_bytes)
except requests.exceptions.RequestException as e:
    print(f"An error occurred during image downloading: {e}")