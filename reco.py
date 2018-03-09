#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import codecs
import sys
import requests
import json
import pyaudio
import wave
import time

# Wit speech API endpoint
API_ENDPOINT = 'https://api.wit.ai/speech'

# Wit.ai api access token
wit_access_token = 'WQEO7P77DQENGBQET2OQUV6L6TB4P5V4'

audio = read_audio("file.wav")

# defining headers for HTTP request
headers = {'authorization': 'Bearer ' + wit_access_token,
           'Content-Type': 'audio/wav'}

# making an HTTP post request
resp = requests.post(API_ENDPOINT, headers = headers,
                     data = audio)

# converting response content to JSON forma t
data = json.loads(resp.content.decode('utf-8'))

# get text from data
try:
    print (data+time.strftime("%Y-%m-%d %H:%M:%S",
                             time.localtime(time.time())))
    text = data['_text']
    # return the text
    return text
except:
    print("error")

if __name__ == "__main__":
    text =  ReconocimientoVoz('voz.wav')
    print("{}".format(text))
