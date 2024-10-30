def selisih_maju(fungsi, T, h=1e-5):
    return (fungsi(T + h) - fungsi(T)) / h

def selisih_mundur(fungsi, T, h=1e-5):
    return (fungsi(T) - fungsi(T - h)) / h

def selisih_tengah(fungsi, T, h=1e-5):
    return (fungsi(T + h) - fungsi(T - h)) / (2 * h)

# Fungsi untuk R(T)
def resistansi_termistor(T):
    return 5000 * np.exp(3500 * (1 / T - 1 / 298))
