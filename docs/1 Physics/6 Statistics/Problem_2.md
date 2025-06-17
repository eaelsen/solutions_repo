# Problem 2
---

# 🎯 **Estimating π Using Monte Carlo Methods**

*A blend of geometry, probability, and simulation to approximate a mathematical constant.*

---

## 🌟 **Motivation**

π (pi) is one of the most fundamental constants in mathematics and physics. While it is often introduced through geometry (as the ratio of a circle's circumference to its diameter), π can also be **estimated probabilistically** using **Monte Carlo methods**.

These approaches allow students to:

* Apply **random sampling** and **statistical reasoning**.
* Connect abstract mathematics with **geometric intuition**.
* Learn about **convergence, variance, and computational accuracy**.

Two famous Monte Carlo methods to estimate π are:

1. **The Dartboard (Circle-in-Square) Method**
2. **Buffon's Needle Experiment**

Both methods rely on randomness and geometric probability but approach the estimation in different ways.

---

## 🧮 Part 1: Circle in a Square Method

### 🧠 1. Theoretical Foundation

A circle of radius $r = 1$ can be inscribed inside a square of side 2. The area of the:

* Circle = $\pi r^2 = \pi$
* Square = $(2r)^2 = 4$

So the ratio of the **circle’s area to the square’s area** is:

$$
\frac{\text{Area of circle}}{\text{Area of square}} = \frac{\pi}{4}
$$

If we generate points randomly inside the square, the fraction of points that fall inside the circle should approximate $\pi / 4$, thus:

$$
\boxed{\pi \approx 4 \cdot \frac{\text{Points inside the circle}}{\text{Total points}}}
$$

---

### 🧪 2. Simulation

* Generate $N$ random points $(x, y)$ in the square $[-1, 1] \times [-1, 1]$.
* Use the condition $x^2 + y^2 \leq 1$ to determine if the point is **inside** the circle.
* Estimate π using the formula above.

---

### 📊 3. Visualization

* Plot all the sampled points.
* Color **inside points** differently from **outside points**.
* Show the circle boundary for visual reference.
* Add a dynamic tracker for π estimate vs. number of points.

---

### 🔍 4. Analysis

* Observe how the estimate **converges** to π as the number of samples increases.
* Study the **variance** and **convergence rate**:

  * Larger samples reduce error.
  * Estimator variance is proportional to $\frac{1}{n}$.

---

## 📏 Part 2: Buffon’s Needle Method

### 🧠 1. Theoretical Foundation

Buffon’s Needle problem involves dropping a needle of length $L$ onto a floor marked with **parallel lines** separated by a distance $d$. The probability that the needle crosses a line is related to π.

If $L \leq d$, the probability $P$ of crossing is:

$$
\boxed{P = \frac{2L}{\pi d}}
\quad \Rightarrow \quad
\boxed{\pi \approx \frac{2L \cdot N}{d \cdot C}}
$$

Where:

* $N$: total number of needle drops
* $C$: number of crossings

---

### 🧪 2. Simulation

* Simulate randomly oriented and positioned needles.
* For each needle:

  * Drop with random center position $x \in [0, d/2]$
  * Pick a random angle $\theta \in [0, \pi/2]$
  * Determine if the needle crosses a line:

    $$
    \text{Crosses if } x \leq \frac{L}{2} \sin(\theta)
    $$
* Use the empirical ratio of crossings to estimate π.

---

### 📊 3. Visualization

* Plot the needle positions, with:

  * **Crossing needles** in one color
  * **Non-crossing needles** in another
* Display the π estimate on the figure.
* Optionally animate the dropping process.

---

### 🔍 4. Analysis

* Buffon’s method tends to **converge slower** than the circle method.
* It is more **sensitive to randomness** and needs **more trials** for accurate estimation.
* Nonetheless, it’s a powerful demonstration of geometric probability and randomness.

---

## 📦 Deliverables Summary

| Component                  | Description                                         |
| -------------------------- | --------------------------------------------------- |
| ✅ **Markdown/Report**      | Theory, assumptions, formulas, methodology          |
| ✅ **Simulation Code**      | One script for each method                          |
| ✅ **Visualizations**       | Point scatter (circle method), needle plot (Buffon) |
| ✅ **Comparative Analysis** | Accuracy, convergence speed, computational time     |
| ✅ **Discussion**           | Strengths and limitations of each method            |

---

## ⚙️ Advanced Extensions (Optional)

* Compare convergence rates using graphs (π vs. iterations).
* Include **confidence intervals** on estimates.
* Optimize performance with **vectorized operations** (NumPy).
* Compare with **true π** using relative error:

  $$
  \text{Error} = \left|\frac{\hat{\pi} - \pi}{\pi}\right|
  $$

---

## 📚 Educational Impact

This project fosters understanding in:

* **Random sampling**
* **Probability and geometry**
* **Estimation and convergence**
* **Visualization and error analysis**

It also develops computational skills while illustrating how randomness can help solve deterministic problems.

---
