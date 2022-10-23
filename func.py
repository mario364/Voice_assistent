import os
import webbrowser
import pyttsx3
from playsound import playsound


events = ['Создать папку', "Удалить папку", "Открыть запрос в интернет",
          "Воспроизвести музыку с компьютера", 'Открыть программу с устройства']

dict_start_program = {'Telegram': 'C:\Programs\Telegram Desktop\Telegram.exe', 'image': '"C:\Programs\FastStone Image Viewer\FSViewer.exe"'}


engine = pyttsx3.init()

ru_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0'
engine.setProperty('rate', 150)
engine.setProperty('voice', ru_voice_id)


def say_hello():
    engine.say('Здравствуйте, пользователь! Меня зовут Поля, я ваш ассистент.')
    engine.say('Что вы хотите сделать?')
    engine.runAndWait()


def do_list():
    while True:
        for num, event in enumerate(events, 1):
            print(num, event)
        action = int(input('Что вы хотите сделать? '))

        if action == 1:
            folder_create()
            continue

        if action == 2:
            folder_del()
            continue

        if action == 3:
            browser_open()
            continue

        if action == 4:
            music_play()
            continue


        if action == 5:
            programm_open()
            continue



def folder_create():
    engine.say('Где вы хотите создать папку?')
    engine.runAndWait()
    create_directory = input('Путь к папке: ')
    if not os.path.isdir(create_directory):
        engine.say('Папка создана.')
        engine.runAndWait()
        os.mkdir(create_directory)

    else:
        engine.say('Папка уже существует.')
        engine.runAndWait()


def folder_del():
    engine.say('Какую папку вы хотите удалить?')
    engine.runAndWait()
    del_directory = input('Путь к папке: ')
    if os.path.isdir(del_directory):
        engine.say('Папка удалена')
        engine.runAndWait()
        os.rmdir(del_directory)

    else:
        engine.say('Такой папки нет')
        engine.runAndWait()


def browser_open():
    engine.say('Введите адрес запроса: ')
    engine.runAndWait()
    ask = input('Введите запрос: ')
    webbrowser.open(ask, new=2)

def programm_open():
    engine.say('Какую программу вы хотите запустить?')
    engine.runAndWait()
    key_word = input('Введите ключевое слово: ')
    if key_word == 'Telegram':
        os.startfile(dict_start_program['Telegram'])
    if key_word == 'image':
        os.startfile(dict_start_program['image'])


def music_play():
    engine.say('Какой файл вы хотите прослушать?')
    engine.runAndWait()
    music1 = input('Укажите путь: ')
    playsound(music1)



