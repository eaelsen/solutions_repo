# Problem 3

---

## 🌌 Problem 3: Trajectories of a Freely Released Payload Near Earth

### 🚀 Motivation

Understanding the motion of a payload released from a moving spacecraft is critical for mission design—whether for orbit insertion, satellite deployment, or Earth reentry. This problem blends Newtonian gravity, Keplerian orbits, and numerical simulations.

---

## 1. 📘 Theoretical Foundation

### Orbital Trajectories:

Depending on total mechanical energy $E$, a released payload may follow:

* **Elliptical orbit** ($E < 0$)
* **Parabolic escape** ($E = 0$)
* **Hyperbolic escape** ($E > 0$)

Use:

$$
E = \frac{1}{2}mv^2 - \frac{GMm}{r}
$$

And angular momentum conservation to derive trajectory type.

---

## 2. 💻 Simulation Overview

We'll simulate the trajectory using Newton's gravitational force:

$$
\vec{F} = -\frac{GMm}{r^3}\vec{r}
$$

Use the **Runge-Kutta** or **Velocity Verlet** method to update:

* Position $\vec{r}$
* Velocity $\vec{v}$

### Inputs:

* Initial position $\vec{r}_0$
* Initial velocity $\vec{v}_0$
* Altitude, direction, and speed

---

## 3. 🧠 Physical Interpretations

* **Orbital Insertion**: Initial $v$ < escape velocity, tangential direction.
* **Reentry**: Suborbital trajectory intersecting Earth.
* **Escape**: $v > v_{escape}$, hyperbolic path.

---

## 4. 💻 Python Implementation Outline

```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11
M = 5.972e24  # Earth mass
R_earth = 6.371e6  # Earth radius

def gravity(r):
    r_mag = np.linalg.norm(r)
    return -G * M * r / r_mag**3

# Initial conditions
altitude = 400e3  # 400 km above surface
r0 = np.array([R_earth + altitude, 0])
v0 = np.array([0, 7500])  # initial speed in m/s

# Simulation
dt = 1  # time step (s)
t_max = 6000
steps = int(t_max / dt)

r = np.zeros((steps, 2))
v = np.zeros((steps, 2))
r[0], v[0] = r0, v0

for i in range(steps - 1):
    a = gravity(r[i])
    v[i+1] = v[i] + a * dt
    r[i+1] = r[i] + v[i+1] * dt

# Plot trajectory
plt.figure(figsize=(8, 8))
earth = plt.Circle((0, 0), R_earth, color='blue', alpha=0.3)
plt.gca().add_patch(earth)
plt.plot(r[:, 0], r[:, 1])
plt.axis('equal')
plt.title("Payload Trajectory Near Earth")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.grid(True)
plt.show()
```

---

## 📈 Visualizations

* Orbit trajectory (2D path)
* Overlay Earth as a circle
* Show variations for different velocities: orbital, suborbital, escape

---

## 🧠 Insights and Applications

* Simulate **satellite deployment**
* Predict **crash or reentry** scenarios
* Model **escape trajectories** for Moon or Mars missions

---


