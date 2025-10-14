"""Skript, um Alter und BMI einer Person auszurechnen."""

aktuelles_jahr = 2025

name = "Max Mustermann"
geburtsjahr = 2010
groesse_cm = 180
masse = 72.3  # kg

alter = aktuelles_jahr - geburtsjahr
groesse = groesse_cm / 100
body_mass_index = masse / groesse ** 2
ist_volljaehrig = alter >= 18
hat_normalgewicht = 18.5 <= body_mass_index <= 24.9

print(f"""{name} ist
- {alter} Jahr(e) alt
- wiegt {masse} kg
- hat einen BMI von {body_mass_index:.1f}
- ist er volljährig? {ist_volljaehrig}
- hat Normalgewicht? {hat_normalgewicht}
""")