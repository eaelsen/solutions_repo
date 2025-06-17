# Problem 2


---

## 🧠 Theoretical Foundation

The **forced damped pendulum** is a system that combines:

* Restoring force (gravity)
* Damping force (e.g., friction or air resistance)
* Periodic external driving force (like a motor)

### ⚙️ Differential Equation of Motion

The motion is governed by the second-order nonlinear differential equation:

$$
\frac{d^2\theta}{dt^2} + b\frac{d\theta}{dt} + \omega_0^2 \sin\theta = A \cos(\omega t)
$$

Where:

* $\theta(t)$: Angular displacement as a function of time
* $b$: Damping coefficient
* $\omega_0$: Natural frequency of the undamped pendulum ($\omega_0 = \sqrt{\frac{g}{L}}$)
* $A$: Amplitude of external forcing
* $\omega$: Angular frequency of the external driving force

---

### 🔍 Linear Approximation (Small-Angle)

For small oscillations, where $\sin \theta \approx \theta$, the equation simplifies to:

$$
\frac{d^2\theta}{dt^2} + b\frac{d\theta}{dt} + \omega_0^2 \theta = A \cos(\omega t)
$$

This is the **driven damped harmonic oscillator** equation.

---

## 📊 Analysis of Dynamics

By varying parameters like:

* Damping ($b$)
* Driving amplitude ($A$)
* Driving frequency ($\omega$)

You can observe different behaviors:

* **Underdamped motion**: Gradual decay
* **Resonance**: Maximal response at driving frequency $\omega \approx \omega_0$
* **Chaotic behavior**: Sensitive dependence on initial conditions

### 📌 Transition to Chaos

As you increase the driving strength or tweak parameters, the system can shift from **regular periodic** motion to **chaotic** motion — i.e., irregular, unpredictable behavior that is still deterministic.

---

## 🛠️ Practical Applications

The forced damped pendulum model is relevant to:

* Energy harvesting systems (piezoelectric, electromagnetic)
* Bridge and building dynamics (e.g., damping in skyscrapers)
* Clock escapements
* RLC circuits (analogous systems in electrical engineering)

---

## 📐 Implementation (Conceptual Steps)

1. **Model Setup**:

   * Define the equation of motion
   * Choose parameter sets (damping, amplitude, frequency)

2. **Numerical Integration**:

   * Use numerical methods (e.g., Runge-Kutta) for solving the differential equation

3. **Phase Space Analysis**:

   * Plot phase portraits ($\theta$ vs. $\dot{\theta}$)
   * Create Poincaré sections (sample the system once every driving cycle)

4. **Bifurcation Diagrams**:

   * Show transitions in motion as a parameter (e.g., $A$ or $\omega$) is varied

---

## 📦 Deliverables Summary (Conceptual)

* Theoretical derivation of the motion
* Visuals: trajectories, phase diagrams, bifurcation plots
* Discussion on regular vs. chaotic motion
* Insights on physical meaning and real-world parallels

---
