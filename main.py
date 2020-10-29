import speech_recognition as sr
import json
import pyttsx3
from datetime import datetime
import os
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


print(comprehension("name"))

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
    if voice_data == "backup":
        os.system("git add .")
        engine.say(read_out_data["git add"])
        engine.runAndWait()
    if meaning == ['commit my code']:
        engine.say(read_out_data["sing gariwala"])
        engine.runAndWait()
    if meaning == ['upload to cloud']:
        engine.say(read_out_data["sing gariwala"])
        engine.runAndWait()
    if meaning == ['tell me about yourself']:
        engine.say(read_out_data["sing gariwala"])
        engine.runAndWait()
    if meaning == ['update yourself']:
        engine.say(read_out_data["sing gariwala"])
        engine.runAndWait()


recognition = sr.Recognizer()
def recognize(selection,number):
    engine.setProperty('voice', voices[number].id)  # changing index, changes voices. 1 for female and 0 for male
    if selection == 'google':
        with sr.Microphone() as source:
            print("Say something!")
            audio = recognition.listen(source,timeout=3)
            try:
                voice_data = recognition.recognize_google(audio)
                print(voice_data)
                exec_command(voice_data)
            except sr.UnknownValueError:
                engine.say('Sorry, I did not get that')
            except sr.RequestError:
                engine.say('Sorry, googles service is down')


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