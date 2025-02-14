import math
pi = math.pi
from dimensions import *

""" Thermal intensity values """

#Earth
J_searth = 1371.3
J_aearth = 307.4
J_irearth  = 239.7

#Jupiter
J_sjupiter = 52.7
J_ajupiter = 21.1
J_irjupiter = 8.2


""" absorptivity and emissivity values dependent on material """
alpha = 0.15 #absorptivity
epsilon = 0.05 #emmisvity
sigma = 5.67*10**(-8)


""" emitting and projected area of lug """
#calculations of the area
A_front = 2 * (w * t1) + 3* (h * w) - 4 * pi * (0.5*D2)**2

A_sunlitside = t2 * w + L * w + 0.5 * pi * (0.5*w)**2 - pi * (0.5*D1)**2

A_top = h * t2 * 3 + (L + 0.5 * w) * t1

A_inside = L*w+0.5*pi*(0.5*w)**2 - pi*(0.5*D1)**2

A_back = w * (3*h+2*t1)

A_total = A_sunlitside*2 + A_top *2 + A_inside * 2 + A_back + A_front


A_i = A_sunlitside  #projected area
A_e = A_total  #emitting area


"""" Calculations of Q_absorbed """

#Q_absorbed = alpha * J_s * A_i + alpha * J_a * A_i + epsilon * J_ir * A_i

#for earth
Q_absorbed_earth = alpha * J_searth * A_i + alpha * J_aearth * A_i + epsilon * J_irearth * A_i

#for Jupiter
Q_absorbed_jupiter = alpha*J_sjupiter*A_i + alpha*J_ajupiter*A_i + epsilon*J_irjupiter*A_i

if Q_absorbed_earth > Q_absorbed_jupiter:
    Q_absorbed_max = Q_absorbed_earth
    Q_absorbed_min = Q_absorbed_jupiter

elif Q_absorbed_earth < Q_absorbed_jupiter:
    Q_absorbed_max = Q_absorbed_jupiter
    Q_absorbed_min = Q_absorbed_earth

""" Calculations for min and max equilibrium temperature"""
#T = (Q_absorbed/(epsilon*sigma*A_e))^(1/4)
#min equilibrium temperature
T_eqmin = (Q_absorbed_min/(epsilon*sigma*A_e))**(1/4)
#max equilibrium temperature
T_eqmax = (Q_absorbed_max/ (epsilon*sigma*A_e))**(1/4)

print(T_eqmin, "[K]" , T_eqmax, "[K]")

