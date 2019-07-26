
import time

import speech_recognition as sr
from time import ctime
#import time
import os
import audio_find as find
from win32com.client import constants
import win32com.client
import training as tr
import webbrowser as wb
#from random import randrange
value=0   


def speak(audioString):
    print("B: "+audioString)
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(audioString)
	
	
    

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        r.energy_threshold=280  # minimum audio energy to consider for recording
        #r.dynamic_energy_threshold = True
        #r.dynamic_energy_adjustment_damping = 0.15
        #r.dynamic_energy_ratio = 0.1
        #r.pause_threshold = 0.8  # seconds of non-speaking audio before a phrase is considered complete
        #r.operation_timeout = None  # seconds after an internal operation (e.g., an API request) starts before it times out, or ``None`` for no timeout

        r.phrase_threshold = 0.1  # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
        #r.non_speaking_duration = 0 # seconds of non-speaking audio to keep on both sides of the recording

        r.adjust_for_ambient_noise(source,duration=1)
        print("Please Say something!")
        speak("Please Say something!")
        audio = r.listen(source,phrase_time_limit=4)
    data = ""
    try:
        print("Audio Recorded")
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio,language='en-IN')
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        check=1
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
    return data
	
def search_data(data):
	if data:     
		if "hi" in data or "hello" in data:
			speak("hi how can i help you")
		elif ('time now') in data or ('time please') in data or ('tell me the time') in data:
			speak("now time is: " +ctime())
		elif "your name" in data :
			speak("I am a robot") 
		elif "dead" in data:
			speak("no, i am just a machine")
		elif "start training" in data or "train yourself" in data :
			tr.training_start()	
		elif "open browser" in data:
			wb.open_new_tab('http://www.google.com')
		elif "close browser" in data:
			os.system("taskkill /F /IM chrome.exe")
		elif "open calculator" in data:
			os.system('calc.exe')
		elif "close calculator" in data:
			os.system("taskkill /F /IM calculator.exe")            
		elif "open facebook" in data:            
			wb.open_new_tab('https://www.facebook.com/')
		else:
			find.find_text(data)

	   
			
       
# initialization
#time.sleep(2)
speak("Hello I am a chatbot") 
while 1:
    data = recordAudio()
    search_data(data)
    	
