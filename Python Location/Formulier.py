import json
from SpacyModule import getLocation

sample_text_english ="Yesterday at our ophthalmology department in Veldhoven, patient Bernard became unwell after administration of hypromellose HPS to both eyes. Dr. Hazelaar has been involved in the treatment"
sample_text = "Bij ons bij oogheelkunde in Veldhoven is gisteren patient Bernard onwel geworden na toediening van hypromellose HPS aan beide ogen. Dr. Hazelaar is betrokken geweest bij de behandeling"

language = "Dutch"

def load_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def get_values2(data):
    d = dict(data)
    items = d.items()
    for (key, value) in items:
        if(key == 'fields'):
            for v in value:
                values = v['values']
                for x in values:
                    if(x.keys() == "locatie"):
                        print("Found locatie")


def get_values(data):
    d = dict(data)
    items = d.items()
    for (key, value) in items:
        if key != 'fields': continue
        for v in value:
            values = v['values']
            if not values: continue
            for i in range(len(values)):
                for (key, value) in values[i].items():
                    match key:
                        case "locatie":
                            print("Locatie gevonden in formulier")
                         
                            values[i][key] = getLocation(value,sample_text,language)[0] #TODO: [0] fix voor test weghalen en zorgen dat er maar 1 locatie uitkomt
                            #print("Locatie ingevuld:",value)
                        #case "dokter": 
                        #    print(f"De dokter is: {value}")
                        #case "patient":
                            #print(f"De patient is: {value}")
    print(d)
                



get_values(load_json('data.json'))
