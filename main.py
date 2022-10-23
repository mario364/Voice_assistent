import os
import pyttsx3
from func import *



engine = pyttsx3.init()

ru_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0'
engine.setProperty('rate', 150)
engine.setProperty('voice', ru_voice_id)


#say_hello()
do_list()





