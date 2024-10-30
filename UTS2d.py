import numpy as np

# Fungsi untuk menyelesaikan sistem persamaan linier menggunakan metode eliminasi Gauss
def gauss_elimination(A, b):
    n = len(b)
    Ab = np.hstack([A, b.reshape(-1, 1)])  # Gabungkan A dan b menjadi augmented matrix
    
    # Eliminasi ke bentuk segitiga
    for i in range(n):
        Ab[i] = Ab[i] / Ab[i][i]  # Normalisasi pivot
        for j in range(i + 1, n):
            Ab[j] -= Ab[i] * Ab[j][i]
    
    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i][-1] - np.sum(Ab[i][i + 1:n] * x[i + 1:n])
    
    return x

# Fungsi untuk menyelesaikan sistem persamaan linier menggunakan metode Gauss-Jordan
def gauss_jordan(A, b):
    n = len(b)
    Ab = np.hstack([A, b.reshape(-1, 1)])  # Gabungkan A dan b menjadi augmented matrix
    
    # Gauss-Jordan elimination
    for i in range(n):
        Ab[i] = Ab[i] / Ab[i][i]  # Normalisasi pivot
        for j in range(n):
            if i != j:
                Ab[j] -= Ab[i] * Ab[j][i]  # Eliminasi di seluruh baris
    
    return Ab[:, -1]  # Mengembalikan solusi

# Matriks koefisien dan vektor konstanta
A = np.array([[4, -1, -1],
              [-1, 3, -1],
              [-1, -1, 5]])

b = np.array([5, 3, 4])

# Menggunakan metode eliminasi Gauss
solution_gauss = gauss_elimination(A, b)

# Menggunakan metode Gauss-Jordan
solution_gauss_jordan = gauss_jordan(A, b)

# Menampilkan hasil
solution_gauss, solution_gauss_jordan
