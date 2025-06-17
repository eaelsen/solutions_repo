# Problem 1


---

# 🌊 **Interference Patterns on a Water Surface from Multiple Sources**

---

## 🎯 **Motivation**

Interference is a core concept in wave physics and occurs when two or more waves meet, resulting in a new wave pattern. These interactions can either:

* **Constructively interfere** (amplify the wave)
* **Destructively interfere** (cancel out)

On a **water surface**, this is beautifully visualized through **ripple patterns** created when multiple point sources generate waves simultaneously. These ripples overlap and form **interference fringes**—regions of constructive and destructive interference—that resemble intricate patterns.

Studying interference patterns on water gives learners an intuitive and visual grasp of:

* Superposition of waves
* Coherence and phase
* Wave geometry and symmetry
* Real-world applications, such as acoustics, optics, antenna arrays, and sonar systems

This project allows for a **hands-on and visual approach** to understanding wave behavior, combining analytical theory with numerical simulations and beautiful graphics.
![Interference Pattern](interference_pattern.png)

---

## 🌐 **Wave from a Single Point Source**

The displacement of the water surface $\eta(x, y, t)$ from a **single point source** located at $(x_0, y_0)$ is modeled as:

$$
\eta(x, y, t) = \frac{A}{\sqrt{r}} \cos \left(kr - \omega t + \phi\right)
$$

Where:

* $\eta(x, y, t)$: Surface displacement at position $(x, y)$ and time $t$
* $A$: Amplitude of the wave
* $r = \sqrt{(x - x_0)^2 + (y - y_0)^2}$: Distance from source to point
* $k = \frac{2\pi}{\lambda}$: Wave number (related to wavelength $\lambda$)
* $\omega = 2\pi f$: Angular frequency (related to frequency $f$)
* $\phi$: Initial phase of the wave

---

## 🧩 **Problem Statement**

The project investigates **interference patterns** created on the water surface by placing **multiple point wave sources** at the vertices of a **regular polygon** (e.g., equilateral triangle, square, pentagon, etc.).

The aim is to **analyze and visualize the superposition** of these waves and interpret the resulting interference patterns.

---

## 🔁 **Steps to Follow**

### 🔸 1. **Choose a Regular Polygon**

Select a geometric shape such as:

* Equilateral triangle (3 sources)
* Square (4 sources)
* Regular pentagon (5 sources)
* Hexagon, heptagon, etc.

### 🔸 2. **Place Sources at Vertices**

Position point wave sources at each of the polygon’s vertices. Assume:

* Same amplitude $A$
* Same wavelength $\lambda$
* Same frequency $f$
* Possibly the same phase

### 🔸 3. **Write the Individual Wave Equations**

For each source $i$, compute the wave displacement at any point $(x, y)$ on the water surface:

$$
\eta_i(x, y, t) = \frac{A}{\sqrt{r_i}} \cos(k r_i - \omega t + \phi_i)
$$

Where $r_i$ is the distance from source $i$ to the point $(x, y)$.

### 🔸 4. **Apply Superposition**

Total wave displacement at $(x, y, t)$ is:

$$
\eta_{\text{total}}(x, y, t) = \sum_{i=1}^{N} \eta_i(x, y, t)
$$

Where $N$ is the number of sources (vertices of the polygon).

---

## 🔬 **Analysis Objectives**

### ✅ 1. **Interference Analysis**

* Identify regions where waves **amplify** (constructive interference)
* Locate zones of **cancellation** (destructive interference)
* Examine symmetry and repeating patterns
* Study how geometry (polygon type) affects pattern structure

### ✅ 2. **Visualization**

Use graphical tools (like Python’s `matplotlib`, `numpy`, or `matplotlib.animation`) to:

* Plot instantaneous wave patterns at time $t$
* Display interference fringes and nodal lines
* Animate the surface to visualize wave propagation dynamically

---

## 🔄 **Considerations**

* Assume all sources are **in phase** for symmetric patterns; vary phase to see changes
* Constant amplitude and frequency for simplicity
* Superposition principle is **linear**, valid for small amplitude waves
* The model is 2D and assumes **non-dispersive waves** (wavelength does not vary with frequency)

---

## 🧠 **Real-World Relevance**

Interference is fundamental to:

* Sonar, radar, and ultrasound
* Laser diffraction
* Optical grating and interference filters
* Engineering (e.g., phased array antennas)
* Quantum interference and wavefunction analysis

This project provides a foundation for both **classical wave mechanics** and more advanced **wave-based technologies**.

---

## 📦 **Deliverables**

1. **Markdown or Jupyter Notebook**

   * Includes theoretical background, polygon setup, and code for superposition and visualization

2. **Written Explanation**

   * Discussion of wave equations, interference phenomena, geometric configurations, and implications

3. **Graphs and Visuals**

   * Static images of interference patterns
   * Animated simulations (optional)
   * Comparative visuals for different polygon shapes and phase conditions

---
