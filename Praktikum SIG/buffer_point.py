# Praktikum 3 Implementasi Buffering pada Titik atau Garis
# Dila Ayu Prastita 
# 121140075
# Sistem Informasi Geografis

# Import library yang diperlukan
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from shapely.geometry import Point


# Definisi titik
titik = Point(5, 5)

# Jarak buffer (misalnya 2 satuan)
jarak_buffer = 2

# Buat buffer di sekitar titik
buffer_titik = titik.buffer(jarak_buffer)

# Visualisasi
fig, ax = plt.subplots()

# Plot buffer
x, y = buffer_titik.exterior.xy
ax.fill(x, y, alpha=0.5, fc='lightblue', label='Zona Buffer')

# Plot titik
ax.scatter(titik.x, titik.y, color='red', label='Titik')

ax.set_title('Buffer di Sekitar Titik')
ax.legend()
plt.grid(True)
plt.show()

# Dokumentasi dan Interpretasi
with open('hasil_buffer_titik.txt', 'w') as file:
    file.write(f'Buffer di sekitar titik: Pusat di {titik}, dengan jarak buffer {jarak_buffer}')

