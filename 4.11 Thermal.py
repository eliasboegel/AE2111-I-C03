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
A_side = t2 * w + w * (l-0.5*D1) + (pi*(0.5*w)**2)-(pi*(D1*0.5)**2)

A_neg_solararray = 2 * (w * t1) + (h*w)*3 - 4*pi*(0.5*D2)**2 #done

A_top_bottom = ((3*(h*t2)+2*t1*t2)+l*t1*2)*2


A_total = 2*A_side + A_neg_solararray + A_top_bottom


A_i = A_side  #projected area
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




temperatures = {"reference": 288.15, "min": T_eqmin, "max": T_eqmax} 

info_fastener = {"E": 2, "diameter": 0.01, "alpha": 0.05} # Also placeholders

alpha_clamped_part = 0.08 # Another placeholder...

phi = 0 # And another one

F_T_max = (alpha_clamped_part - info_fastener["alpha"]) * (temperatures["max"] - temperatures["reference"]) * info_fastener["E"] * info_fastener["diameter"] ** 2 / 4 * (1 - phi)
F_T_min = (alpha_clamped_part - info_fastener["alpha"]) * (temperatures["min"] - temperatures["reference"]) * info_fastener["E"] * info_fastener["diameter"] ** 2 / 4 * (1 - phi)

print("F_T_max:", F_T_max, "\nF_T_min:", F_T_min)