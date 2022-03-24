import locationtagger
import nltk
import spacy

# essential entity models downloads
nltk.downloader.download('maxent_ne_chunker')
nltk.downloader.download('words')
nltk.downloader.download('treebank')
nltk.downloader.download('maxent_treebank_pos_tagger')
nltk.downloader.download('punkt')
nltk.download('averaged_perceptron_tagger')
  

# initializing sample text
sample_text = "Bij ons bij oogheelkunde in Veldhoven is gisteren een patient onwel geworden na toedining van hypomellose HPS aan beide ogen. Dr. Hazelaar is betrokken geweest bij de behandeling"
  
# extracting entities.
place_entity = locationtagger.find_locations(text = sample_text)
  
# getting all country regions
print("The countries regions in text : ")
print(place_entity.country_regions)

# getting all country cities
print("The countries cities in text : ")
print(place_entity.country_cities)

# getting all other countries
print("All other countries in text : ")
print(place_entity.other_countries)

# getting all region cities
print("The region cities in text : ")
print(place_entity.region_cities)

# getting all other regions
print("All other regions in text : ")
print(place_entity.other_regions)

# getting all other entities
print("All other entities in text : ")
print(place_entity.other)

