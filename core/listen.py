import speech_recognition as sr

recognizer = sr.Recognizer()


def listen():
    try:
        with sr.Microphone() as source:
            print("🎤 Listening... Speak now!")

            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)

        print("Recognizing...")

        text = recognizer.recognize_google(audio)

        print("You said:", text)

        return text.lower()

    except Exception as e:
        print(e)
        return ""
