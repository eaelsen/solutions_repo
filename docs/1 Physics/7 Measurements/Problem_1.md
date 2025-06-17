# Problem 1


---

# 🌍 **Measuring Earth’s Gravitational Acceleration with a Pendulum**

---

## 🎯 **Motivation**

The acceleration due to gravity, $g$, is a **fundamental physical constant** with a standard value near Earth's surface of approximately:

$$
g \approx 9.81\ \text{m/s}^2
$$

Accurately measuring $g$ is crucial for:

* Understanding Newtonian mechanics
* Engineering and structural analysis
* Calibration of physical instruments
* Precision experiments in physics labs

This experiment uses a **simple pendulum**, a classical system where the period of oscillation depends only on the **length of the pendulum** and **gravitational acceleration**.

By measuring the time it takes for a pendulum to oscillate, we can experimentally determine the local value of $g$, while also learning how to analyze **uncertainty** and **experimental error**.

---

## 🧪 **Task Summary**

1. **Measure the period** of a simple pendulum.
2. **Calculate gravitational acceleration** using:

   $$
   g = \frac{4\pi^2 L}{T^2}
   $$
3. **Evaluate experimental uncertainty**, including how measurement tools and procedures affect your result.

---

## 🧰 Materials Needed

| Item                           | Purpose                 |
| ------------------------------ | ----------------------- |
| String (1–1.5 m)               | Pendulum length         |
| Small mass (key, washer, coin) | Weight for pendulum bob |
| Stopwatch or smartphone        | Timing 10 oscillations  |
| Ruler or tape measure          | To measure length $L$   |
| Clamp or support               | To suspend the pendulum |

---

## 🛠️ Setup Procedure

1. **Build the pendulum**:

   * Tie the mass securely to the string.
   * Fix the other end of the string to a rigid point (door frame, ring stand, etc.).

2. **Measure the length**:

   * Use a ruler/tape to measure from the **pivot point to the center of the mass**.
   * Record the uncertainty:

     $$
     \Delta L = \frac{\text{ruler resolution}}{2}
     $$

3. **Record timing data**:

   * Pull the pendulum back < 15° (small-angle approximation applies).
   * Start timing when the pendulum passes the vertical.
   * Time **10 full oscillations**.
   * Repeat this 10 times for reliability.

---

## 📊 Data Collection Table Example

| Trial | Time for 10 Oscillations ($T_{10}$) \[s] |
| ----- | ---------------------------------------- |
| 1     | 20.12                                    |
| 2     | 20.08                                    |
| ...   | ...                                      |
| 10    | 20.11                                    |

Then compute:

* Mean time for 10 oscillations: $\bar{T}_{10}$
* Period: $T = \bar{T}_{10} / 10$
* Standard deviation: $\sigma_T$
* Uncertainty in the mean:

  $$
  \Delta T = \frac{\sigma_T}{\sqrt{n}} \quad (n = 10)
  $$

---

## 🔬 Calculations

### 1. **Compute the Period**

$$
T = \frac{\bar{T}_{10}}{10}
$$

### 2. **Calculate g**

Using the simple pendulum formula:

$$
g = \frac{4\pi^2 L}{T^2}
$$

Make sure to use consistent units (length in meters, time in seconds).

---

### 3. **Uncertainty Propagation**

To account for uncertainty in both $L$ and $T$, apply:

$$
\Delta g = g \cdot \sqrt{\left(\frac{\Delta L}{L}\right)^2 + \left(2\frac{\Delta T}{T}\right)^2}
$$

---

## 📈 Analysis

### ✅ Compare Measured vs. Standard

* Standard value: $g = 9.81\ \text{m/s}^2$
* Your result: e.g., $g = 9.76 \pm 0.05\ \text{m/s}^2$
* Is the true value within your error bounds?

### ✅ Discuss Uncertainties

* **Length measurement resolution**: smallest unit you can read on the ruler.
* **Timing variability**: human reaction time or stopwatch resolution.
* **Air resistance and friction**: small but present.
* **Small-angle approximation**: only valid if initial displacement < 15°.

---

## 📦 Deliverables

1. **Markdown / Lab Report** including:

   * Raw data
   * Mean values and standard deviation
   * Calculations of $T$, $g$, and $\Delta g$

2. **Discussion** of:

   * Experimental sources of error
   * Improvements for better accuracy
   * Comparison with expected theoretical value

---
