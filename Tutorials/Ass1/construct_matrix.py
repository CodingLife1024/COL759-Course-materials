def create_playfair_matrix(keyword):
    # Define alphabet and initialize matrix
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' is omitted
    keyword = keyword.upper().replace('J', 'I')  # Handle 'J' in the keyword

    # Remove duplicates from keyword while preserving order
    seen = set()
    keyword_unique = [char for char in keyword if not (char in seen or seen.add(char))]

    # Create matrix with keyword
    matrix = []
    for char in keyword_unique:
        if char not in matrix:
            matrix.append(char)

    # Add remaining letters
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    # Format the matrix into 5x5
    matrix_5x5 = [matrix[i:i + 5] for i in range(0, 25, 5)]

    return matrix_5x5

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))

keyword = "KUNDARILSHT"
matrix = create_playfair_matrix(keyword)
print_matrix(matrix)
print(matrix)
