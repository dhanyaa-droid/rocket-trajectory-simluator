# rocket-trajectory-simluator
Physics based rocket trajectory simulator in Python with drag, variable mass, and ASCII visualization.
# 🚀 Rocket Trajectory Simulator

A physics-based rocket trajectory simulator built in Python that models the motion of a rocket considering thrust, gravity, air drag, and changing mass during fuel burn.

---

## 📌 Features

- 2D trajectory simulation (Distance vs Height)
- Includes real-world physics:
  - Thrust force
  - Gravity
  - Air resistance (drag)
  - Variable mass (fuel consumption)
- Color-coded trajectory:
  - 🔴 Thrust phase (engine ON)
  - 🔵 Coasting phase (engine OFF)
  - 🟡 High velocity regions
- ASCII-based graph with:
  - X and Y axes
  - Scale markings
  - Side legend

---

## 🧠 Physics Model

The simulation is based on Newton’s Second Law:

F = ma

Forces considered:
- Thrust (T)
- Gravity (mg)
- Drag force:
  
  D = 0.5 × ρ × Cd × A × v²

Mass variation:
  
  m(t) = m₀ - ṁt

---

## ⚙️ How to Run

1. Make sure Python is installed
2. Clone this repository or download the file
3. Run:

```bash
Initial mass
Final mass
Thrust
Launch angle
Burn time
🧪 Sample Input
Initial mass: 50
Final mass: 20
Thrust: 1000
Angle: 60
Burn time: 5
Output
Maximum height reached
Horizontal range
ASCII trajectory graph with axis scaling and color legend
 Purpose
This project demonstrates:

Application of physics in programming
Basic aerospace trajectory modeling
Visualization without external plotting libraries

python rocket_simulator.py
