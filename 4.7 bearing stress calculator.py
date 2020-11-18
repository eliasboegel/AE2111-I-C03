import numpy as np
"""Bearing stress calculator"""

""" Constants and inputs"""
D2 = 2
t2 = 1
F_inplane_x = 20
F_inplane_z = 10
F_inplane_my = 10
stress_allowable = 20

""" Vectorize the forces [x,y,z]"""
F_inx = np.array([F_inplane_x , 0, 0])
F_inmy = np.array([0, F_inplane_my, 0])
F_inz = np.array([0, 0, F_inplane_z])


""" Calculate Pi"""
Pi = F_inx + F_inz + F_inmy
print(Pi)

Pix = Pi[0]
Piy = Pi[1]
Piz = Pi[2]
print(Pix, Piy, Piz)
#find magnitude of Pi and the bearing stress
Pi = (Pix**2+Piy**2+Piz**2)**(1/2)
B_stress = Pi/(D2*t2)


print("The bearing stress is:", B_stress)
print("The max allowable stress is:", stress_allowable)
print(" ")
 #Check if bearing stress does not exceed allowable stress
if B_stress < stress_allowable:
    print("No failure due to bearing stress")
    print("Try to save weight by reducing t2 or removing fasteners")

elif B_stress == stress_allowable:
    print("Bearing stress is equal to allowable stress")

elif B_stress > stress_allowable:
    print("Failure occurs due to bearing stress please change one of the following geometries:")
    print("D2")
    print("t2")
    print("number of fasteners, note w might change due to this")

else:
    print("Failed to compute")


