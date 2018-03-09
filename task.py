import threading
import time
import pygame
from gtts import gTTS
def respuesta(value):
    value = value+'.mp3'
    print (value)
    time.sleep(0.2)
    pygame.mixer.pre_init(24050, -16, 2, 2048)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(value)
    pygame.mixer.music.play()
    time.sleep(4)

def tareas(entidad,valor):
    if(entidad=='set_temperatura'):
        text = "temperatura ajustada a "+str(valor)+" grados"
        print(text)
        tts = gTTS(text=text, lang='es')
        tts.save('temperatura.mp3')
        t = threading.Thread(target=respuesta("temperatura"))
        t.start()
    elif(entidad=='set_luces'):
        tts = gTTS(text="luces encendidas", lang='es')
        tts.save('luces.mp3')
        t = threading.Thread(target=respuesta('luces'))
        t.setDaemon(True)
        t.start()
        print(valor)
