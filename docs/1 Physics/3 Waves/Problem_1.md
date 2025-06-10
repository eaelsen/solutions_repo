# Problem 1



---

## 🌊 Interference Patterns on a Water Surface

### 🎯 Goal

To analyze how water surface interference patterns form when waves from multiple point sources (e.g., placed at the vertices of a regular polygon) overlap. The project explores constructive and destructive interference through superposition.

---

## 🧮 Wave Equation for a Single Source

$$
\eta(x, y, t) = \frac{A}{\sqrt{r}} \cos(kr - \omega t + \phi)
$$

Where:

* $r = \sqrt{(x - x_0)^2 + (y - y_0)^2}$
* $k = \frac{2\pi}{\lambda}$, $\omega = 2\pi f$

---

## 🔄 Superposition of Multiple Sources

$$
\eta_{\text{total}}(x, y, t) = \sum_{i=1}^{N} \eta_i(x, y, t)
$$

Sources are placed at polygon vertices (e.g., triangle, square, pentagon).

---

## 🧪 Project Steps

1. **Choose a Polygon** (e.g., equilateral triangle)
2. **Position the Sources** at each vertex
3. **Construct Wave Equations** for each source
4. **Superpose** to get total displacement
5. **Visualize** the resulting pattern (at fixed time)
6. **Analyze** areas of constructive vs destructive interference

---

## 💻 Python Implementation Concept

You can use Python with `numpy` and `matplotlib`:

```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 1
λ = 1
k = 2 * np.pi / λ
f = 1
ω = 2 * np.pi * f
t = 0

# Source positions (equilateral triangle for example)
sources = [(0, 1), (-np.sqrt(3)/2, -0.5), (np.sqrt(3)/2, -0.5)]

# Grid
x = np.linspace(-3, 3, 500)
y = np.linspace(-3, 3, 500)
X, Y = np.meshgrid(x, y)
eta_total = np.zeros_like(X)

# Superposition
for x0, y0 in sources:
    r = np.sqrt((X - x0)**2 + (Y - y0)**2)
    eta_total += (A / np.sqrt(r + 1e-6)) * np.cos(k * r - ω * t)

# Plot
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, eta_total, levels=100, cmap='coolwarm')
plt.colorbar(label="Wave Displacement")
plt.title("Interference Pattern on Water Surface")
plt.xlabel("x")
plt.ylabel("y")
plt.axis('equal')
plt.show()
```

---

## 📈 Deliverables

* 📄 Markdown report or Jupyter notebook
* 📊 Visuals of wave patterns for different polygons
* 🔍 Analysis of interference zones

---


