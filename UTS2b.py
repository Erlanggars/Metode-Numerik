def determinan(matrix):
    """
    Menghitung determinan matriks menggunakan ekspansi kofaktor.
    """
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for c in range(len(matrix)):
        minor = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinan(minor)
    return det
