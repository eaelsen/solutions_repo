# Problem 1



## 🎯 Problem 1: Investigating the Range as a Function of the Angle of Projection

### 🔍 Motivation

Projectile motion offers a rich opportunity to explore fundamental physics. Understanding how range varies with angle helps explain trajectories in sports, engineering, and even space exploration.

---

## 1. 📘 Theoretical Foundation

We begin with the kinematic equations of motion:

* Horizontal motion (constant velocity):

  $$
  x(t) = v_0 \cos(\theta) \cdot t
  $$

* Vertical motion (accelerated):

  $$
  y(t) = v_0 \sin(\theta) \cdot t - \frac{1}{2}gt^2
  $$

To find range $R$, solve for time of flight $T$ when $y(T) = 0$:

$$
T = \frac{2v_0 \sin(\theta)}{g}
$$

Substitute into $x(T)$:

$$
R = \frac{v_0^2 \sin(2\theta)}{g}
$$

This shows range depends on the sine of double the angle. Peak range occurs at $\theta = 45^\circ$.

### 🔄 Family of Solutions

Different values of:

* $v_0$: initial velocity
* $g$: gravitational acceleration
* $\theta$: launch angle

... yield different trajectories and ranges.

---

## 2. 📊 Analysis of the Range

Let’s examine the effect of:

* Angle: $\theta$ in \[0°, 90°]
* $v_0 =$ constant values
* $g = 9.81\,m/s^2$

We'll plot $R(\theta)$ for different $v_0$.

---

## 3. 🌍 Practical Applications

* Uneven terrain: introduces asymmetric time of flight.
* Air resistance: breaks ideal symmetry; reduces range.
* Launch height ≠ 0: requires full quadratic solution for $y(t) = 0$

---

## 4. 💻 Implementation (Python Code)

```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # m/s²
angles = np.linspace(0, 90, 500)  # degrees
angles_rad = np.radians(angles)

# Test different velocities
velocities = [10, 20, 30]  # m/s

plt.figure(figsize=(10, 6))
for v0 in velocities:
    R = (v0 ** 2) * np.sin(2 * angles_rad) / g
    plt.plot(angles, R, label=f'v0 = {v0} m/s')

plt.title("Projectile Range vs Angle of Projection")
plt.xlabel("Angle (degrees)")
plt.ylabel("Range (m)")
plt.legend()
plt.grid(True)
plt.show()
```

---

## 📈 Graphical Insights

The graphs will show:

* Symmetric curve peaking at 45°
* Higher initial velocity → longer range
* Sensitivity to angle increases with speed

---

## ⚠️ Limitations and Real-World Factors

* **Air drag**: can reduce range significantly
* **Launch height**: modifies time of flight
* **Wind and spin**: introduce lift or drag effects
* **Non-constant gravity** (e.g., rocket dynamics)

### 💡 Future Improvements

* Include drag force: $F_d = -kv^2$
* Vary $g$ (e.g., Moon, Mars simulations)
* Add terrain modeling

---


