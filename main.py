import pyaudio
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os

kayit = sr.Recognizer()


def dinleme(a=False):

    with sr.Microphone() as kaynak:
        if a:
            print(a)
        mikrofon = kayit.listen(kaynak)
        ses = ""

        try:
            ses = kayit.recognize_google(mikrofon, language="tr_TR")
        except UnknownValueError:
            print("Asistan: Anlayamadım.")

        except RequestError:
            print("Asistan: Sistem Şu Anda Çalışmıyor")

        return ses

def konusma(metin):
    tts = gTTS(text=metin, lang="tr", slow=False)
    ses = "konusma.mp3"
    tts.save(ses)
    playsound("konusma.mp3")
    os.remove(ses)


print("Sistem Açıldı")
ses = dinleme()
#playsound("konusma.mp3")
#konusma(ses)
print(ses)