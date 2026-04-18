import math

# Colors
RED = "\033[91m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
GREEN = "\033[92m"
RESET = "\033[0m"

print(YELLOW + "Enter Rocket Parameters:" + RESET)

m0 = float(input("Initial mass (kg): "))
mf = float(input("Final mass (kg): "))
thrust = float(input("Thrust (N): "))
angle_deg = float(input("Angle (degrees): "))
burn_time = float(input("Burn time (s): "))

# Constants
g = 9.81
rho = 1.225
Cd = 0.75
A = 0.03

angle = math.radians(angle_deg)
mdot = (m0 - mf) / burn_time

dt = 0.1
t = 0

vx, vy = 0, 0
x, y = 0, 0

points = []
velocities = []

# --- Simulation ---
while y >= 0:
    if t <= burn_time:
        m = m0 - mdot * t
        T = thrust
        phase = "thrust"
    else:
        m = mf
        T = 0
        phase = "coast"

    v = math.sqrt(vx**2 + vy**2)
    velocities.append(v)

    D = 0.5 * rho * Cd * A * v**2

    if v != 0:
        drag_x = D * (vx / v)
        drag_y = D * (vy / v)
    else:
        drag_x, drag_y = 0, 0

    ax = (T * math.cos(angle) - drag_x) / m
    ay = (T * math.sin(angle) - m * g - drag_y) / m

    vx += ax * dt
    vy += ay * dt

    x += vx * dt
    y += vy * dt

    points.append((x, y, phase, v))
    t += dt

# --- Results ---
max_height = max(p[1] for p in points)
max_range = max(p[0] for p in points)
max_velocity = max(velocities)

print(GREEN + "\nResults:" + RESET)
print("Max Height:", round(max_height, 2), "m")
print("Range:", round(max_range, 2), "m")

# --- Graph Setup ---
width = 60
height = 20

grid = [[" " for _ in range(width)] for _ in range(height)]

# Axes
for i in range(height):
    grid[i][0] = WHITE + "|" + RESET

for j in range(width):
    grid[height - 1][j] = WHITE + "-" + RESET

grid[height - 1][0] = WHITE + "+" + RESET

# Plot
for px, py, phase, v in points:
    ix = int(px / max_range * (width - 1))
    iy = int(py / max_height * (height - 1))
    iy = min(height - 1, iy)

    if v > 0.7 * max_velocity:
        color = YELLOW
    elif phase == "thrust":
        color = RED
    else:
        color = BLUE

    if ix > 0 and iy < height - 1:
        grid[height - 1 - iy][ix] = color + "*" + RESET

# Sidebar legend content
legend_lines = [
    "Legend:",
    RED + "* " + RESET + "Thrust",
    BLUE + "* " + RESET + "Coast",
    YELLOW + "* " + RESET + "High speed",
    "",
    "Y: Height (m)",
    "X: Distance (m)"
]

print("\n" + GREEN + "Trajectory:\n" + RESET)

# Print graph + sidebar
for i in range(height):
    if i % 4 == 0:
        y_val = max_height * (height - 1 - i) / (height - 1)
        label = f"{y_val:6.1f}|"
    else:
        label = "      |"

    graph_row = label + "".join(grid[i][1:])

    # Add sidebar text if available
    if i < len(legend_lines):
        print(graph_row + "   " + legend_lines[i])
    else:
        print(graph_row)

# X-axis
print("      +" + "-" * (width - 1))

x_labels = ""
for j in range(0, width, 10):
    x_val = max_range * j / (width - 1)
    x_labels += f"{int(x_val):<10}"

print("       " + x_labels)