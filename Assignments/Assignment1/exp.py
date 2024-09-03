import nltk
from nltk.corpus import words

# Download the word list (if not already downloaded)
nltk.download('words')

def is_english(text):
    english_words = set(words.words())
    words_in_text = text.split()
    english_word_count = sum(1 for word in words_in_text if word.lower() in english_words)
    ans = english_word_count / len(words_in_text)
    print(ans)
    return english_word_count / len(words_in_text) > 0.5  # Adjust threshold as needed

text = "Forgiveness is simply freeing ourselves from wanting to punish."
print(is_english(text))  # True

text = "Fzrgtveyesd is dimaly qrepinr oucsewved frzm wlnttng eo pfnidh."
print(is_english(text))  # False
