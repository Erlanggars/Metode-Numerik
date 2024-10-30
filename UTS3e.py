import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghitung resistansi R berdasarkan temperatur T
def R(T):
    return 5000 * np.exp(3500 * (1/T - 1/298))

# Metode selisih tengah
def central_difference(T, h):
    return (R(T + h) - R(T - h)) / (2 * h)

# Metode eksak
def exact_derivative(T):
    return (5000 * 3500 * (-1/T**2) * np.exp(3500 * (1/T - 1/298)))

# Metode extrapolasi Richardson
def richardson_extrapolation(T, h):
    central1 = central_difference(T, h)          # Dengan interval h
    central2 = central_difference(T, h / 2)      # Dengan interval h/2
    return (4 * central2 - central1) / 3         # Extrapolasi Richardson

# Range temperatur dan interval
temperatures = np.arange(250, 360, 10)  # Dari 250K sampai 350K
h = 1e-5  # Interval kecil untuk selisih

# Menghitung nilai dR/dT untuk semua metode
exact_results = np.array([exact_derivative(T) for T in temperatures])
richardson_results = np.array([richardson_extrapolation(T, h) for T in temperatures])

# Menghitung error relatif untuk Richardson
richardson_errors = np.abs((richardson_results - exact_results) / exact_results) * 100

# Menampilkan hasil
results = {
    'Temperature (K)': temperatures,
    'Richardson Extrapolation': richardson_results,
    'Exact Derivative': exact_results,
    'Richardson Error (%)': richardson_errors
}

# Memplot hasil
plt.figure(figsize=(10, 6))
plt.plot(temperatures, richardson_errors, marker='o', label='Richardson Error (%)')
plt.xlabel('Temperature (K)')
plt.ylabel('Relative Error (%)')
plt.title('Relative Error of Richardson Extrapolation')
plt.legend()
plt.grid()
plt.show()

results
