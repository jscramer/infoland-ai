import SpacyModule as spacyModule
import QuestionModel as questionModel
import json

sample_text_english ="Yesterday at our ophthalmology department in Veldhoven, patient Bernard became unwell after administration of hypromellose HPS to both eyes. Dr. Hazelaar has been involved in the treatment"
sample_text = "Bij ons bij oogheelkunde in Veldhoven is gisteren patient Bernard onwel geworden na toediening van hypromellose HPS aan beide ogen. Dokter Hazelaar is betrokken geweest bij de behandeling"

persons = []
questionModelAnswer = []

def load_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def getPerson(jsonForm, text, kindOfPerson):
    #Using the spacy module to get the persons
    #persons = getPersonsWithSpacy(jsonForm, text)

    #Using the question model to get the persons
    getPersonsWithQuestionModel(text, kindOfPerson)


    #Easy Fix :D
    for ent in persons:        
        if ent.start_char == sample_text.find("patient") + 8:
            print(ent.text)
      

def getPersonsWithSpacy(jsonForm, text):
    spacyModule.getEntities(jsonForm, text)
    return spacyModule.getPersons()

def getPersonsWithQuestionModel(text, kindOfPerson):
    question = "Wie is "
    match kindOfPerson:
        case "Patient":
            question += "de patient?"


    questionModelAnswer = questionModel.questionmodel({
    'context': text,
    'question': question})
    print(questionModelAnswer)
    




getPerson(load_json('./jsonTestFiles/data.json'), sample_text, "Patient")