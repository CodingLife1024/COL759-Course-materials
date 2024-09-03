import nltk
from nltk.corpus import words

# Download the 'words' corpus if not already downloaded
nltk.download('words')

# Get the list of English words
word_list = words.words()

# Print each word
for word in word_list:
    print(word)
