import numpy as np

# Fungsi untuk menghitung determinan matriks menggunakan ekspansi kofaktor
def determinant(A):
    n = A.shape[0]
    if n == 1:
        return A[0, 0]
    elif n == 2:
        return A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]

    det = 0
    for c in range(n):
        minor = np.delete(np.delete(A, 0, axis=0), c, axis=1)
        det += ((-1) ** c) * A[0, c] * determinant(minor)

    return det

# Fungsi untuk menghitung invers matriks menggunakan metode adjoin
def inverse_matrix(A):
    det_A = determinant(A)
    if det_A == 0:
        raise ValueError("Matriks tidak dapat di-inversi (determinannya nol).")
    
    n = A.shape[0]
    adjugate = np.zeros_like(A, dtype=float)

    for i in range(n):
        for j in range(n):
            # Menghitung minor dengan menghapus baris i dan kolom j
            minor = np.delete(np.delete(A, i, axis=0), j, axis=1)
            # Menghitung kofaktor
            adjugate[j, i] = ((-1) ** (i + j)) * determinant(minor)

    # Mengembalikan invers matriks
    return adjugate / det_A

# Matriks koefisien dari sistem persamaan
A = np.array([[4, -1, -1],
              [-1, 3, -1],
              [-1, -1, 5]])

# Menghitung invers matriks
inverse_A = inverse_matrix(A)

inverse_A
