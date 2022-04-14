import spacy

text = "Op mijn afdeling is patient is onwel geworden na toediening Hypromellose HPS aan bd ogen. Dr. Hazelaar is betrokken geweest bij de afhandeling."

nlp = spacy.load("nl_core_news_lg")   #("en_core_web_lg")
doc = nlp(text)
for ent in doc.ents:
    print(ent.text,ent.label_)