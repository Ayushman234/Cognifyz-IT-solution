from collections import Counter
import string

filename = input("Enter file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read().lower()

    text = text.translate(str.maketrans("", "", string.punctuation))

    words = text.split()

    word_count = Counter(words)

    print("\nWord Frequency:\n")

    for word in sorted(word_count):
        print(f"{word:<15} : {word_count[word]}")

except FileNotFoundError:
    print("Error: File not found.")

except Exception as e:
    print("Error:", e)