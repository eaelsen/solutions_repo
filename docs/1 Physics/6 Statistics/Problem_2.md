# Problem 2
\

---

## 🧮 Project: Estimating π Using Monte Carlo Methods

### 🎯 Motivation

Monte Carlo simulations provide a visual and statistical approach to estimate π using:

* **Circle-based random point sampling**
* **Buffon’s Needle probability experiment**

These methods not only estimate π but also teach key concepts in randomness, convergence, and computational modeling.

---

## 🧪 Part 1: Estimating π Using a Circle

### Theoretical Basis:

$$
\pi \approx 4 \cdot \frac{\text{points inside the circle}}{\text{total points}}
$$

### Simulation Steps:

1. Generate random $(x, y)$ points in a unit square
2. Check whether they fall inside the unit circle: $x^2 + y^2 \leq 1$
3. Estimate π and visualize the point distribution

---

## 📏 Part 2: Estimating π Using Buffon's Needle

### Theoretical Basis:

$$
\pi \approx \frac{2L \cdot N}{d \cdot C}
$$

Where:

* $L$ = needle length
* $d$ = distance between parallel lines
* $N$ = number of drops
* $C$ = number of crossings

### Simulation Steps:

1. Randomly generate needle positions and angles
2. Check if the needle crosses a line
3. Estimate π and visualize the needles relative to the lines

---

## 📈 Deliverables

* **Markdown/Jupyter Notebook**:

  * Derivations and explanations
  * Python simulations for both methods
* **Visualizations**:

  * Circle hits/misses
  * Needle positions and crossings
* **Analysis**:

  * Compare convergence speed and accuracy
  * Discuss trade-offs and computational cost

---


### 🟢 Circle-Based Estimation

* Points are randomly distributed inside a unit square.
* Points inside the quarter circle are shown in green, outside in red.
* **Estimated value of π ≈ 3.14880** (very close to the actual value!).

---

### 📏 Buffon's Needle Estimation

* Needles are randomly dropped on a plane with parallel lines.
* Green needles cross a line, red needles do not.
* **Estimated value of π ≈ 3.15060**, also close but typically more variable unless many samples are used.

---

### 📌 Summary Comparison

| Method          | Trials | Estimated π | Notes                              |
| --------------- | ------ | ----------- | ---------------------------------- |
| Circle Sampling | 10,000 | 3.14880     | Simple, intuitive, consistent      |
| Buffon’s Needle | 10,000 | 3.15060     | More variable, depends on geometry |

---


