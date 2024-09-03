from construct_matrix import *
import nltk
from nltk.corpus import words

# Download the 'words' corpus if not already downloaded
nltk.download('words')

# Get the list of English words
word_list = words.words()

def check(keyword, imcomplete_matrix):
    matrix = create_playfair_matrix(keyword)
    # print(matrix)
    # print(imcomplete_matrix)
    for i in range(5):
        for j in range(5):
            if imcomplete_matrix[i][j] != '_':
                if imcomplete_matrix[i][j] != matrix[i][j]:
                    # print(imcomplete_matrix[i][j], matrix[i][j])
                    return False
    return True

def find_keyword(imcomplete_matrix):
    ans = []
    for word in word_list:
        print(word)
        if check(word, imcomplete_matrix):
            ans.append(word)
    return ans

imcomplete_matrix = [['_', '_', '_', 'D', '_'],
                     ['_', '_', '_', 'S', '_'],
                     ['_', '_', '_', 'E', '_'],
                     ['_', '_', '_', 'P', '_'],
                     ['V', 'W', 'X', 'Y', 'Z']]

run = [['R', 'U', 'N', 'A', 'B'], ['C', 'D', 'E', 'F', 'G'], ['H', 'I', 'K', 'L', 'M'], ['O', 'P', 'Q', 'S', 'T'], ['V', 'W', 'X', 'Y', 'Z']]

# print(check("run", imcomplete_matrix))

if __name__ == "__main__":
    print(find_keyword(imcomplete_matrix))