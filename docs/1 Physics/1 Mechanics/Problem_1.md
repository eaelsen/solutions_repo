# Problem 1




---

## 🧠 Theoretical Foundation

We analyze projectile motion in two dimensions (2D), assuming:

* No air resistance
* Launch from ground level (initial height = 0)

Let:

* $v_0$ be the initial velocity
* $\theta$ be the angle of projection with respect to the horizontal
* $g$ be the gravitational acceleration ($\approx 9.8 \, \text{m/s}^2$)

---

### 1. **Equations of Motion**

#### Horizontal motion:

* Constant velocity:

  $$
  x(t) = v_0 \cos(\theta) \cdot t
  $$

#### Vertical motion (accelerated under gravity):

* Displacement:

  $$
  y(t) = v_0 \sin(\theta) \cdot t - \frac{1}{2}gt^2
  $$

---

### 2. **Time of Flight (T)**

Set $y(t) = 0$ to find when the projectile hits the ground:

$$
0 = v_0 \sin(\theta) \cdot T - \frac{1}{2}gT^2
$$

Solving:

$$
T = \frac{2v_0 \sin(\theta)}{g}
$$

---

### 3. **Horizontal Range (R)**

Range is total horizontal distance when projectile lands (at $t = T$):

$$
R = v_0 \cos(\theta) \cdot T
$$

Substitute $T$ from above:

$$
R = v_0 \cos(\theta) \cdot \frac{2v_0 \sin(\theta)}{g}
$$

$$
\boxed{R = \frac{v_0^2 \sin(2\theta)}{g}}
$$

✅ This is the most important formula. It shows:

* Range depends on $\sin(2\theta)$, peaking at $\theta = 45^\circ$
* Range increases with square of $v_0$
* Inversely proportional to gravity

---

## 🔍 Additional Analyses

### How Gravity Affects Range:

* On Earth: $g \approx 9.8 \, \text{m/s}^2$
* On Moon (1/6th of Earth): Range increases significantly due to smaller $g$

### Effect of Uneven Terrain or Initial Height:

If projectile is launched from height $h$, time of flight and range change:

$$
y(t) = h + v_0 \sin(\theta) \cdot t - \frac{1}{2}gt^2
$$

Solve for $t$ when $y(t) = 0$ (quadratic equation), then plug into:

$$
R = v_0 \cos(\theta) \cdot t
$$

---

## 🧩 Practical Application Reflections

* Sports: Choosing best angle to kick a football
* Engineering: Launch angles for projectiles or water streams
* Space: Adjusting launch parameters to account for different gravities

---





