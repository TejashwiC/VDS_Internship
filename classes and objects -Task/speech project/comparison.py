import difflib
import string

def main():
    original_sentence = input("Enter the original sentence: ")
    spoken_sentence = input("Enter the spoken sentence: ")

    # Preprocess: lowercase + remove punctuation
    original_sentence = original_sentence.lower().translate(str.maketrans("", "", string.punctuation))
    spoken_sentence = spoken_sentence.lower().translate(str.maketrans("", "", string.punctuation))

    compare_sentences(original_sentence, spoken_sentence)

def compare_sentences(original, spoken):
    original_words = original.split()
    spoken_words = spoken.split()

    i, j = 0, 0
    correct = wrong = spelling_mistakes = 0
    missing_words, extra_words = [], []

    print("\n--- Comparison ---")
    while i < len(original_words) and j < len(spoken_words):
        o = original_words[i]
        s = spoken_words[j]

        if o == s:
            print(f"Correct: {s}")
            correct += 1
            i += 1
            j += 1
        elif difflib.SequenceMatcher(None, o, s).ratio() > 0.8:
            print(f"Spelling mistake: Expected '{o}', Got '{s}'")
            spelling_mistakes += 1
            i += 1
            j += 1
        else:
            # assume original word is missing
            print(f"Missing word: {o}")
            missing_words.append(o)
            i += 1

    # Remaining words in original → missing
    while i < len(original_words):
        print(f"Missing word: {original_words[i]}")
        missing_words.append(original_words[i])
        i += 1

    # Remaining words in spoken → extra
    while j < len(spoken_words):
        print(f"Extra word: {spoken_words[j]}")
        extra_words.append(spoken_words[j])
        j += 1

    # Summary
    print("\n--- Summary ---")
    print("Correct words     :", correct)
    print("Wrong words       :", wrong)
    print("Spelling mistakes :", spelling_mistakes)
    print("Missing words     :", missing_words if missing_words else "None")
    print("Extra words       :", extra_words if extra_words else "None")

    if wrong + spelling_mistakes + len(missing_words) + len(extra_words) == 0:
        print("✅ Perfect reading!")
    else:
        print("❌ Some mistakes detected.")

if __name__ == "__main__":
    main()
