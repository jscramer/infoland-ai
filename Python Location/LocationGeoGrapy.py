import geograpy3

sample_text = "Bij ons bij oogheelkunde in Veldhoven is gisteren een patient Bernard onwel geworden na toedining van hypomellose HPS aan beide ogen. Dr. Hazelaar is betrokken geweest bij de behandeling"

more_places = geograpy3.get_place_context(text = sample_text) 


link = 'https://nos.nl/artikel/2422474-navo-leiders-bijeen-in-brussel-navo-chef-stoltenberg-blijft-langer-aan'
places = geograpy3.get_place_context(url = link)

print("Places in text")
#print(more_places.country_mentions)
#print(more_places.region_mentions)
#print(more_places.city_mentions)

print("Places from URL")
#print (places.city_mentions)
print(places.region_mentions)
#print(places.country_mentions)
