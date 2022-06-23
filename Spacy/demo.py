from __future__ import annotations
import csv
from spacy.training import Example
from multiprocessing.context import SpawnContext
import random
import pandas as pd
import spacy
from spacy.tokens import Doc, DocBin, Span


def train_spacy(data,iterations,nlp):
    TRAIN_DATA = data
      # create blank Language class
    # create the built-in pipeline components and add them to the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        nlp.add_pipe("ner", last=True)
       
    ner = nlp.get_pipe('ner')
    # add labels
    for _, annotations in TRAIN_DATA:
         for ent in annotations.get('entities'):
            ner.add_label(ent[2])

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.create_optimizer()
        for itn in range(iterations):
            print("Starting iteration " + str(itn))
            random.shuffle(TRAIN_DATA)
            losses = {}
            for text, annotations in TRAIN_DATA:
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)
                nlp.update(examples=[example],
                  # batch of annotations
                    drop=0.2,  # dropout - make it harder to memorise data
                    sgd=optimizer,  # callable to update weights
                    losses=losses)
         #       print(losses)
    return nlp

  
                
  

with open('ner_dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    nlp = spacy.load("en_core_web_lg")
    #docbin = DocBin()
    #words = []
    #spaces = []
    #ents = []
    #docs = []
    #for row in csv_reader:
    #    if len(row[0]) > 0:
    #        doc = Doc(nlp.vocab,words=words,ents=ents,spaces=spaces)
    #        if len(spaces):
    #            spaces.pop()
    #            spaces.append(False)
           # docbin.add(doc)
    #        docs.append(doc)
    #        ents = []
    #        spaces = []
    #        words = []
    #    words.append(row[1])
     #   spaces.append(True)
    #    ents.append(row[3])
    data = TRAIN_DATA = [('what is the price of polo?', {'entities': [(21, 25, 'PrdName')]}), 
              ('what is the price of ball?', {'entities': [(21, 25, 'PrdName')]}), 
              ('what is the price of jegging?', {'entities': [(21, 28, 'PrdName')]}), 
              ('what is the price of t-shirt?', {'entities': [(21, 28, 'PrdName')]}), 
              ('what is the price of jeans?', {'entities': [(21, 26, 'PrdName')]}), 
              ('what is the price of bat?', {'entities': [(21, 24, 'PrdName')]}), 
              ('what is the price of shirt?', {'entities': [(21, 26, 'PrdName')]}), 
              ('what is the price of bag?', {'entities': [(21, 24, 'PrdName')]}), 
              ('what is the price of cup?', {'entities': [(21, 24, 'PrdName')]}), 
              ('what is the price of jug?', {'entities': [(21, 24, 'PrdName')]}), 
              ('what is the price of plate?', {'entities': [(21, 26, 'PrdName')]}), 
              ('what is the price of glass?', {'entities': [(21, 26, 'PrdName')]}), 
              ('what is the price of moniter?', {'entities': [(21, 28, 'PrdName')]}), 
              ('what is the price of desktop?', {'entities': [(21, 28, 'PrdName')]}), 
              ('what is the price of bottle?', {'entities': [(21, 27, 'PrdName')]}), 
              ('what is the price of mouse?', {'entities': [(21, 26, 'PrdName')]}), 
              ('what is the price of keyboad?', {'entities': [(21, 28, 'PrdName')]}), 
              ('what is the price of chair?', {'entities': [(21, 26, 'PrdName')]}), 
              ('what is the price of table?', {'entities': [(21, 26, 'PrdName')]}), 
              ('what is the price of watch?', {'entities': [(21, 26, 'PrdName')]})]
  
   
    doc = nlp("what is the price of beer?")
    for ent in doc.ents:
        print(ent.text,ent.label_)
    nlp = train_spacy(TRAIN_DATA, 2,nlp)
    doc = nlp("Where can we buy a watch in Amsterdam?")
    for ent in doc.ents:
        print(ent.text,ent.label_)
    doc = nlp("what is the price of beer?")
    for ent in doc.ents:
        print(ent.text,ent.label_)
   # docbin.to_disk("./train.spacy")