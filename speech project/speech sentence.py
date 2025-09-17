import speech_recognition as sr
import difflib

def main():
    # Read the sentence from file
    with open("sentences.txt", "r") as file:
        sentence = file.readline().strip()

    print(f"\nExpected sentence:\n\"{sentence}\"\n")

    recognizer = sr.Recognizer()

    with sr.AudioFile("speech.wav") as source:
        print("Listening from WAV file...")
        audio = recognizer.record(source)

    try:
        # Convert speech to text
        spoken_text = recognizer.recognize_google(audio)
        print("\nYou said:", spoken_text)

        # Compare spoken vs expected
        similarity = compare_sentences(sentence, spoken_text)

        if similarity > 0.85:  
            print("✅ Good job! You read it correctly.")
        else:
            print("❌ Not a proper match, try again.")

    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
    except sr.RequestError:
        print("⚠️ Could not request results from Google Speech Recognition service.")

def compare_sentences(original, spoken):
    original = original.lower().strip()
    spoken = spoken.lower().strip()
    return difflib.SequenceMatcher(None, original, spoken).ratio()

if __name__ == "__main__":
    main()
