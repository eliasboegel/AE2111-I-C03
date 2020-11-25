import math
pi = math.pi
from dimensions import *


A_front = 2 * (w * t1) + 3* (h * w) - 4 * pi * (0.5*D2)**2

A_sunlitside = t2 * w + l * w + 0.5 * pi * (0.5*w)**2 - pi * (0.5*D1)**2

A_top = h * t2 * 3 + (l + 0.5 * w) * t1

A_inside = l*w+0.5*pi*(0.5*w)**2 - pi*(0.5*D1)**2

A_back = w * (3*h+2*t1)

A_total = A_sunlitside*2 + A_top *2 + A_inside * 2 + A_back + A_front




