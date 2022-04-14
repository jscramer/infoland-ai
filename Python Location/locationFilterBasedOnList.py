import json
with open('./jsonTestFiles/locationListExample.json') as location_data_file:    
    location_data = json.load(location_data_file)

#Get Locations from list -> Currently making list based on json file.
#Then check if location is in text.
def getLocationFromTextBasedOnList(text):    
    locationsFilteredFromText = []
    #Locaties uitlezen vanuit JSON
    for location in location_data['locations']:     
        if location['location']['name'] in text:
            locationsFilteredFromText.append(location['location']['name'])
    
    print(locationsFilteredFromText)

    