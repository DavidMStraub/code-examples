import math

# constants
HOUR = 3600  # hour in seconds
CM = 0.01  # cm in m
kappa = 0.5
air_density = 1.2  # kg/m³
grav_accel = 9.81  # m/s²
voltage = 11.1  # V
capacity = 3 * HOUR  # in As = C

# input
mass_kg = float(input("Geben Sie die Masse der Drohne in kg an:"))
num_rotors = int(input("Geben Sie die Anzahl der Rotoran an:"))
diameter_rotor_cm = float(input("Geben Sie den Durchmesser eines Rotors in cm an:"))

radius_rotor = diameter_rotor_cm * CM / 2  # m
rotor_area = num_rotors * math.pi * radius_rotor**2
thrust = mass_kg * grav_accel
hover_power = kappa * thrust**(3/2) / math.sqrt(2 * air_density * rotor_area)

current = hover_power / voltage

print(f"The dronw will draw {current:.2f} A in hover")

hover_duration = capacity / current  # seconds

print(f"The drone will be able to hover for {hover_duration:.1f} seconds.")
