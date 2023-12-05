import numpy as np
from matplotlib import pyplot as plt

# Polynomial model
polymod = np.poly1d([-1.58311283e-62,  3.86411858e-57, -4.27340475e-52,  2.83112517e-47,
       -1.25159917e-42,  3.89253884e-38, -8.74741936e-34,  1.43609685e-29,
       -1.72113139e-25,  1.48844658e-21, -9.06885780e-18,  3.73596281e-14,
       -9.69265826e-11,  1.38268929e-07, -8.27539559e-05, -2.52587008e-02,
        2.28524710e+03])

ean = 1
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
