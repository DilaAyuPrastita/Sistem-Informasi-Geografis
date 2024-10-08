# Praktikum 3 Implementasi Buffering pada Titik atau Garis
# Dila Ayu Prastita 
# 121140075
# Sistem Informasi Geografis

# Import library yang diperlukan
from shapely.geometry import LineString
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

#Definisikan Garis dan Jarak Buffer
# Definisi garis
garis = LineString([(1, 1), (5, 5), (8, 1)])

# Jarak buffer (misalnya 1 satuan)
jarak_buffer_garis = 1

# Buat buffer di sekitar garis
buffer_garis = garis.buffer(jarak_buffer_garis)

# Visualisasi
fig, ax = plt.subplots()

# Plot buffer
x, y = buffer_garis.exterior.xy
ax.fill(x, y, alpha=0.5, fc='lightgreen', label='Zona Buffer')

# Plot garis
x, y = garis.xy
ax.plot(x, y, color='blue', label='Garis')
ax.set_title('Buffer di Sekitar Garis')
ax.legend()
plt.grid(True)
plt.show()

# Dokumentasi dan Interpretasi
with open('hasil_buffer_garis.txt', 'w') as file:
    file.write(f'Buffer di sekitar garis: Garis dengan jarak buffer {jarak_buffer_garis}')

    