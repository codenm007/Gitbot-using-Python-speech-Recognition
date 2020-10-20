import speech_recognition as sr
import json
import pyttsx3
from datetime import datetime
engine = pyttsx3.init()

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 159)     # setting up new voice rate
voices = engine.getProperty('voices')


#reading json files
with open('readout.json') as read_out:
    read_out_data = json.load(read_out)
#reading dictionaries
from reverse_search_dict import test_dict



def comprehension(read_dic):
    results = [k for k,v in test_dict.items() if read_dic in v]
    return results


#function to execute
def exec_command(voice_data):
    meaning = comprehension(voice_data)
    print(meaning)
    if meaning == ['what is your name']:
        engine.say(read_out_data["name"])
        engine.runAndWait()
    if meaning == ['time']:
        engine.say(datetime.now())
        engine.runAndWait()
    if meaning == ['what is your name']:
        engine.say(read_out_data["sing gariwala"])
        engine.runAndWait()




recognition = sr.Recognizer()
def recognize(selection,number):
    engine.setProperty('voice', voices[number].id)  # changing index, changes voices. 1 for female and 0 for male
    if selection == 'google':
        with sr.Microphone() as source:
            print("Say something!")
            audio = recognition.listen(source,timeout=3)
            voice_data = recognition.recognize_google(audio)
            print(voice_data)
            exec_command(voice_data)


    elif selection == 'offline':
        with sr.Microphone() as source:
            print("Say something!")
            audio = recognition.listen(source, timeout=3)
            voice_data = recognition.recognize_sphinx(audio)
            print(voice_data)
            exec_command(voice_data)
    else:
        print('Invalid selection!')

recognize('google',0)