#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import codecs
import sys
import requests
import json
import pyaudio
import wave
import time
from task import tareas
# Wit speech API endpoint
API_ENDPOINT = 'https://api.wit.ai/speech'

# Wit.ai api access token
wit_access_token = 'CEXK54UG7325J5DEAIX5URZR5WH2FTNU'
def read_audio(WAVE_FILENAME):
    # function to read audio(wav) file
    with open(WAVE_FILENAME, 'rb') as f:
        audio = f.read()
    return audio
def ReconocimientoVoz():

    # record audio of specified length in specified audio file

    # reading audio
    audio = read_audio('file.wav')
    # defining headers for HTTP request
    headers = {'authorization': 'Bearer ' + wit_access_token,
               'Content-Type': 'audio/wav'}
    # making an HTTP post request
    resp = requests.post(API_ENDPOINT, headers = headers,
                         data = audio)

    # converting response content to JSON format
    data = json.loads(resp.content.decode('utf-8'))

    entidad = data['entities']['intent'][0]['value']
    print(data)
    try:
        if(entidad=='set_temperatura'):
            tareas(entidad,data['entities']['temperature'][0]['value'])
        elif(entidad=='set_luces'):
            tareas(entidad,data['entities']['on_off'][0]['value'])
    except:
        print('error')
