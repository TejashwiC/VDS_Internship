from collections import Counter
import string

def word_frequency(filename):
    with open(filename, 'r') as f:
        text = f.read().lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()
        freq = Counter(words)
    return freq

freqs = word_frequency("merged.txt")
for word, count in freqs.items():
    print(f"{word}: {count}")
