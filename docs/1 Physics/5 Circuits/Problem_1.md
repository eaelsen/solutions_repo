# Problem 1



---

### 1. Resistor-Network Graph

The first diagram shows a sample resistor circuit rendered as a **graph**:

* **Nodes A–D** represent junctions.
* **Edges** carry a label giving the resistance value in Ω.
* This layout makes clear which resistors share common nodes, so series/parallel combinations can be detected algorithmically.

*(Use the image as a template: swap in any topology or edge-weights you need for test cases.)*

---

### 2. Flowchart of the Reduction Algorithm

The second image is a **high-level schematic** of an iterative graph-simplification routine:

```
Start with Circuit Graph
        ↓
   Find Series Connections
        ↓
 Replace with Single Resistor
        ↓
  Find Parallel Connections
        ↓
 Replace with Single Resistor
(Loop until one equivalent edge remains)
```

This mirrors the pseudocode you would write:

1. **Detect chains** (two-degree nodes) → merge into a single edge (R = R₁ + R₂ + …).
2. **Detect cycles** of order 2 (parallel edges) → merge into one edge (1/R = Σ 1/Rᵢ).
3. Repeat until the graph collapses to a single edge between the chosen terminals.

---

## How to Use These Schemes

| Purpose           | How the Graphic Helps                                                                                |
| ----------------- | ---------------------------------------------------------------------------------------------------- |
| **Unit testing**  | Try small graphs (triangle, bridge, cube) and compare the algorithm’s output to a hand calculation.  |
| **Documentation** | Embed the flowchart in your report so readers see the decision path at a glance.                     |
| **Teaching/demo** | Walk through the graph on a whiteboard, manually eliminating one series or parallel group at a time. |

Feel free to request more examples (e.g., Wheatstone bridge, cube network) or deeper algorithmic notes!
