import wikipedia

def pokemon_image(pokemon):
    wikipage = wikipedia.page(pokemon)
    return wikipage.images[1]

print(pokemon_image("Charmeleon"))

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