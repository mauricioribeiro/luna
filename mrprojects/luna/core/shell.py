# Luna imports
from luna import Luna
from luna_cost_command import LunaCostCommand

# NOTE: this requires PyAudio because it uses the Microphone class
import speech_recognition as SpeechRecognition

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