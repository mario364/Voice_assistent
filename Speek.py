import pyttsx3



engine = pyttsx3.init()


ru_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0'


engine.setProperty('rate', 150)
engine.setProperty('voice', ru_voice_id)

str1 = input('Введите имя: ')
engine.say(f'Здравствуйте,{str1}!')

engine.runAndWait()






