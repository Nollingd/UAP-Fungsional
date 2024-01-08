import matplotlib.pyplot as plt

data = [
    ('Bus', 5, 200),
    ('Trem', 8, 150),
    ('Kereta', 12, 300),
    ('Minibus', 8, 100),
    ('Tram', 9, 220)
]

# Pisahkan data
jenis_kendaraan, penggunaan_energi, biaya_operasional = zip(*data)

plt.figure(figsize=(15, 5))

# Visualisasi data penggunaan energi
plt.subplot(1, 3, 1)
plt.bar(jenis_kendaraan, penggunaan_energi, color='skyblue')
plt.title('Penggunaan Energi per KM')
plt.xlabel('Jenis Kendaraan')
plt.ylabel('Penggunaan Energi')
plt.xticks(rotation=45)

# Visualisasi data biaya operasional
plt.subplot(1, 3, 2)
plt.bar(jenis_kendaraan, biaya_operasional, color='skyblue')
plt.title('Biaya Operasional per KM')
plt.xlabel('Jenis Kendaraan')
plt.ylabel('Biaya Operasional')
plt.xticks(rotation=45)

# Visualisasi scatter plot hubungan antara penggunaan energi dan biaya operasional
plt.subplot(1, 3, 3)
plt.scatter(penggunaan_energi, biaya_operasional, color='blue')
plt.title('Hubungan Biaya dan Energi')
plt.xlabel('Penggunaan Energi')
plt.ylabel('Biaya Operasional')

# Memberikan label pada tiap titik
for i, kendaraan in enumerate(jenis_kendaraan):
    plt.text(penggunaan_energi[i], biaya_operasional[i], kendaraan, ha='right')

# Menambahkan legenda dengan label "jenis_kendaraan"
plt.legend(['jenis_kendaraan'], loc='upper left')

# Menampilkan plot
plt.tight_layout()
plt.show()
