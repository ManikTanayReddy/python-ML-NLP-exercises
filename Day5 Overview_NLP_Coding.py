#1. Write a Python program to calculate the frequency of each word in a given text. Print the words and their corresponding counts

text = input("Enter a text: ")
words = text.split()
print(words)
wordfreq = {}
# Count frequency of each word
for word in words:
    if word not in wordfreq:
        wordfreq[word] = 0  
    wordfreq[word] += 1  
for word, count in wordfreq.items():
    print(f"{word}: {count}")
