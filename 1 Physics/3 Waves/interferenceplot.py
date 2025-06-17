import numpy as np
import matplotlib.pyplot as plt

# Parametreler
A = 1
wavelength = 1
frequency = 1
omega = 2 * np.pi * frequency
k = 2 * np.pi / wavelength
phi = 0
num_sources = 4
radius = 3
grid_size = 300

# Grid
x = np.linspace(-5, 5, grid_size)
y = np.linspace(-5, 5, grid_size)
X, Y = np.meshgrid(x, y)

# Kaynak konumları (kare)
angles = np.linspace(0, 2 * np.pi, num_sources, endpoint=False)
source_positions = [(radius * np.cos(a), radius * np.sin(a)) for a in angles]

# Toplam dalga yüksekliği
eta_total = np.zeros_like(X)
for (x0, y0) in source_positions:
    r = np.sqrt((X - x0)**2 + (Y - y0)**2)
    eta = A / np.sqrt(r + 1e-6) * np.cos(k * r - omega * 0 + phi)
    eta_total += eta

# Görselleştirme
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, eta_total, levels=100, cmap='RdBu_r')
plt.colorbar(label='Wave Amplitude')
plt.scatter(*zip(*source_positions), color='black', label='Wave Sources')
plt.title(f'Interference Pattern from {num_sources} Point Sources (Square)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.axis('equal')
plt.tight_layout()
plt.savefig("interference_pattern.png")  # Dosyaya kaydeder
plt.show()
