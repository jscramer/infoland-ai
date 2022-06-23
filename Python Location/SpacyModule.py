import json
from sqlite3 import Date
import spacy
import urllib.request

with open('./jsonTestFiles/locationListExample.json') as location_data_file:    
    location_data = json.load(location_data_file)

nlpDutch = spacy.load("nl_core_news_lg")

organisations = []
persons= []
locations = []
time = []
date = []


locationInTextAndWebsite = []

def getPersons():
    return persons

def getTime():
    return time + date

def getEntities(jsonform, text):   
    doc = nlpDutch(text)
    
    for ent in doc.ents:                 
        match ent.label_:
            case "GPE":
                 locations.append(ent.text)
            case "PERSON":
                 persons.append(ent)                    
            case "ORG":    
                 organisations.append(ent.text)
            case "TIME":
                 time.append(ent.text)
            case "DATE":
                 date.append(ent.text)
               
        

def getLocation(jsonForm, text, language):
    if(language == "Dutch"):
        doc = nlpDutch(text)
        for ent in doc.ents:    
           if ent.label_ == "GPE":
                locations.append(ent.text)
        getHospitalLocations()
        getLocationFromList()
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

def getLocationFromList():
    locationsFromList = []
    locationsInListAndNer = []

    #Locaties uitlezen vanuit JSON
    for location in location_data['locations']:     
        locationsFromList.append(location['location']['name'])
    
    #Locaties vergelijken met lijst en NER
    for location in locations:
        if location in locationsFromList:
            locationsInListAndNer.append(location)
    
    return locationsInListAndNer
        
   

    
        






