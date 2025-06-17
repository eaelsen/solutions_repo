# Problem 1

---

# **Orbital Period and Orbital Radius – Understanding Kepler’s Third Law**

---

## 🚀 **Motivation**

The relationship between the **orbital period (T)** and the **orbital radius (r)** is a cornerstone of celestial mechanics, known as **Kepler’s Third Law**. This law states that the square of the orbital period of a planet is proportional to the cube of the semi-major axis of its orbit (for circular orbits, this is the orbital radius). Symbolically:

$$
T^2 \propto r^3
$$

This relationship connects fundamental laws of motion and gravitation to real-world orbital systems. It enables:

* Estimating planetary distances from their periods
* Calculating masses of central celestial bodies
* Modeling satellite trajectories and planetary system dynamics

Understanding this law not only explains motions in our solar system but also provides insight into **exoplanet detection**, **satellite deployment**, and **astrophysical modeling** across scales—from moons to galaxies.

---

## 📘 **Theoretical Foundation and Derivation**

We derive Kepler’s Third Law for **circular orbits** using Newton’s law of gravitation and centripetal force.

### 1. **Gravitational Force**

A body of mass $m$ orbits a much larger body of mass $M$ (e.g., planet around a star), and the gravitational attraction provides the required centripetal force to keep the smaller body in circular motion:

$$
F_{\text{gravity}} = \frac{G M m}{r^2}
$$

$$
F_{\text{centripetal}} = \frac{m v^2}{r}
$$

Equating both:

$$
\frac{G M m}{r^2} = \frac{m v^2}{r}
$$

Simplifying:

$$
v^2 = \frac{G M}{r}
$$

---

### 2. **Orbital Period $T$**

The orbital speed $v$ is the distance traveled in one orbit divided by time:

$$
v = \frac{2\pi r}{T}
$$

Substitute into the earlier equation:

$$
\left(\frac{2\pi r}{T}\right)^2 = \frac{G M}{r}
$$

$$
\frac{4\pi^2 r^2}{T^2} = \frac{G M}{r}
$$

Multiply both sides by $r$ and solve for $T^2$:

$$
\frac{4\pi^2 r^3}{T^2} = G M
$$

$$
\boxed{T^2 = \frac{4\pi^2}{G M} r^3}
$$

---

### ✅ **Interpretation:**

* The square of the orbital period is **proportional to the cube of the radius**:

  $$
  T^2 \propto r^3
  $$
* The constant of proportionality depends on the mass of the central body.

This is **Kepler’s Third Law**, refined by Newton.

---

## 🌌 **Implications in Astronomy and Physics**

1. **Determining Planetary Masses**
   Rearranging the formula:

   $$
   M = \frac{4\pi^2 r^3}{G T^2}
   $$

   If you can observe $r$ and $T$ of a satellite or moon, you can calculate the mass $M$ of the planet or star.

2. **Calculating Orbital Distances**
   For planetary systems, astronomers measure $T$, then infer $r$ based on this relationship.

3. **Exoplanet Studies**
   Kepler’s Law is used to detect and characterize planets orbiting distant stars by observing changes in star brightness and using the orbital period to estimate the planet's orbit.

---

## 🌍 **Real-World Examples**

* **Moon Around Earth**:
  $T \approx 27.3$ days, $r \approx 384,400$ km
  Plug into the formula to estimate Earth's mass.

* **Planets Around the Sun**:
  Kepler originally formulated his law by observing Mars, Jupiter, etc. The orbits match the $T^2 \propto r^3$ rule closely.

* **Artificial Satellites**:
  Used to place satellites in geostationary orbits (e.g., at 42,164 km from Earth center for 24-hour period).

---

## 🛠️ **Computational Modeling (Conceptual Steps)**

To simulate this numerically and verify the relationship:

1. **Define Constants**:

   * $G$ (gravitational constant)
   * $M$ (mass of the central body)

2. **Generate Orbital Radii**:

   * Use a set of $r$ values (e.g., 5 values from Earth radius to Mars)

3. **Compute Periods**:

   * Use $T = 2\pi \sqrt{r^3 / (GM)}$

4. **Visualize**:

   * Plot $T^2$ vs. $r^3$: the result should be a **straight line** showing proportionality

5. **Compare with Real Data**:

   * Use planetary data from the solar system to validate the theoretical result

---

## 📊 **Graphical Representations**

* **$T^2$ vs. $r^3$**: Linear relationship (straight line)

* **Log-Log Plot**: $\log T$ vs. $\log r$ yields a slope of 1.5, since:

  $$
  \log T = \frac{3}{2} \log r + \text{const}
  $$

* **Residuals or deviations** can reveal non-circular orbits or perturbations

---

## 📦 **Deliverables (Explanation)**

1. **Markdown or Jupyter Notebook** with theory, plots, and simulations
2. **Detailed derivation and conceptual background**
3. **Graphs** of simulated and real orbital systems
4. **Extension to elliptical orbits**:

   * Kepler’s law holds for **elliptical orbits** when $r$ is interpreted as the **semi-major axis (a)**:

     $$
     T^2 \propto a^3
     $$

---

## 🧩 **Extensions and Insights**

* **Satellite Engineering**: Helps determine orbital heights for GPS or ISS
* **Astrophysics**: Used to estimate black hole or galactic masses
* **Gravitational Interactions**: Lays the foundation for more advanced orbital mechanics (e.g., perturbations, multi-body problems)

---

