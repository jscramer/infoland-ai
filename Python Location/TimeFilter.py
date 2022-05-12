from datetime import datetime, timedelta
import SpacyModule as spacyModule
import QuestionModel as questionModel
import json

sample_text_english ="Yesterday at our ophthalmology department in Veldhoven, patient Bernard became unwell after administration of hypromellose HPS to both eyes. Dr. Hazelaar has been involved in the treatment"
sample_text = "Bij ons bij oogheelkunde in Veldhoven is 21 September 2013 de patient Bernard onwel geworden na toediening van hypromellose HPS aan beide ogen. Dokter Hazelaar is betrokken geweest bij de behandeling"
english = True

#questionModelAnswer = []

def load_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def getTime(jsonForm, text):
    #Using the spacy module to get the persons
    #persons = getPersonsWithSpacy(jsonForm, text)

    #Using the question model to get the persons
 #   getTimeWithQuestionModel(text)
   # print(getTimeWithSpacy(jsonForm,text))
    result = getTimeFromStaticListDutch(text)
    if result == None:
        result = getTimeWithSpacy(jsonForm, text)
        
    print(result)
 #Easy Fix :D
 #  for ent in persons:
 #      if ent.start_char == sample_text.find("patient") + 8:
 #           print(ent.text)
def getTimeFromStaticListEnglish(text):
    if "yesterday" in text:
        today = datetime.now() - timedelta(days=1)
        return today
        
    if "today" in text:
        return datetime.now()
    
    if "tomorrow" in text:
        today = datetime.now() + timedelta(days=1)
        return today
      
def getTimeFromStaticListDutch(text):
    if "eergisteren" in text:
        today = datetime.now() - timedelta(days=2)
        return today
    
    if "gisteren" in text:
        today = datetime.now() - timedelta(days=1)
        return today
        
    if "vandaag" in text:
        return datetime.now()
    
    if "morgen" in text:
        today = datetime.now() + timedelta(days=1)
        return today
        
    if "overmorgen" in text:
        today = datetime.now() + timedelta(days=2)
        return today
    
def getTimeWithSpacy(jsonForm, text):
    spacyModule.getEntities(jsonForm, text)
    return spacyModule.getTime()

#def getTimeWithQuestionModel(text):
#    question = "welke tijd is het ? "
#    
#    questionModelAnswer = questionModel.questionmodel({
#    'context': text,
#    'question': question})
#    print(questionModelAnswer)
    



if english:
    getTime(load_json('./jsonTestFiles/data.json'), sample_text.lower())
else:
    getTime(load_json('./jsonTestFiles/data.json'), sample_text_english.lower())