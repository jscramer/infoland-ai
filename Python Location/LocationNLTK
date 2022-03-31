from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

sample_text = "Bij ons bij oogheelkunde in Veldhoven is gisteren patient Bernard onwel geworden na toediening van hypromellose HPS aan beide ogen. Dr. Hazelaar is betrokken geweest bij de behandeling"
sample_text_english ="Yesterday at our ophthalmology department in Veldhoven, patient Bernard became unwell after administration of hypromellose HPS to both eyes. Dr. Hazelaar has been involved in the treatment"


def get_continuous_chunks(text, label):
    chunked = ne_chunk(pos_tag(word_tokenize(text))) 
    continuous_chunk = []
    current_chunk = []

    for subtree in chunked:
        if type(subtree) == Tree and subtree.label() == label:
            current_chunk.append(" ".join([token for token, pos in subtree.leaves()]))
        if current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue

    return continuous_chunk

#Print every entitie with the label GPE
print("Nederlandse tekst")
print(get_continuous_chunks(sample_text,'GPE'))
print("Engelse tekst")
print(get_continuous_chunks(sample_text_english,'GPE'))

