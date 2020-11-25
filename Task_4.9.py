from math import pi

#calculating the normal stress
D_fo = 7 #outer diameter in mm
D_fi = 4 #inner diameter in mm
r_fo = D_fo / 2
r_fi = D_fi / 2

F_y = 4 # pull-through load

A_head_ap = pi * ( r_fo**2 - r_fi**2 ) #area of the fastener head on the attached parts

stress_N = F_y / A_head_ap

print(stress_N)

#calculating shaer stress for t1
t1 = 2
A_t1_ap = pi * t1 * D_fi #area of the attached parts of t1
stress_t1_V = F_y / A_t1_ap

print('shearstress in t1 = ',stress_t1_V)

#calculating shaer stress for t2
t2 = 2
A_t2_ap = pi * t2 * D_fi #area of the attached parts of t2
stress_t2_V = F_y / A_t2_ap

print('shearstress in t2 = ',stress_t2_V)

#calculating shaer stress for t3
t3 = 2
A_t3_ap = pi * t3 * D_fi #area of the attached parts of t3
stress_t3_V = F_y / A_t3_ap

print('shearstress in t3 = ',stress_t3_V)

#total shear stress

stress_V_tot = stress_t1_V + stress_t2_V + stress_t3_V

print('total shearstress = ',stress_V_tot)

