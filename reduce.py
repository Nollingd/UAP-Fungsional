from functools import reduce

angka_ganjil = [angka for angka in range(51) if angka % 2 != 0]
kelipatan_3 = list(filter(lambda x: x % 3 == 0, angka_ganjil))

result = reduce(lambda x, y: x + y, kelipatan_3)
print(result)
