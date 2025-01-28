#1. Write a Python program to calculate the frequency of each word in a given text. Print the words and their corresponding counts
# Input: Text from the user
text = input("Enter a text: ")

# Split the text into words
words = text.split()
print(words)

# Create an empty dictionary for word frequencies
wordfreq = {}

# Count frequency of each word
for word in words:
    if word not in wordfreq:
        wordfreq[word] = 0  # Initialize word frequency to 0
    wordfreq[word] += 1  # Increment word frequency

# Print word frequencies
for word, count in wordfreq.items():
    print(f"{word}: {count}")
