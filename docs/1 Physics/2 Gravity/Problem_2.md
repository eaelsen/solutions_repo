# Problem 2


---

## 🚀 Problem 2: Escape Velocities and Cosmic Velocities

### 🔭 Motivation

Escape and cosmic velocities determine the energy required for a spacecraft to orbit Earth, break free from Earth's gravity, or leave the Solar System. These concepts are fundamental to modern astronautics, including satellite launches, Mars missions, and future interstellar travel.

---

## 1. 📘 Definitions and Physical Meaning

* **First Cosmic Velocity (v₁):** Minimum velocity required to maintain a circular orbit around a planet (orbital speed).

  $$
  v_1 = \sqrt{\frac{GM}{R}}
  $$

* **Second Cosmic Velocity (v₂):** Minimum velocity to escape the gravitational field of a celestial body (escape velocity).

  $$
  v_2 = \sqrt{2} \cdot v_1 = \sqrt{\frac{2GM}{R}}
  $$

* **Third Cosmic Velocity (v₃):** Minimum velocity required to escape the Solar System from Earth's orbit (relative to the Sun).

  $$
  v_3 = \sqrt{\frac{2GM_{\text{sun}}}{R_{\text{earth-orbit}}}} \approx 42.1\,\text{km/s}
  $$

---

## 2. 🧮 Derivations

Derived from **conservation of energy**:

* Kinetic energy vs. gravitational potential energy
* Escape when total mechanical energy ≥ 0

$$
\frac{1}{2}mv^2 = \frac{GMm}{R}
$$

---

## 3. 🌍 Example: Earth, Mars, Jupiter

| Planet  | Radius (m)   | Mass (kg)    |
| ------- | ------------ | ------------ |
| Earth   | 6.371 × 10⁶  | 5.972 × 10²⁴ |
| Mars    | 3.390 × 10⁶  | 6.417 × 10²³ |
| Jupiter | 6.9911 × 10⁷ | 1.898 × 10²⁷ |

---

## 4. 💻 Python Simulation

```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # m³/kg/s²

# Celestial body data
bodies = {
    "Earth": {"R": 6.371e6, "M": 5.972e24},
    "Mars": {"R": 3.390e6, "M": 6.417e23},
    "Jupiter": {"R": 6.9911e7, "M": 1.898e27}
}

# Calculate cosmic velocities
results = {}
for body, data in bodies.items():
    R = data["R"]
    M = data["M"]
    v1 = np.sqrt(G * M / R)
    v2 = np.sqrt(2) * v1
    results[body] = {"v1": v1, "v2": v2}

# Plotting
labels = list(results.keys())
v1_values = [results[b]["v1"] / 1000 for b in labels]  # in km/s
v2_values = [results[b]["v2"] / 1000 for b in labels]

x = np.arange(len(labels))
width = 0.35

plt.figure(figsize=(10, 6))
plt.bar(x - width/2, v1_values, width, label='1st Cosmic Velocity')
plt.bar(x + width/2, v2_values, width, label='2nd Cosmic Velocity')

plt.xticks(x, labels)
plt.ylabel("Velocity (km/s)")
plt.title("Cosmic Velocities for Earth, Mars, Jupiter")
plt.legend()
plt.grid(True)
plt.show()
```

---

## 📈 Visualization

* Bar chart comparing first and second cosmic velocities.
* Demonstrates how planetary mass and radius influence escape speed.

---

## 🌌 Importance in Space Exploration

* **1st Cosmic Velocity**: Launching satellites into stable orbits.
* **2nd Cosmic Velocity**: Interplanetary missions (e.g., Mars rover).
* **3rd Cosmic Velocity**: Escape Solar System (e.g., Voyager 1/2).

---

## 🔁 Extensions

* Include atmospheric drag for realistic models.
* Account for rotation (reduces required launch speed at equator).
* Compare with **rocket equation**: $\Delta v = v_e \ln(m_0/m_f)$

---


