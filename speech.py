import speech_recognition as sr

def sp_rg():
    mic = sr.Microphone()
    recog = sr.Recognizer()
    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        return recog.recognize_google(audio, language='pl_PL')
    

