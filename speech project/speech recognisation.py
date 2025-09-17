import speech_recognition as sr

def main():
    sentence = input("Enter the sentence for comparison: ")
    print(f"\nOriginal sentence:\n\"{sentence}\"\n")
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile("speech.wav") as source:  
            audio = recognizer.record(source)
        spoken_text = recognizer.recognize_google(audio)
        print("Spoken sentence:", spoken_text)
        correct, incorrect = compare_sentences(sentence, spoken_text)
        print(f"\nCorrect words ({len(correct)}): {correct}")
        print(f" Incorrect words ({len(incorrect)}): {incorrect}")

    except sr.UnknownValueError:
        print(" Could not understand the audio.")
    except sr.RequestError:
        print(" Could not request results from Google Speech Recognition service.")
    except FileNotFoundError:
        print(" File 'speech.wav' not found. Please place your WAV file in the same folder.")

def compare_sentences(original, spoken):
    original_words = original.lower().strip().split()
    spoken_words = spoken.lower().strip().split()
    correct = []
    incorrect = []
    for i, word in enumerate(spoken_words):
        if i < len(original_words) and word == original_words[i]:
            correct.append(word)
        else:
            incorrect.append(word)
    return correct, incorrect
if __name__ == "__main__":
    main()
