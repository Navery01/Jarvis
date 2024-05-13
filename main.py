import sys
import os
import app
import chat_bot as chat
import pygame
import time
import record_audio as ra

def play_audio(audio_file):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy() == True:
        print("Playing audio", end='')
        time.sleep(.5)
        print('.', end='')
        time.sleep(.5)
        print('.', end='')
        time.sleep(.5)
        print('.', end= '')
        time.sleep(.5)
        os.system('cls' if os.name == 'nt' else 'clear')


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Speak now, ctrl + c to stop: ")
    recording = ra.record_audio()

    input_text = chat.transcribe(recording)
    
    output_file = app.return_tts(chat.get_response(input_text))

    if output_file:
        play_audio(output_file)


