"""
Speech for DELTA
"""

#Import libraries
import speech_recognition as sr
import pyttsx3
import re
from time import sleep

#Defs/classes
class Speech:
    
    def __init__(self, voice='Australian female'):
        self.set_voice = self.get_voice(voice=voice)
        self.voice(self.set_voice)
    
    def voice(self, voice):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        #print(self.voices[15])
        #self.engine.setProperty('voice', self.voices[voice].id)
    
    def get_voice(self, voice='Australian female'):
        voices = {'Australian female':15,
                  'Portuguese female':13,
                  'French female':11,
                  'Spanish female':9}
        return voices[voice]
    
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self, lang='english'):
        langs = {'english': 'en-GB', 'french': 'fr-FR', 'spanish': 'es-ES', 'portuguese': 'pt-PT'}
        statement = None
        while statement == None:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print('Listening...')
                audio = r.listen(source)
                try:
                    statement = r.recognize_google(audio, language=langs[lang]).lower()
                    print('User said: {0}'.format(statement))
                except Exception:
                    self.speak('Sorry, could you say that again?')
                    sleep(1)
                    statement = None
        return statement
    
    def start(self):
        statement = 'None'
        while re.search('delta', statement) is None:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print('Listening...')
                audio = r.listen(source)
                try:
                    statement = r.recognize_google(audio, language='en-in').lower()
                    print(statement)
                except Exception:
                    print('Exception...')
        else:
            self.speak('Hello, what can I help you with?')
    
    def run(self):
        self.start()
        self.listen()
