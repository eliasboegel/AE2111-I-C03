
import numpy as np
import math

import constants as const
import loads as ld

import iteration_Latch as aaa
import iteration_Bearing as bbb
import iteration_PullThrough as ccc


# Iteration bounds, all dimensions in m
w1_start = 25e-3
w1_end = 35e-3
w1_step = 5e-3

d1_start = 4e-3
d1_end = 10e-3
d1_step = 1e-3

t1_start = 2e-3
t1_end = 10e-3
t1_step = 4e-3

t2_start = 4e-3
t2_end = 10e-3
t2_step = 1e-3

h_start = 5e-3
h_end = 15e-3
h_step = 5e-3


mats = [
    {"name" : "Al_2014_T6", "alpha" : 23e-6, "rho" : 2800, "sigma_y" : 414e6, "E" : 72.4e9},
    #{"name" : "Al_2024_T3", "alpha" : 23.2e-6, "rho" : 2780, "sigma_y" : 240e6, "E" : 72.4e9},
    #{"name" : "Al_7075_T6", "alpha" : 23.6e-6, "rho" : 2810, "sigma_y" : 503e6, "E" : 71.7e9}
]


results = []
min_dim = {}
min_m = 1000000000000000000000000000000

for lug in range(0, 1):
    for mat in mats:
        for w1 in np.arange(w1_start, w1_end, w1_step):
            for d1 in np.arange(d1_start, d1_end, d1_step):
                for t1 in np.arange(t1_start, t1_end, t1_step):
                    for t2 in np.arange(t2_start, t2_end, t2_step):
                        for h in np.arange(h_start, h_end, h_step):
                            # Dimension set validity check
                            if not (2*d1 < w1):
                                continue

                            


                            unrounded_d2 = w1 / 5

                            fastener_distances = []
                            for fastener_column in range(2):
                                d_x_fastener = 1.5 * unrounded_d2 + t1 + h / 2 + fastener_column * 2 * unrounded_d2
                                fastener_distances.append((d_x_fastener**2 + unrounded_d2**2)**0.5);

                        
                            dim = {
                                    "w1" : w1,
                                    "w2" : 2*w1 + 2*t1 + h,
                                    "d1" : d1,
                                    "d2" : math.floor(unrounded_d2*1000)/1000,
                                    "t1" : t1,
                                    "t2" : t2,
                                    "h" : h,
                                    "L" : 1.5*d1,
                                    "d" : 2.2 - w1
                                }


                            totF_L = ld.totForcesLaunch()
                            totF_O = ld.totForcesOrbit()

                            totM_L = ld.totMomentsLaunch()
                            totM_O = ld.totMomentsOrbit(dim)

                            if lug:
                                # Get loads from first lug
                                F_L  = ld.wallForcesLug1(totF_L, totM_L, dim)
                                M_L  = ld.wallMomentsLug1(totF_L, totM_L, dim)
                                F_O  = ld.wallForcesLug1(totF_O, totM_O, dim)
                                M_O  = ld.wallMomentsLug1(totF_O, totM_O, dim)
                            else:
                                # Get loads from second lug
                                F_L  = ld.wallForcesLug2(totF_L, totM_L, dim)
                                M_L  = ld.wallMomentsLug2(totF_L, totM_L, dim)
                                F_O  = ld.wallForcesLug2(totF_O, totM_O, dim)
                                M_O  = ld.wallMomentsLug2(totF_O, totM_O, dim)

                            loads_L = {"Fx": F_L[0], "Fy": F_L[1], "Fz": F_L[2], "Mx" : M_L[0], "My" : M_L[1], "Mz" : M_L[2]}
                            loads_O = {"Fx": F_O[0], "Fy": F_O[1], "Fz": F_O[2], "Mx" : M_O[0], "My" : M_O[1], "Mz" : M_O[2]}



                            """Example"""
                            ms = []
                            ms.extend(bbb.bearingstress_everything(dim, mat, loads_L))
                            ms.append(aaa.lug_get_MS(dim, mat, loads_L))
                            ms.append(ccc.get_MS(dim, mat, loads_L, fastener_distances))
                            ms.extend(bbb.bearingstress_everything(dim, mat, loads_O))
                            ms.append(aaa.lug_get_MS(dim, mat, loads_O))
                            ms.append(ccc.get_MS(dim, mat, loads_O, fastener_distances))


                            if min(ms) < 0:
                                continue

                            
                            V_backplate = dim["w2"]*dim["w1"]*dim["t2"] - 8 * math.pi * (dim["d2"] / 2)**2 * dim["t2"]
                            V_latch = (dim["L"]-dim["t2"])*dim["w1"]*dim["t1"] + math.pi * (dim["w1"]/2)**2 / 2 - math.pi * (dim["d1"]/2)**2
                            m = mat["rho"] * (V_backplate + 2*V_latch)
                            if not m > 0:
                                continue

                            for val in ms:
                                print(round(val,1), end=' ')
                            print(round(m, 3))

                            if (min_m > m):
                                min_m = m
                                min_dim = dim

                            results.append(dim)


print(min_dim)
print(min_m)
                            

                            
                            