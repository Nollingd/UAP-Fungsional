def hitung_pangkat(pangkat):
    def pangkat_bilangan(angka):
        return angka ** pangkat
    return pangkat_bilangan

pangkat_2 = hitung_pangkat(2)

#contoh inputan
print(pangkat_2(5))  