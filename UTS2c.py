def gauss_jordan(A, B):
    """
    Mengimplementasikan metode Gauss-Jordan untuk menyelesaikan sistem persamaan linier.
    """
    n = len(B)
    for i in range(n):
        # Normalisasi baris
        factor = A[i][i]
        for j in range(n):
            A[i][j] /= factor
        B[i] /= factor
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(n):
                    A[k][j] -= factor * A[i][j]
                B[k] -= factor * B[i]
    return B

solusi_gauss_jordan = gauss_jordan(A, B)
print("Solusi dengan Gauss-Jordan:", solusi_gauss_jordan)
