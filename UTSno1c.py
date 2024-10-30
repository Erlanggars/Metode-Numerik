def metode_newton_raphson(fungsi, turunan, target, R0, tol=0.1, max_iter=100):
    R = R0
    for i in range(max_iter):
        f_val = fungsi(R) - target
        f_prime = turunan(R)
        R_next = R - f_val / f_prime
        if abs(R_next - R) < tol:
            return R_next
        R = R_next
    return R

# Memanggil metode Newton-Raphson untuk menemukan nilai R
R_newton = metode_newton_raphson(frekuensi_resonansi, turunan_frekuensi_resonansi, 1000, 50)
