"""
CP1404 Practical 05 - Word Occurrences
"""

text = input("Text: ")
words = text.split()

word_to_count = {}

for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

if word_to_count:
    longest_word_length = max(len(word) for word in word_to_count)

    for word in sorted(word_to_count):
        print(f"{word:{longest_word_length}} : {word_to_count[word]}")