import speech_recognition as sr

r = sr.Recognizer()
print(sr.Microphone.list_microphone_names())
while True:
    with sr.Microphone(device_index=0) as source:
        r.adjust_for_ambient_noise(source)
        print("adjusted! start talking")
        audio = r.listen(source)
        print(r.recognize_google(audio))

