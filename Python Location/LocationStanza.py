import stanza
import time

stanza.download('en')

start = time.time()
sample_text_english ="Yesterday at our ophthalmology department in Veldhoven, patient Bernard became unwell after administration of hypromellose HPS to both eyes. Dr. Hazelaar has been involved in the treatment"

sample_text = "Bij ons bij oogheelkunde in Veldhoven is gisteren patient Bernard onwel geworden na toediening van hypromellose HPS aan beide ogen. Dr. Hazelaar is betrokken geweest bij de behandeling"


nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,ner', use_gpu=True,)

doc = nlp(sample_text)
docEng = nlp(sample_text_english)

print("NL")
print(*[f'entity: {ent.text}\ttype: {ent.type}' for ent in doc.ents], sep='\n')
print("ENG")
print(*[f'entity: {ent.text}\ttype: {ent.type}' for ent in docEng.ents], sep='\n')
end = time.time()
print(end - start)