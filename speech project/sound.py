import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr

def record_audio(filename="study.wav", duration=5, samplerate=16000):
    print("\n Recording... Please say: 'I am studying in First/Second/Third Class'")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    write(filename, samplerate, audio)
    print(" Recording saved:", filename)

def recognize_audio(filename="study.wav"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language="en-IN")
        return text.lower()
    except:
        return ""

def check_class(spoken_text):
    if "first class" in spoken_text:
        return True, ("First Class", 95, "A+")
    elif "second class" in spoken_text:
        return True, ("Second Class", 80, "A")
    elif "third class" in spoken_text:
        return True, ("Third Class", 65, "B")
    else:
        return False, None

def main():
    record_audio()
    spoken = recognize_audio()
    print("\n You said:", spoken)

    match, details = check_class(spoken)

    print("\nRESULT ")
    if match:
        classname, marks, grade = details
        print("SAME ", classname)
        print("Marks:", marks)
        print("Grade:", grade)
    else:
        print("NOT SAME ")

if __name__ == "__main__":
    main()
