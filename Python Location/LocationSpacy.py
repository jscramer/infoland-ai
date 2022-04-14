import spacy
import time

nlpDutch = spacy.load("nl_core_news_lg")
nlpEnglish = spacy.load("en_core_web_trf")

entities = []
labels = []
position_start =[]
position_end = []


entitiesEng = []
labelsEng = []
position_startEng =[]
position_endEng = []


start = time.time()

sample_text_english ="Yesterday at our ophthalmology department in Veldhoven, patient Bernard became unwell after administration of hypromellose HPS to both eyes. Dr. Hazelaar has been involved in the treatment"
sample_text = "Bij ons bij oogheelkunde in Veldhoven is gisteren patient Bernard onwel geworden na toediening van hypromellose HPS aan beide ogen. Dr. Hazelaar is betrokken geweest bij de behandeling"
extra_text = """
Gisteren is er in de Koffiekamer van het ziekenhuis in Eindhoven een vrouw gestruikeld.
Zij wilde naar de kantine gaan. 
Vanuit de afdeling Oncologie is er hulp gekomen. 
Vanuit de afdeling Kaakchirurgie kwam niks.
Op de campus Batavia is dit nieuws later vanuit Kaakchirurgie aangekomen.
"""
doc = nlpDutch(sample_text)
docEng = nlpEnglish(sample_text_english)
docExtra = nlpDutch(extra_text)

#Dutch Entities
for ent in doc.ents:    
    entities.append(ent)
    labels.append(ent.label_)
    position_start.append(ent.start_char)
    position_end.append(ent.end_char)


#Entities
for ent in docExtra.ents:    
    entitiesEng.append(ent)
    labelsEng.append(ent.label_)
    position_startEng.append(ent.start_char)
    position_endEng.append(ent.end_char)

end = time.time()
print(end - start)

for entity in docExtra.ents:
    print(entity.text, entity.label_)