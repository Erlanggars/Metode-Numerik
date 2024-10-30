import matplotlib.pyplot as plt

# Visualisasi konvergensi kedua metode
toleransi = 0.1
R_values_bisection = []
R_values_newton = []

# Konvergensi Bisection
a, b = 0, 100
while abs(b - a) > toleransi:
    c = (a + b) / 2
    R_values_bisection.append(c)
    if frekuensi_resonansi(c) < 1000:
        a = c
    else:
        b = c

# Konvergensi Newton-Raphson
R = 50
for _ in range(10):
    R_values_newton.append(R)
    R -= (frekuensi_resonansi(R) - 1000) / turunan_frekuensi_resonansi(R)

# Plot hasil konvergensi
plt.plot(R_values_bisection, label="Bisection")
plt.plot(R_values_newton, label="Newton-Raphson", marker='o')
plt.xlabel("Iterasi")
plt.ylabel("Nilai R")
plt.legend()
plt.title("Perbandingan Konvergensi Bisection dan Newton-Raphson")
plt.show()
