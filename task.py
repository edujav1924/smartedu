import threading
import time
import pygame
import sqlite3
from gtts import gTTS
from playsound import playsound
import time;

def respuesta(value):
    value = value+'.mp3'
    print (value)
    playsound(value)

def tareas(entidad,valor):
    if(entidad=='set_temperatura'):
        text = "temperatura ajustada a "+str(valor)+" grados"
        print(text)
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        localtime = time.asctime( time.localtime(time.time()) )
        print "Local current time :", localtime
        sql = ''' INSERT INTO temperatura(status,hora)VALUES(?,?) '''
        task = (valor,localtime)
        c.execute(sql,task)
        conn.commit()
        conn.close()
        tts = gTTS(text=text, lang='es-us')
        tts.save('temperatura.mp3')


        ta = threading.Thread(target=respuesta("temperatura"))
        ta.start()

    elif(entidad=='set_luces' and valor=='on'):
        tb = threading.Thread(target=respuesta('luces'))
        tb.start()

    elif(entidad=='get_temperatura'):
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        c.execute('''SELECT status FROM temperatura''')
        user1 = c.fetchall()
        conn.close()
        text = "temperatura actual "+str(user1[len(user1)-1][0])+" grados"
        print(text)
        tts = gTTS(text=text, lang='es-us')
        tts.save('temperatura_actual.mp3')
        ta = threading.Thread(target=respuesta("temperatura_actual"))
        ta.start()
    else:
        tc = threading.Thread(target=respuesta('no_comando'))
        tc.start()
