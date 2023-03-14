# 1den 100 e kadar olan pisagor 3lülerini bulan fonksiyon


def p():
    for a in range(1,101):
        for b in range(a,101):
            c=(a**2+b**2)**0.5
            if c == int(c) and c<=100:
                print(f"{a}, {b}, {int(c)}")


p()