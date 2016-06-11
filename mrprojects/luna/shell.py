# Luna Shell
# Author: Mauricio Ribeiro
# Python: 3.4
# Lang: PT-BR

# Luna imports
from core.luna import *
from core.luna_cost_command import LunaCostCommand

# Django Luna models imports
import os, sys, django
sys.path.append(os.pardir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mrprojects.settings")
django.setup()

from luna.models import *

# Speech Recognition imports
import speech_recognition as SpeechRecognition

def runLunaShell():
	exit_msg = "até mais Luna"
	print("*** Diga \"%s\" para sair ***" %exit_msg)

	r = SpeechRecognition.Recognizer()
	luna = Luna([LunaCostCommand])

	while True:
	    with SpeechRecognition.Microphone() as source:
	        audio = r.listen(source)
	        if 1: #try:
	            text = r.recognize_google(audio, language = "pt-BR")
	            print("Detectado >> " + text)
	            print(luna.process(text))
	            if text in exit_msg: break
	        #except:
	        #    print("Luna >> Desculpa, não entendi o que disse. Pode repetir?")

runLunaShell()