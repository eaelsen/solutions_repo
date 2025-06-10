# Problem 1

---

## 🌍 Problem 1: Orbital Period and Orbital Radius

### 🚀 Motivation

Kepler’s Third Law reveals a deep connection between time and space in orbital mechanics: the square of a planet's orbital period is proportional to the cube of its orbital radius. This law forms a bridge between observation and Newtonian gravitation, enabling predictions of satellite behavior, moon motion, and planetary distances.

---

## 1. 📘 Theoretical Foundation

### Newton’s Law of Gravitation:

$$
F = \frac{GMm}{r^2}
$$

### Centripetal Force for Circular Motion:

$$
F = \frac{mv^2}{r}
$$

Equating the two:

$$
\frac{GMm}{r^2} = \frac{mv^2}{r}
$$

$$
v = \sqrt{\frac{GM}{r}}
$$

Period $T$ is the time to complete one orbit:

$$
T = \frac{2\pi r}{v} = 2\pi r \sqrt{\frac{r}{GM}} = 2\pi \sqrt{\frac{r^3}{GM}}
$$

### Final Form of Kepler's Third Law:

$$
T^2 \propto r^3
$$

---

## 2. 🧠 Implications for Astronomy

* Allows estimation of **planetary masses** and **orbital distances**.
* Explains consistent behavior across moons, planets, and satellites.
* Groundwork for Newton’s universal law of gravitation.

---

## 3. 🌍 Real-World Examples

### Example 1: The Moon around Earth

* Radius: $r \approx 384,400$ km
* Period: $T \approx 27.3$ days
* Use to verify $T^2 \propto r^3$

### Example 2: Planets in the Solar System

Compare $\frac{T^2}{r^3}$ across planets—should be nearly constant.

---

## 4. 💻 Python Simulation and Verification

```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # gravitational constant (m^3/kg/s^2)
M = 1.989e30     # mass of the Sun (kg)

# Orbital radii (m) and periods (s) of planets
planet_data = {
    'Mercury': (5.79e10, 7.60e6),
    'Venus': (1.08e11, 1.94e7),
    'Earth': (1.50e11, 3.15e7),
    'Mars': (2.28e11, 5.94e7),
    'Jupiter': (7.78e11, 3.74e8),
    'Saturn': (1.43e12, 9.29e8)
}

# Calculate T^2 and R^3
radii = []
t_squared = []
r_cubed = []

for planet, (r, T) in planet_data.items():
    radii.append(r)
    t_squared.append(T**2)
    r_cubed.append(r**3)

# Plot
plt.figure(figsize=(8, 6))
plt.loglog(r_cubed, t_squared, 'o-')
plt.xlabel("Orbital Radius³ (m³)")
plt.ylabel("Orbital Period² (s²)")
plt.title("Verification of Kepler's Third Law")
plt.grid(True)
plt.show()
```

---

## 📈 Visualization

* Log-log plot of $T^2$ vs $r^3$ should yield a straight line.
* Confirms that $T^2 \propto r^3$ for all major planets.

---

## 📉 Beyond Circular Orbits

* For elliptical orbits, Kepler’s Third Law still holds with:

  $$
  T^2 = \frac{4\pi^2 a^3}{GM}
  $$

  where $a$ is the semi-major axis.
* Used in binary star systems, exoplanets, and orbital transfer calculations.

---

