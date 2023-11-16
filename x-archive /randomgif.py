import requests
import random
from IPython.display import Image, display
print('          ~~~~~~~~~~MBS Python for Business~~~~~~~~~~~~~~~~')
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

GIPHY_API_KEY = 'CcUdCmsZQT1jTKPP56JLP9hLW09KY4iw'  # Replace with your GIPHY API key
qimage=input('select your gify...')

def get_random_office_gif_url(api_key):
    base_url = "https://api.giphy.com/v1/gifs/search"
    
    # Search for The Office gifs
    params = {
        "api_key": api_key,
            "q":qimage,
        "limit": 100  # You can adjust this limit
    }
    
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    
    gifs = response.json()["data"]
    
    if not gifs:
        print("No GIFs found.")
        return
    
    # Randomly select a gif
    random_gif = random.choice(gifs)
    
    return random_gif["images"]["original"]["url"]

def display_gif_in_notebook(url):
    img = Image(url=url)
    display(img)

# Fetch and display gif
gif_url = get_random_office_gif_url(GIPHY_API_KEY)
if gif_url:
    display_gif_in_notebook(gif_url)
    print('you selected....',qimage)
