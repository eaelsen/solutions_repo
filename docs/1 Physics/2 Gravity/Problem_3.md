# Problem 3

---

# 🛰️ **Trajectories of a Freely Released Payload Near Earth**

---

## 🌍 **Motivation**

When a payload is released from a moving spacecraft near Earth, its subsequent **trajectory** depends entirely on its **initial velocity**, **direction**, **altitude**, and the **gravitational pull of Earth**. The motion could lead to a variety of paths:

* **Reentry to Earth**
* **Stable orbit**
* **Escape from Earth’s gravity**

This problem beautifully combines **orbital mechanics** and **computational physics**, making it a rich area of study for students and professionals interested in spaceflight, mission planning, and gravity-dominated motion.

Understanding these trajectory outcomes is **crucial for**:

* Satellite deployment
* Space station rendezvous
* Space tourism safety
* Planetary reentry
* Interplanetary travel planning

---

## 📘 **Theoretical Background**

To model the trajectory of a payload near Earth, we apply:

### 1. **Newton’s Law of Universal Gravitation**

$$
F = \frac{GMm}{r^2}
$$

Where:

* $F$: Gravitational force
* $G$: Gravitational constant
* $M$: Mass of Earth
* $m$: Mass of payload
* $r$: Distance from Earth's center to payload

---

### 2. **Equation of Motion**

Using Newton's Second Law:

$$
\vec{F} = m\vec{a} \Rightarrow \vec{a} = -\frac{GM}{r^2} \hat{r}
$$

This leads to a **second-order differential equation** for the position $\vec{r}(t)$, which usually requires **numerical integration** (e.g., Runge-Kutta methods) to solve for complex cases.

---

### 3. **Energy and Trajectory Types**

The total mechanical energy determines the trajectory type:

$$
E = \frac{1}{2}mv^2 - \frac{GMm}{r}
$$

Based on $E$:

* **Elliptical orbit**: $E < 0$
* **Parabolic trajectory (escape)**: $E = 0$
* **Hyperbolic trajectory (escape with excess energy)**: $E > 0$

---

### 4. **Escape Velocity Revisited**

To determine if the payload will escape Earth, we calculate:

$$
v_{\text{escape}} = \sqrt{\frac{2GM}{r}}
$$

If the payload’s speed $v > v_{\text{escape}}$, it **escapes** Earth’s gravity.

---

## 🚀 **Tasks and Analysis**

### ✅ 1. **Trajectory Classification**

Depending on:

* Initial speed
* Direction of velocity vector
* Altitude from Earth’s surface

The payload may:

* **Fall back** to Earth (suborbital)
* **Enter a circular or elliptical orbit**
* **Escape** Earth (if $v \geq v_{\text{escape}}$)
* **Reenter** in a ballistic trajectory

### ✅ 2. **Numerical Simulation**

Using Newtonian mechanics and a numerical integrator (e.g., Runge-Kutta 4th order), simulate the payload's path in 2D (or 3D) space. Vary:

* Launch angle
* Initial velocity
* Altitude

Plot position over time to visualize the resulting path.

### ✅ 3. **Orbital Insertion and Reentry Conditions**

Determine:

* What minimum velocity at what altitude yields a stable orbit
* What trajectories lead to **reentry** within one or multiple revolutions
* What speeds and directions ensure **safe deployment** or intentional deorbiting

---

## 🛰️ **Practical Applications**

* **Satellite Launches**: Ensuring correct velocity and direction for orbit insertion
* **Spacecraft Reentry**: Predicting where and when reentry occurs for safety
* **Lunar Missions**: Calculating Earth departure conditions
* **Debris Management**: Simulating where discarded stages will fall or orbit

---

## 📐 **Simulation & Visualization**

Suggested simulation features:

* Simulate motion in Earth’s gravity from different altitudes (e.g., 100 km to 1000 km)
* Show:

  * Circular orbits
  * Escape trajectories
  * Reentry arcs
* Plot:

  * Position vs. time
  * Energy vs. time
  * Phase-space diagrams
  * Trajectory overlaid on Earth diagram

---

## 📊 **Graphical Representations**

1. **Trajectory Maps**: Path of payload in real-time orbits
2. **Energy Diagrams**: Visualize when total energy crosses 0 (escape)
3. **Altitude vs. Time**: To identify orbital decay or escape
4. **Velocity Vectors**: To show direction and magnitude throughout motion

---

## 📦 **Deliverables Summary**

1. **Markdown / Notebook**:

   * Equations
   * Simulation results
   * Trajectory plots

2. **Detailed Report**:

   * Explanation of orbital mechanics
   * Energy analysis
   * Classifications of outcomes

3. **Graphs and Diagrams**:

   * Trajectories for various conditions
   * Escape velocities at different altitudes
   * Energy-time plots

---

## 🌠 **Summary**

This project allows you to explore **gravity-dominated motion** in a realistic, computationally rich context. By studying the trajectories of a freely released payload:

* You apply Newton’s laws in a practical way
* Simulate satellite and spacecraft motion
* Prepare for more complex astrodynamics topics like multi-body interactions or maneuver planning

---
