import difflib
import string
def main():
    original_sentence = input("Enter the original sentence: ")
    spoken_sentence = input("Enter the spoken sentence: ")
    compare_sentences(original_sentence, spoken_sentence)
def compare_sentences(original, spoken):
    original_words = original.strip().split()
    spoken_words = spoken.strip().split()
    correct = 0
    wrong = 0
    spelling_mistakes = 0
    punctuation_mistakes = 0
    missing = 0

    print("\n Comparison ")
    for i, word in enumerate(spoken_words):
        if i < len(original_words):
            orig = original_words[i]
            spoken = word
            if orig == spoken:
                print(f"Correct: {spoken}")
                correct += 1
            elif spoken.strip(string.punctuation) == orig.strip(string.punctuation):
                print(f"Punctuation mistake: Expected '{orig}', Got '{spoken}'")
                punctuation_mistakes += 1
            elif difflib.SequenceMatcher(None, orig.lower(), spoken.lower()).ratio() > 0.8:
                print(f"Spelling mistake: Expected '{orig}', Got '{spoken}'")
                spelling_mistakes += 1
            else:
                print(f"Wrong word: Expected '{orig}', Got '{spoken}'")
                wrong += 1
        else:
            print(f"Extra word: {word}")
            wrong += 1

    if len(spoken_words) < len(original_words):
        missing_words = original_words[len(spoken_words):]
        print("Missing words:", " ".join(missing_words))
        missing = len(missing_words)
    print("\nafter comparison")
    print("Correct words :", correct)
    print("Wrong words :", wrong)
    print("Spelling mistakes:", spelling_mistakes)
    print("Punctuation mistakes:", punctuation_mistakes)
    print("Missing words :", missing)

    if (wrong + spelling_mistakes + punctuation_mistakes + missing) == 0:
        print("Perfect reading!")
    else:
        print("Some mistakes detected.")

if __name__ == "__main__":
    main()
