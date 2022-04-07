import spacy
import urllib.request

nlpDutch = spacy.load("nl_core_news_lg")
nlpEnglish = spacy.load("en_core_web_trf")
locations = []
locationInTextAndWebsite = []

def getLocation(jsonForm, text, language):
    if(language == "Dutch"):
        doc = nlpDutch(text)
        for ent in doc.ents:    
           if ent.label_ == "GPE":
                locations.append(ent.text)
        getHospitalLocations()
        return locations
        
def getHospitalLocations():
    #Data uit webpagina lezen
    target_url = 'https://nl.wikipedia.org/wiki/Lijst_van_Nederlandse_ziekenhuizen'
    webUrl = urllib.request.urlopen(target_url)
    web_data = webUrl.read()
    string_web_data = web_data.decode("utf-8")

    #Check of locatie in de url text voorkomt
    for location in locations:  
        if location in string_web_data:
            locationInTextAndWebsite.append(location)   
        






