import re
from collections import Counter
import pprint
from itertools import combinations

def modify_text(text: str) -> str:
    ciphertext = text.lower().replace(" ", "")
    removed_punctuation = ""
    for i in range(len(ciphertext) - 2):
        if ciphertext[i].isalpha():
            removed_punctuation += ciphertext[i]
    return removed_punctuation

def count_letters(text: str) -> Counter:
    frequency = Counter(text)
    return frequency

def find_trigrams(ciphertext: str) -> dict:
    trigrams = {}
    ciphertext = ciphertext.lower().replace(" ", "")
    removed_punctuation = ""
    for i in range(len(ciphertext) - 2):
        if ciphertext[i].isalpha():
            removed_punctuation += ciphertext[i]
    for i in range(len(removed_punctuation) - 2):
        trigram = removed_punctuation[i:i + 3]
        if trigram in trigrams.keys():
            trigrams[trigram].append(i)
        else:
            trigrams[trigram] = [i]
    return trigrams

def kasiski(trigrams: dict, ciphertext: str) -> list:
    distances = []
    for trigram, indices in trigrams.items():
        if len(indices) > 1:
            distances.extend([indices[i + 1] - indices[i] for i in range(len(indices) - 1)])
    if len(distances) == 0:
        return [len(ciphertext)]
    return distances

def get_possible_lengths(distances: list) -> list:
    common_factors = Counter()
    distances = list(set(distances))
    print(distances)
    if len(distances) == 1:
        distance = distances[0]
        outer_bound = min(distance + 1, 6)
        factors = [i for i in range(2, outer_bound)]
        return factors
    for distance in distances:
        for i in range(2, min(6, distance + 1)):
            if distance % i == 0:
                common_factors[i] += 1
    return [length for length, count in common_factors.items() if count >= 3]

def calculate_ic(text: str) -> float:
    text_length = len(text)
    frequency = count_letters(text)
    ic = 0.0
    for letter in frequency:
        ic += frequency[letter] * (frequency[letter] - 1)
    ic /= (text_length * (text_length - 1)) if text_length > 1 else 1
    return ic

def get_ic_values(ciphertext: str, possible_lengths: list) -> dict:
    ic_values = {}
    for m in possible_lengths:
        segments = ['' for _ in range(m)]
        for i, char in enumerate(ciphertext):
            segments[i % m] += char
        total_ic = sum(calculate_ic(segment) for segment in segments) / m
        ic_values[m] = total_ic
    return ic_values


def calculate_mic(segment1: str, segment2: str) -> float:
    freq1 = count_letters(segment1)
    freq2 = count_letters(segment2)
    mic = 0.0
    for char in freq1:
        if char in freq2:
            mic += freq1[char] * freq2[char]
    mic /= (len(segment1) * len(segment2))
    return mic

def get_mic_values(ciphertext: str, possible_lengths: list) -> dict:
    mic_values = {}
    for m in possible_lengths:
        segments = ['' for _ in range(m)]
        for i, char in enumerate(ciphertext):
            segments[i % m] += char
        mic_sum = 0
        comb_count = 0
        for segment1, segment2 in combinations(segments, 2):
            mic_sum += calculate_mic(segment1, segment2)
            comb_count += 1
        mic_values[m] = mic_sum / comb_count if comb_count > 0 else 0
    return mic_values

def format_text(old: str, new: str) -> str:
    ans = ""
    for i in range(len(old)):
        if old[i].isalpha():
            if old[i].isupper():
                ans += new[0].upper()
            else:
                ans += new[0].lower()
            new = new[1:]
        else:
            ans += old[i]
    return ans

