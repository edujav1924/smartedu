#!/usr/bin/python3
# -*- coding: utf-8 -*-
import subprocess, string, time
import configparser
import os
import io

def escuchar():
    #Grabar audio del microfono en wav
    #y enviarlo a Google quien devolvera el texto en una variable
    envio = subprocess.Popen(["./grabar.sh"], shell=True, universal_newlines=True, stdout=subprocess.PIPE)
    texto = envio.communicate()[0]
    texto = texto.strip('\n')
    return texto

while True:
    clave = escuchar()
    print("Escuche:" + clave)

    if clave == 'encender luz' or clave == 'enciende la luz' :
        os.system("sudo python encender.py")

    if clave == 'apagar luz' or clave == 'apaga la luz' :
        os.system("sudo python apagar.py 2>/dev/null")

    if clave == 'hacer foto' :
        os.system("sudo ./foto.sh 2>/dev/null")
