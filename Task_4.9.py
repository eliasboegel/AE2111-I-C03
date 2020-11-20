from math import pi

#calculating the normal stress
D_fo = 4
D_fi = 2
r_fo = D_fo / 2
r_fi = D_fi / 2

F_y = 4 # pull-through load

A = pi * ( r_fo**2 - r_fi**2 )

stress_N = F_y / A

print(stress_N)

#calculating shaer stress

t = 2
A_ap = pi * t * D_fi #area of the attached parts
stress_V = F_y / A_ap

print(stress_V)
