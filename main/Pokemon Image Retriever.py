#wiki image finder
import wikipedia
def pokemon_image(pokemon):
    wikipage = wikipedia.page(pokemon)
    return wikipage.images[1]
url = pokemon_image("Charmeleon")
print(url)
from PIL import Image
import requests
im = Image.open(requests.get(url, stream=True).raw)
print(im)


#google image finder - not all images needed are on wikipedia


"""
import selenium
from selenium import webdriver
# This is the path I use
# DRIVER_PATH = '.../Desktop/Scraping/chromedriver 2'
# Put the path for your ChromeDriver here
DRIVER_PATH = ''
wd = webdriver.Chrome(executable_path=DRIVER_PATH)
wd.get('https://google.com')
search_box = wd.find_element_by_css_selector('input.gLFyf')
search_box.send_keys('Dogs')
"""

"""
from gsearch.googlesearch import search
import requests
import numpy as np
import cv2


def url_to_image(url):
    response = requests.get(url)
    data = response.json()

    image_url = data['data'][0]['card_images'][0]['image_url']
    print('image_url:', image_url)

    response = requests.get(image_url)

    data = np.asarray(bytearray(response.content), dtype="uint8")
    image = cv2.imdecode(data, cv2.IMREAD_COLOR)

    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return image

print(url_to_image('https://bulbapedia.bulbagarden.net/wiki/Charmeleon', num_results=1))"""