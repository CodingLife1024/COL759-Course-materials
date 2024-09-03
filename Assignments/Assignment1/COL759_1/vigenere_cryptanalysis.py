###########################################
#   Vigenere Cryptanalysis Assignment     #
#   Authors:                              #
#       Riddhidipta Pal, 2021CS10546      #
#       Vaibhav Bajaj,   2021CS50126      #
###########################################

import re
from math import gcd
import string
import nltk
from nltk.corpus import words
from collections import Counter
from collections import defaultdict
import requests
import sys

# Needs to run once, can comment for subsequent runs
nltk.download('words', quiet=True)  # Backup to compare score of plaintext with english words as a reference

# Global Constants
MAX_KEY_LENGTH = 5
IC_ENGLISH = 0.0686
IC_RANDOM = 0.038466
MIC = 0.065

# Letter Frequency in English scraped from Pride and Prejudice, Project Gutenberg
LETTER_FREQ = {
    'a': 0.0774023579457662,
    'b': 0.016851595126658875,
    'c': 0.025614907990394193,
    'd': 0.04095588476485283,
    'e': 0.12853376793103985,
    'f': 0.022436566977364895,
    'g': 0.019002715660192012,
    'h': 0.0624308352597314,
    'i': 0.071125091284509,
    'j': 0.0017523172885522752,
    'k': 0.00603729414587912,
    'l': 0.04052773236331494,
    'm': 0.02706337518753248,
    'n': 0.07024289016682406,
    'o': 0.07489386827062684,
    'p': 0.015803657595475397,
    'q': 0.0011394378428024646,
    'r': 0.06071304639065799,
    's': 0.061624596664899965,
    't': 0.08776433663137287,
    'u': 0.02814756755916876,
    'v': 0.010562243518584058,
    'w': 0.0224728218178177,
    'x': 0.0017816664451093082,
    'y': 0.023443070405173738,
    'z': 0.0016763547656987775
}


class VignereSolver:
    def __init__(self):
        self.english_words = set(words.words())
        self.letters = string.ascii_lowercase
    

    def get_letter_frequencies(self, url = 'https://www.gutenberg.org/cache/epub/1342/pg1342.txt'):
        '''
        Scrapes the text from the given url and returns the letter frequencies
        '''
        response = requests.get(url)
        text = response.text
        text = text.lower()
        text = re.sub(r'[^a-z]', '', text)
        letter_freq = Counter(text)
        tot = sum(letter_freq.values())
        letter_freq = {k: v/tot for k, v in sorted(letter_freq.items(), key=lambda item: item[0])}
        
        return letter_freq


    def preprocess(self, c : str):
        '''
        Removes all non-alphabetic characters and converts to lowercase
        '''
        return re.sub(r'[^a-zA-Z]', '', c.lower())


    def get_repeating_sequences(self, c : str):
        '''
        Returns all repeating sequences of length > 2 with their locations
        '''
        c = self.preprocess(c)
        n_grams = defaultdict(list)
        for size in range(MAX_KEY_LENGTH, 2, -1):
            for start in range(len(c) - size + 1):
                n_grams[c[start:start+size]].append(start)
        
        n_grams = {k: v for k, v in n_grams.items() if len(v) > 1}

        return n_grams


    def get_distances(self, c : str):
        '''
        Returns the distances between repeating sequences
        '''
        c = self.preprocess(c)
        distances = []
        for n_gram in self.get_repeating_sequences(c).values():
            for i in range(len(n_gram) - 1):
                distances.append(n_gram[i+1] - n_gram[i])
        
        return distances


    def get_key_length_kasiski(self, c : str):
        '''
        Tries to find the key length using Kasiski method
        '''
        distances = self.get_distances(c)
        
        if len(distances) == 0:
            return None
        
        if len(distances) == 1:
            return distances[0]

        return gcd(*distances)


    def calculate_index_coeff(self, c : str):
        '''
        Calculates the index of coincidence for the given text
        '''
        c = self.preprocess(c)
        size = len(c)
        freq = Counter(c)
        ic = sum([count * (count - 1) for count in freq.values()]) / (size * (size - 1))
        
        return ic
    

    def get_key_length_index_coeff(self, c : str):
        '''
        Tries to find the key length using Index of Coincidence
        '''
        c = self.preprocess(c)
        key_length = None
        min_diff = float('inf')

        # Loops through all possible key lengths and calculates the closest index of coincidence
        # to the English language index of coincidence
        for length in range(1, MAX_KEY_LENGTH + 1):
            ic = 0
            for i in range(length):
                ic += self.calculate_index_coeff(c[i::length])
            
            ic /= length
            diff = abs(ic - IC_ENGLISH)

            if diff < min_diff:
                min_diff = diff
                key_length = length
        
        return key_length
    

    def shift_string(self, c : str, n : int):
        '''
        Shifts the string by n characters
        '''
        c = list(self.preprocess(c))
        c = [(ord(i) - ord('a') + n) % 26 for i in c]
        c = [chr(i + ord('a')) for i in c]
        return ''.join(c)


    def get_key(self, c : str, key_length : int):
        '''
        Returns the key for the given text using Mutual Index of Coincidence
        '''
        if key_length is None:
            return None
        
        c = self.preprocess(c)
        key = [0] * key_length

        # For each character in the key, calculates the best shift to get the closest MIC
        # to the English MIC.
        for i in range(key_length):
            ci = c[i::key_length]
            best_shift = -1
            min_diff = float('inf')
            for shift in range(26):
                shifted_c = self.shift_string(ci, shift)
                freq_c = Counter(shifted_c)
                mic = sum([LETTER_FREQ[letter] * freq_c[letter] for letter in self.letters]) / len(ci)
                diff = abs(mic - MIC)
                if diff < min_diff:
                    min_diff = diff
                    best_shift = shift
            
            key[i] = best_shift

        return ''.join([chr(ord('a') + (26 - i)) for i in key])


    def get_key_mic(self, c : str):
        '''
        Returns the key using both Kasiski and Index of Coincidence
        '''
        kasiski_key_len = self.get_key_length_kasiski(c)
        ic_key_len = self.get_key_length_index_coeff(c)

        kasiski_key = self.get_key(c, kasiski_key_len)
        ic_key = self.get_key(c, ic_key_len)
        
        return kasiski_key, ic_key


    def get_english_score(self, text : str):
        '''
        Returns the score of the text based on the frequency of english words
        '''
        score = 0
        for i in text.split():
            if i.lower() in self.english_words:
                score += 1
        
        return score/len(text.split())
    

    def get_plaintext(self, c : str, key : str):
        '''
        Returns the plaintext for the given text and key
        '''
        plaintext = ''
        key_len = len(key)
        non_alpha = 0

        for i in range(len(c)):
            if c[i].isalpha():
                shift = ord(key[(i - non_alpha) % key_len]) - ord('a')
                if c[i].isupper():
                    plaintext += chr((ord(c[i].lower()) - ord('a') - shift) % 26 + ord('a')).upper()
                else:
                    plaintext += chr((ord(c[i].lower()) - ord('a') - shift) % 26 + ord('a'))
            else:
                plaintext += c[i]
                non_alpha += 1

        return plaintext


    def decrypt(self, c : str):
        '''
        Decrypts the given text and returns the plaintext
        '''
        kasiski_key, ic_key = self.get_key_mic(c)
        
        if kasiski_key is None and ic_key is None:
            print("Failed to find key!")
            return None
        
        key = None
        matching_key = True

        if kasiski_key is None:
            key = ic_key
        elif ic_key is None:
            key = kasiski_key
        elif kasiski_key == ic_key:
            key = kasiski_key
        else:
            matching_key = False

        if matching_key:
            plaintext = self.get_plaintext(c, key)
        else:
            # If the keys are different, we choose the key with the higher score
            plaintext_kasiski = self.get_plaintext(c, kasiski_key)
            plaintext_ic = self.get_plaintext(c, ic_key)
            score_kasiski = self.get_english_score(plaintext_kasiski)
            score_ic = self.get_english_score(plaintext_ic)
            plaintext = plaintext_kasiski if score_kasiski > score_ic else plaintext_ic
        
        if  (kasiski_key is not None and len(kasiski_key) == 4) or \
            (ic_key is not None and len(ic_key) == 4):
            # If the key length is 4, we try to find the existence of a key of length 2
            extra_key = self.get_key(c, 2)

            maybe_plaintext = self.get_plaintext(c, extra_key)
            maybe_score = self.get_english_score(maybe_plaintext)

            if maybe_score > self.get_english_score(plaintext):
                plaintext = maybe_plaintext 
        
        output = f'Key:\t"{key.capitalize()}", plaintext:\t"{plaintext}"'
        print(output)
        return plaintext


def main():
    cipher_text = sys.argv[-1]
    solver = VignereSolver()
    solver.decrypt(cipher_text)


if __name__ == '__main__':
    main()