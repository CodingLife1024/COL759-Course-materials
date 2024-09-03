from itertools import permutations

def fill_matrix_pattern(pattern):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Playfair cipher usually combines I/J
    used_letters = {ch for row in pattern for ch in row if ch != '_'}
    remaining_letters = ''.join([ch for ch in alphabet if ch not in used_letters])

    empty_positions = [(i, j) for i in range(5) for j in range(5) if pattern[i][j] == '_']

    for perm in permutations(remaining_letters):
        matrix = [row[:] for row in pattern]  # Copy the pattern matrix
        for pos, letter in zip(empty_positions, perm):
            matrix[pos[0]][pos[1]] = letter
        yield matrix

def print_matrix(matrix):
    ans = ""
    for row in matrix:
        ans += (''.join(row))
    print(ans)
    print()

# Given pattern
pattern = [
    ['_', '_', '_', 'D', '_'],
    ['_', '_', '_', 'S', '_'],
    ['_', '_', '_', 'E', '_'],
    ['_', '_', '_', 'P', '_'],
    ['V', 'W', 'X', 'Y', 'Z']
]

# Generate and print all matrices following the pattern
for idx, matrix in enumerate(fill_matrix_pattern(pattern)):
    print(f"Matrix {idx + 1}:")
    print_matrix(matrix)
