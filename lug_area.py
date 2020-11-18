import math
pi = math.pi
from dimensions import *




A_side = t2 * w + w * (l-0.5*D1) + (pi*(0.5*w)**2)-(pi*(D1*0.5)**2)

A_neg_solararray = 2 * (w * t1) + (h*w)*3 - 4*pi*(0.5*D2)**2 #done

A_top_bottom = ((3*(h*t2)+2*t1*t2)+l*t1*2)*2


A_total = 2*A_side + A_neg_solararray + A_top_bottom


