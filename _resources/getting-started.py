# NOTE: this requires PyAudio because it uses the Microphone class
import speech_recognition as sr

exit_msg = "até mais Luna"
print("*** Diga \"%s\" para sair ***" %exit_msg)
r = sr.Recognizer()

while True:
    with sr.Microphone() as source:                # use the default microphone as the audio source
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
        try:
            text = r.recognize_google(audio, language = "pt-BR")
            print("Detectado >> " + text)    # recognize speech using Google Speech Recognition
            if text in exit_msg: break
        except:                            # speech is unintelligible
            print("Luna >> Desculpa, não entendi o que disse. Pode repetir?")
            
