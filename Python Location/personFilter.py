import SpacyModule as spacyModule
import QuestionModel as questionModel
import json
from transformers import logging


sample_text_english ="Yesterday at our ophthalmology department in Veldhoven, patient Bernard became unwell after administration of hypromellose HPS to both eyes. Dr. Hazelaar has been involved in the treatment"
sample_text = "Bij ons bij oogheelkunde in Veldhoven is gisteren de heer Bernard onwel geworden na toediening van hypromellose HPS aan beide ogen. Dokter Hazelaar is betrokken geweest bij de behandeling"

persons = []
questionModelAnswer = []



def load_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    print(type(data))
    return data

def getPerson(jsonForm, text, kindOfPerson):
    person = []
    if kindOfPerson == "Dokter":
        #Using TestData / API to get Doctors
        person = getDoctorFromZenya(text)
    else:
        #Using the question model to get the persons
        person = getPersonsWithQuestionModel(text)


    print(person)
    #Using the spacy module to get the persons
    #persons = getPersonsWithSpacy(jsonForm, text)
    
      

def getDoctorFromZenya(text):   
    #Getting doctors now from Fake JSON List -> TODO: Extend to make an API Call
    doctors = load_json('./jsonTestFiles/doctorListExample.json')

    #Check if doctor from list is in the text -> TODO: Check if doctor is not the patient here.
    for doctor in doctors['doctors']:
        if text.find(doctor['name']):            
            return doctor['name']
            

def getPersonsWithSpacy(jsonForm, text):
    #Get the list of persons from spaCy
    spacyModule.getEntities(jsonForm, text)
    return spacyModule.getPersons()


def getPersonsWithQuestionModel(text):  
    #Get an answer on the question what has happened. This helps with determing to whom it happened -> The patient 
    whatQuestion = "Wat is er gebeurd?"
    whatQuestionAnswer = questionModel.questionmodel({
    'context': text,
    'question': whatQuestion})
    
    toWhomQuestion = "Bij wie is" + whatQuestionAnswer['answer']
    whoQuestion = "Wie is de Patiënt?"
    
    toWhomAnswer = questionModel.questionmodel({
    'context': text,
    'question': toWhomQuestion})

    whoAnswer = questionModel.questionmodel({
    'context': text,
    'question': whoQuestion})


    print(whoAnswer['answer'])
    print(toWhomAnswer['answer'])
 

#Function that starts when running the python file
getPerson(load_json('./jsonTestFiles/data.json'), sample_text, "Dokter")

