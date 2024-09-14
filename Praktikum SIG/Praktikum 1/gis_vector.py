# Praktikum 1 Perhitungan jarak antar titik menggunakan Pythagoras
# Dila Ayu Prastita 
# 121140075
# Sistem Informasi Geografis

# Import library yang diperlukan
import numpy as np
import matplotlib.pyplot as plt

# Deklarasi data titik
# Koordinat titik
titik_A = np.array([4.5, 2.5])
titik_B = np.array([5.7, 2.4])

# Hitung Jarak Menggunakan Rumus Pythagoras
def hitung_jarak(titik1, titik2):
    jarak = np.sqrt(np.sum((titik1 - titik2) ** 2))
    return jarak

jarak = hitung_jarak(titik_A, titik_B)
print(f"Jarak antara titik A dan B: {jarak}")

# Visualisasi Titik
plt.scatter(titik_A[0], titik_A[1], color='red', label='Titik A')
plt.scatter(titik_B[0], titik_B[1], color='blue', label='Titik B')
plt.plot([titik_A[0], titik_B[0]], [titik_A[1], titik_B[1]], color='green', linestyle='--')
plt.title('Visualisasi Titik A dan B')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()

# Dokumentasi dan Interpretasi
with open('hasil_jarak.txt', 'w') as file:
    file.write(f'Jarak antara titik A dan B adalah: {jarak}')

