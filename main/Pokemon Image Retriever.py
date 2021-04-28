import wikipedia

def pokemon_image(pokemon):
    wikipage = wikipedia.page(pokemon)
    return wikipage.images[1]

print(pokemon_image("Bulbasaur"))