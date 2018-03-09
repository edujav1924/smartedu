from gtts import gTTS
import os
tts = gTTS(text='temperatura a 30 grados', lang='es')
tts.save('apagado.mp3')
