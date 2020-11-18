import numpy as np

# Dimensions regarding both lugs
d = 0.1 # m, Distance between both lug pinhole centers

# Dimensions regarding one lug
L = 0.05 # m, Distance of pin center from wall
w = 0.005 # m
h = 0.005 # m
D1 = 0.01 # m
D2 = 0.01 # m
t1 = 0.005 # m
t2 = 0.005 # ms

# X, Y, Z
coord_origin = np.array([0, 0, 0]) # This is centered between both logs on the wall surface
r_pin_1 = np.array([0, L, d/2]) # Location of the force application point of the lug loads with respect to wall coordinate system
r_pin_2 = np.array([0, L, -d/2]) # Location of the force application point of the lug loads with respect to wall coordinate system
r_sa_from_pin = np.array([0, 6 - L - 2.2 / 2, 0]) # Distance of the solar array CG from the pin