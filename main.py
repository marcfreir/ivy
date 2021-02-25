import speech_recognition as speechrec

rec = speechrec.Recognizer()

with speechrec.Microphone() as source:
    print('Say something.:')
    audio = rec.listen(source)
    try:
        voice_data = rec.recognize_google(audio)
        print(voice_data)
    except speechrec.UnknownValueError:
        print('Sorry! I did not understand...')
    except speechrec.RequestError:
        print('Sorry! My speech service is off...')