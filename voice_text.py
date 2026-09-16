import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:

    print("🎤 Speak something...")

    recognizer.adjust_for_ambient_noise(source)

    audio = recognizer.listen(source)

try:

    text = recognizer.recognize_google(audio)

    print("You said:")
    print(text)

except sr.UnknownValueError:

    print("Sorry, I could not understand.")

except sr.RequestError:

    print("Speech recognition service is unavailable.")