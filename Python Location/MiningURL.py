import urllib.request
import spacy


#SpacY Language choice
nlp = spacy.load("nl_core_news_lg")

#SpacY text
sample_text = "Bij ons bij oogheelkunde in Veldhoven is gisteren een patient Bernard, wonende in Vught, onwel geworden na toedining van hypomellose HPS aan beide ogen. Dr. Hazelaar is betrokken geweest bij de behandeling"
doc = nlp(sample_text)

locations = []
locationInTextAndWebsite = []

#Elke entity met een "GPE" tag eruit halen
for ent in doc.ents:    
    if ent.label_ == "GPE":
        locations.append(ent.text)  

print("Found locations in text")
print(locations)

#Data uit webpagina lezen
target_url = 'https://nl.wikipedia.org/wiki/Lijst_van_Nederlandse_ziekenhuizen'
webUrl = urllib.request.urlopen(target_url)
web_data = webUrl.read()
string_web_data = web_data.decode("utf-8")

#Check of locatie in de url text voorkomt
for location in locations:  
    if location in string_web_data:
        locationInTextAndWebsite.append(location)

print("Found locations in text which are also on the website")
print(locationInTextAndWebsite)
