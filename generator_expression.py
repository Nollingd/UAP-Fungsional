generator_angka_ganjil = (angka for angka in range(51) if angka % 2 != 0)

for angka in generator_angka_ganjil:
    print(angka, end=', ')