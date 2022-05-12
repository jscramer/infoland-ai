from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline


tokenizer = AutoTokenizer.from_pretrained("henryk/bert-base-multilingual-cased-finetuned-dutch-squad2")
model = AutoModelForTokenClassification.from_pretrained("henryk/bert-base-multilingual-cased-finetuned-dutch-squad2")


questionmodel = pipeline("question-answering",
    model="henryk/bert-base-multilingual-cased-finetuned-dutch-squad2",
    tokenizer="henryk/bert-base-multilingual-cased-finetuned-dutch-squad2"
)

sample_text = "Bij ons bij oogheelkunde in Veldhoven is gisteren patient Bernard onwel geworden na toediening van hypromellose HPS aan beide ogen. Dr. Hazelaar is betrokken geweest bij de behandeling"
question = "Wie is de patient"

