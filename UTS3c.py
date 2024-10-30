import math
import matplotlib.pyplot as plt

# Fungsi resistansi berdasarkan temperatur
def R(T):
    return 5000 * math.exp(3500 * (1 / T - 1 / 298))

# Fungsi-fungsi diferensiasi
def forward_difference(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

def backward_difference(f, x, h=1e-5):
    return (f(x) - f(x - h)) / h

def central_difference(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

# Turunan eksak dR/dT
def exact_derivative_R(T):
    return -5000 * 3500 * math.exp(3500 * (1 / T - 1 / 298)) / T ** 2

# Rentang temperatur dari 250K sampai 350K dengan interval 10K
T_values = list(range(250, 351, 10))

# Menghitung turunan menggunakan metode berbeda
forward_diff = [forward_difference(R, T) for T in T_values]
backward_diff = [backward_difference(R, T) for T in T_values]
central_diff = [central_difference(R, T) for T in T_values]
exact_diff = [exact_derivative_R(T) for T in T_values]

# Menampilkan hasil perhitungan
print("T (K) | Forward Diff | Backward Diff | Central Diff | Exact Diff")
print("---------------------------------------------------------------")
for i, T in enumerate(T_values):
    print(f"{T:5} | {forward_diff[i]:12.6f} | {backward_diff[i]:13.6f} | {central_diff[i]:12.6f} | {exact_diff[i]:11.6f}")

# Visualisasi hasil turunan
plt.plot(T_values, forward_diff, label='Selisih Maju')
plt.plot(T_values, backward_diff, label='Selisih Mundur')
plt.plot(T_values, central_diff, label='Selisih Tengah')
plt.plot(T_values, exact_diff, label='Eksak', linestyle='--')
plt.xlabel('Temperatur (K)')
plt.ylabel('dR/dT')
plt.legend()
plt.title("Perbandingan Metode Diferensiasi Numerik pada Rentang Suhu")
plt.show()
