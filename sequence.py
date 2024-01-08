data_tuple = ('Pensil', 1500, 'Buku', 5000, 'Penggaris', 2000)

def split_data(data):
    items = []
    prices = []
    for i in range(0, len(data), 2):
        items.append(data[i])
        prices.append(data[i + 1])
    return items, prices

barang, harga = split_data(data_tuple)

def create_dictionary(items, prices):
    return dict(zip(items, prices))

barang_harga_dict = create_dictionary(barang, harga)

print(data_tuple)
print(barang, harga)
print(barang_harga_dict)
