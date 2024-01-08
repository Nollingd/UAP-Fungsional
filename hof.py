def kurang(a, b):
    return a - b

def sisagold(fn):
    def wrapper(a, b):
        return fn(a, b)
    return wrapper

fungsi_kurang = sisagold(kurang)

hasil = fungsi_kurang(10, 5)
print(hasil)
