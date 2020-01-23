# LFX253 page 58
# https://buildmedia.readthedocs.org/media/pdf/gtts/latest/gtts.pdf

from gtts import gTTS  # Uses API to contact Google Translate Text-to-Speech service
from io import BytesIO
#import tempfile
import time

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"  # Hide pygame messages on import
from pygame import mixer

while True:
    myLang = input('lang: ')
    # Fun languages:
    #    en-us  U.S. accent
    #    en-ca  Canadian accent
    #    en-uk  British accent
    #    en-au  Australian accent
    #    fr     French
    #    it     Italian (male)
    #    ru     Russian
    #    ja     Japanese
    # Source: https://cloud.google.com/speech-to-text/docs/languages
    myText = input('text: ')

    tts = gTTS(myText, myLang)
    mixer.init()

    mp3_fp = BytesIO()  # Instead of writing to an mp3 file to disk, write to memory
    #mp3_fp = tempfile.TemporaryFile()  # Not sure tempfile is faster than BytesIO
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    mixer.music.load(mp3_fp)
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(0.25)  # Don't want script to finish and exit before sound finishes playing
    mixer.music.stop()
    mixer.quit()

