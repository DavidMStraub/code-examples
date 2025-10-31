"""Skript, das die Geschwindigkeit eines UAV anpasst."""

v0 = 10  # m/s
v_target = 20  # m/s
epsilon = 0.5  # m/s
max_steps = 20
k = 0.2

v = v0
step = 0
while abs(v - v_target) >= epsilon and step < max_steps:
    print(f"Schritt {step}: aktuelle Geschwindigkeit {v:.2f} m/s")
    step += 1
    v += k * (v_target - v)

print(f"Endgeschwindigkeit: {v:.2f} m/s")
