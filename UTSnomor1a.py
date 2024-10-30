import numpy as np

def frekuensi_resonansi(R, L=0.5, C=10e-6):
    # Menghitung frekuensi resonansi
    return (1 / (2 * np.pi)) * np.sqrt((1 / (L * C)) - (R**2 / (4 * L**2)))

def turunan_frekuensi_resonansi(R, L=0.5, C=10e-6):
    # Menghitung turunan frekuensi resonansi terhadap R
    return -R / (4 * np.pi * L**2 * np.sqrt((1 / (L * C)) - (R**2 / (4 * L**2)))
