def eliminasi_gauss(A, B):
    """
    Mengimplementasikan metode eliminasi Gauss untuk menyelesaikan sistem persamaan linier.
    """
    n = len(B)
    for i in range(n):
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            B[j] -= factor * B[i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
    X = np.zeros(n)
    for i in range(n-1, -1, -1):
        X[i] = B[i] / A[i][i]
        for j in range(i-1, -1, -1):
            B[j] -= A[j][i] * X[i]
    return X

# Definisikan matriks A dan vektor B
A = [[4, -1, -1], [-1, 3, -1], [-1, -1, 5]]
B = [5, 3, 4]
solusi_gauss = eliminasi_gauss(A, B)
print("Solusi dengan Eliminasi Gauss:", solusi_gauss)
