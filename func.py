import os

import pyttsx3

events = ['Создать папку', "Удалить папку", "Создать текстовый файл", "Переминовать файл"]

engine = pyttsx3.init()

ru_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0'
engine.setProperty('rate', 150)
engine.setProperty('voice', ru_voice_id)


def say_hello():
    engine.say('Здравствуйте, пользователь! Меня зовут Полина, я ваш ассистент.')
    engine.say(f'Вот что я могу: {events}')
    engine.say('Что вы хотите сделать?')
    engine.runAndWait()


def get_action():
    while True:
        for num, event in enumerate(events, 1):
            print(num, event)
        action = int(input('Что вы хотите сделать? '))

        if action == 1:
            engine.say('Где вы хотите создать папку?')
            engine.runAndWait()
            direction = input('Путь к папке: ')
            if not os.path.isdir(direction):
                engine.say('Папка создана.')
                engine.runAndWait()
                os.mkdir(direction)
                continue
            else:
                engine.say('Папка уже существует.')
                engine.runAndWait()
                continue

        if action == 2:
            engine.say('Какую папку вы хотите удалить?')
            engine.runAndWait()
            del_direction = input('Путь к папке: ')
            if os.path.isdir(del_direction):
                engine.say('Папка удалена')
                engine.runAndWait()
                os.rmdir(del_direction)
                continue
            else:
                engine.say('Такой папки нет')
                engine.runAndWait()
                continue



