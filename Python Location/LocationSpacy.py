import spacy
import pandas as pd

nlp = spacy.load("nl_core_news_lg")

sample_text = "Bij ons bij oogheelkunde in Veldhoven is gisteren een patient Bernard onwel geworden na toedining van hypomellose HPS aan beide ogen. Dr. Hazelaar is betrokken geweest bij de behandeling"
doc = nlp(sample_text)

entities = []
labels = []
position_start =[]
position_end = []

for ent in doc.ents:
    entities.append(ent)
    labels.append(ent.label_)
    position_start.append(ent.start_char)
    position_end.append(ent.end_char)



df = pd.DataFrame({'Entities':entities,'Labels':labels,'Start':position_start,'End':position_end})

print(df)