import matplotlib.pyplot as plt
import numpy as np

# Membuat data koordinat titik (contoh: (1, 2), (2, 3), (3, -1))
x = [1, 2, 3]
y = [2, 3, -1]

# Membuat figur dan sumbu
fig, ax = plt.subplots()

# Mengatur letak sumbu X dan Y di titik (0,0)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Plot titik-titik koordinat
ax.scatter(x, y, color='red', zorder=5)

# Memberi label pada setiap titik
for i, txt in enumerate(zip(x, y)):
    ax.annotate(f'({txt[0]}, {txt[1]})', (txt[0], txt[1]), textcoords="offset points", xytext=(0,10), ha='center')

# Mengatur batas sumbu
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# Menambahkan grid
ax.grid(True, linestyle='--', alpha=0.6)

# Judul dan keterangan
plt.title('Contoh Diagram Kartesius', pad=15)
plt.xlabel('Sumbu X', loc='right')
plt.ylabel('Sumbu Y', loc='top')

# Menampilkan grafik
plt.show()
