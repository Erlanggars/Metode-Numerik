import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghitung resistansi R berdasarkan temperatur T
def R(T):
    return 5000 * np.exp(3500 * (1/T - 1/298))

# Metode selisih maju
def forward_difference(T, h):
    return (R(T + h) - R(T)) / h

# Metode selisih mundur
def backward_difference(T, h):
    return (R(T) - R(T - h)) / h

# Metode selisih tengah
def central_difference(T, h):
    return (R(T + h) - R(T - h)) / (2 * h)

# Metode eksak
def exact_derivative(T):
    return (5000 * 3500 * (-1/T**2) * np.exp(3500 * (1/T - 1/298)))

# Range temperatur dan interval
temperatures = np.arange(250, 360, 10)  # Dari 250K sampai 350K
h = 1e-5  # Interval kecil untuk selisih

# Menghitung nilai dR/dT untuk semua metode
forward_results = np.array([forward_difference(T, h) for T in temperatures])
backward_results = np.array([backward_difference(T, h) for T in temperatures])
central_results = np.array([central_difference(T, h) for T in temperatures])
exact_results = np.array([exact_derivative(T) for T in temperatures])

# Menghitung error relatif untuk metode numerik
forward_errors = np.abs((forward_results - exact_results) / exact_results) * 100
backward_errors = np.abs((backward_results - exact_results) / exact_results) * 100
central_errors = np.abs((central_results - exact_results) / exact_results) * 100

# Memplot error relatif
plt.figure(figsize=(10, 6))
plt.plot(temperatures, forward_errors, marker='o', label='Forward Difference Error (%)')
plt.plot(temperatures, backward_errors, marker='o', label='Backward Difference Error (%)')
plt.plot(temperatures, central_errors, marker='o', label='Central Difference Error (%)')
plt.xlabel('Temperature (K)')
plt.ylabel('Relative Error (%)')
plt.title('Relative Error for Numerical Differentiation Methods')
plt.legend()
plt.grid()
plt.show()
