import QuestionModel as questionModel
import personFilter as personFilter

from transformers import logging

logging.set_verbosity_error()

sample_text_english ="Yesterday at our ophthalmology department in Veldhoven, patient Bernard became unwell after administration of hypromellose HPS to both eyes. Dr. Hazelaar has been involved in the treatment"
sample_text = "Bij ons bij oogheelkunde in Veldhoven is gisteren de heer Bernard onwel geworden na toediening van hypromellose HPS aan beide ogen. Dokter Hazelaar is betrokken geweest bij de behandeling"
sample_text2 = "Bij de afdeling kraamzorg is er vandaag een baby geboren. Dokter Nielson heeft bij de bevalling geholpen"
sample_text3 = "Er is vandaag in Eindhoven een melding binnengekomen over Sarah. Sarah is vannacht gevallen en heeft haar been gebroken"


def getIncidentFromText(text):
    #Get the person which the incident is about
    person = personFilter.getPerson("",text, "patient")          

    #Find out what happened with the person
    whatQuestion2 = "Wat is er gebeurd met "+person+"?"
    whatQuestionAnswer2 = questionModel.questionmodel({
    'context': text,
    'question': whatQuestion2})   

    #Find out why it happened
    whatQuestion3 = "Waarom is  "+person+ whatQuestionAnswer2['answer'] + "overkomen?"
    whatQuestionAnswer3 = questionModel.questionmodel({
    'context': text,
    'question': whatQuestion3})
  
    #Combine answers to one description
    answer = person + " " + whatQuestionAnswer3['answer'] +" "+ whatQuestionAnswer2['answer']
    print(answer)
    return answer


getIncidentFromText(sample_text)
#getIncidentFromText(sample_text2)
#getIncidentFromText(sample_text3)