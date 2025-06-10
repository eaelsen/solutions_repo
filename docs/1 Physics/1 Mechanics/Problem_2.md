# Problem 2

---

## 🌀 Problem 2: Investigating the Dynamics of a Forced Damped Pendulum

### 🧭 Motivation

The forced damped pendulum showcases the interplay between damping, restoring forces, and external driving. It offers insight into linear vs. nonlinear behavior, including resonance and chaotic dynamics—key phenomena in real-world systems like circuits, bridges, and biomechanics.

---

## 1. 📘 Theoretical Foundation

### General Equation of Motion:

$$
\frac{d^2\theta}{dt^2} + \gamma \frac{d\theta}{dt} + \omega_0^2 \sin\theta = A \cos(\omega t)
$$

Where:

* $\theta$: angular displacement
* $\gamma$: damping coefficient
* $\omega_0$: natural frequency $(\sqrt{g/L})$
* $A$: amplitude of the external force
* $\omega$: driving frequency

### Small-Angle Approximation:

For small $\theta$, $\sin\theta \approx \theta$, giving:

$$
\frac{d^2\theta}{dt^2} + \gamma \frac{d\theta}{dt} + \omega_0^2 \theta = A \cos(\omega t)
$$

This is a linear second-order ODE with periodic forcing. Solutions can exhibit:

* **Underdamping**
* **Resonance** (when $\omega \approx \omega_0$)
* **Steady-state** oscillation

---

## 2. 📊 Analysis of Dynamics

We explore:

* Effects of increasing $\gamma$: faster decay, less oscillation.
* Varying $A$: transition from linear to nonlinear behavior.
* Tuning $\omega$: resonance effects and bifurcations.

### Chaos:

Numerical solutions (no small-angle approx) show:

* **Regular behavior** (periodic or quasiperiodic)
* **Chaotic behavior** (sensitive dependence on initial conditions)

---

## 3. 🌍 Practical Applications

* **RLC circuits** (analogous to the pendulum)
* **Human gait dynamics**
* **Bridge design** (e.g., Tacoma Narrows Bridge collapse)
* **Energy harvesters** using periodic mechanical motion

---

## 4. 💻 Implementation (Python Code)

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
gamma = 0.2      # damping coefficient
omega0 = 1.5     # natural frequency
A = 1.2          # forcing amplitude
omega_d = 2/3    # driving frequency

def pendulum(t, y):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -gamma * omega - omega0**2 * np.sin(theta) + A * np.cos(omega_d * t)
    return [dtheta_dt, domega_dt]

# Initial conditions
y0 = [0.2, 0.0]
t_eval = np.linspace(0, 100, 10000)

# Solve ODE
sol = solve_ivp(pendulum, [0, 100], y0, t_eval=t_eval)

# Plot
plt.figure(figsize=(10, 4))
plt.plot(sol.t, sol.y[0])
plt.title("Forced Damped Pendulum Motion")
plt.xlabel("Time")
plt.ylabel("Theta (rad)")
plt.grid(True)
plt.show()
```

---

### 🔁 Phase Space and Poincaré Section

```python
# Phase portrait
plt.figure()
plt.plot(sol.y[0], sol.y[1], lw=0.5)
plt.title("Phase Space: θ vs ω")
plt.xlabel("Theta")
plt.ylabel("Angular Velocity")
plt.grid(True)
plt.show()

# Poincaré section (sample once every drive period)
T_drive = 2 * np.pi / omega_d
indices = np.arange(int(T_drive / (t_eval[1]-t_eval[0])), len(t_eval), int(T_drive / (t_eval[1]-t_eval[0])))

plt.figure()
plt.plot(sol.y[0][indices], sol.y[1][indices], 'o', markersize=1)
plt.title("Poincaré Section")
plt.xlabel("Theta")
plt.ylabel("Angular Velocity")
plt.grid(True)
plt.show()
```

---

## 🧠 Discussion & Limitations

### Limitations:

* Small-angle approximation fails at large amplitudes.
* Ignores frictional forces with different damping profiles.
* Assumes perfectly periodic driving force.

### Extensions:

* Nonlinear damping: $\propto |\omega|\omega$
* Stochastic or aperiodic driving force
* Double pendulum for richer chaos

---


