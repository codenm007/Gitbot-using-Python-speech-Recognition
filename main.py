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
with open('comprehensions.json') as comprehensions:
    comprehensions_data = json.load(comprehensions)

#function to execute
def exec_command(voice_data):
    if there_exists(comprehensions_data["what is your name"],voice_data):
        engine.say(read_out_data["name"])
        engine.runAndWait()
    if there_exists(comprehensions_data["time"],voice_data):
        engine.say("The time is:")
        engine.say(datetime.now().strftime("%I:%M %p"))
        engine.runAndWait()
    if there_exists(comprehensions_data["backup my code"],voice_data):
        os.system("git add .")
        engine.say(read_out_data["git add"])
        engine.runAndWait()
    if there_exists(comprehensions_data["commit my code"],voice_data):
        os.system('git commit -m "committed by viki the gitbot"')
        engine.say(read_out_data["commit"])
        engine.runAndWait()
    if there_exists(comprehensions_data["push to remote repo"],voice_data):
        os.system("git push origin master")
        engine.say(read_out_data["remote_repo"])
        engine.runAndWait()
    if there_exists(comprehensions_data["about"],voice_data):
        engine.say(read_out_data["about"])
        engine.runAndWait()
    if there_exists(comprehensions_data["what is your name"],voice_data):
        os.system("git pull origin master")
        engine.say(read_out_data["pull"])
        engine.runAndWait()


#function to match if anything is matching
def there_exists(terms,voice_data):
    for term in terms:
        if term in voice_data:
            return True


recognition = sr.Recognizer()
def recognize(selection,number):
    engine.setProperty('voice', voices[number].id)  # changing index, changes voices. 1 for female and 0 for male
    if selection == 'google':
        with sr.Microphone() as source:
            print("Say something!")
            audio = recognition.listen(source,timeout=3)
            try:
                voice_data = recognition.recognize_google(audio)
                print(voice_data.lower())
                exec_command(voice_data.lower())
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