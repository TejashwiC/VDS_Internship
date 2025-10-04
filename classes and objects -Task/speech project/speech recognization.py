import speech_recognition as sr

def main():
    sentence = input("Enter the sentence: ")
    print(f"\nGiven sentence:\n\"{sentence}\"\n")
    recognizer = sr.Recognizer()
    
    with sr.AudioFile("speech.wav") as source:  
        audio = recognizer.record(source)

    try:
        spoken_text = recognizer.recognize_google(audio)
        print("You said:", spoken_text)
        compare_words(sentence, spoken_text)
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")

def compare_words(original, spoken):
    original_words = original.lower().split()
    spoken_words = spoken.lower().split()
    matched = [w for w in spoken_words if w in original_words]
    missed = [w for w in original_words if w not in spoken_words]

    print("\nWord Comparison")
    print(" Matched words:", matched)
    print(" Missed words:", missed)

if __name__ == "__main__":
    main()
