import numpy as np
from matplotlib import pyplot as plt

# Voltage divider #1

R1 = 100 # ohms unless otherwise stated
R2 = 20E3
C1 = 680E-12 # farads

# Voltage divider #2

R3 = 47E3 # ohms unless otherwise stated
C2 = 0.22E-6 # farads

# Voltage divider #3

R4 = 200 # ohms unless otherwise stated
R5 = 2E3
C3 = 1E-9 # farads

measured_params = (R1, R2, R3, R4, R5, C1, C2, C3)

j = 0 + 1j

def gain50(frequency, R1, R2, R3, R4, R5, C1, C2, C3):
    omega = 2 * np.pi * frequency
    amp1 = ((1 / (1 / R2 + (j * omega * C1))) + R1) / R1
    amp2 = ((j * omega * C2) + R3) / R3
    amp3 = ((1 / (1 / R5 + (j * omega * C3))) + R4) / R4
    return np.abs(((amp1 * amp3) / amp2))
