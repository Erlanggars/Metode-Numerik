def metode_bisection(fungsi, target, a, b, tol=0.1):
    while abs(b - a) > tol:
        c = (a + b) / 2
        if fungsi(c) - target == 0:
            return c
        elif fungsi(a) * (fungsi(c) - target) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Memanggil metode bisection untuk menemukan nilai R
R_bisection = metode_bisection(lambda R: frekuensi_resonansi(R), 1000, 0, 100)
