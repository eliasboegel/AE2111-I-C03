import numpy as np
import iteration_Latch as aaa
import iteration_Bearing as bbb
import iteration_PullThrough as ccc
import loads


# Iteration bounds, all dimensions in mm
w1_start = 0
w1_end = 50
w1_step = 1

d1_start = 0
d1_end = 10
d1_step = 1

t1_start = 0
t1_end = 10
t1_step = 1

t2_start = 0
t2_end = 10
t2_step = 1

h_start = 5
h_end = 20
h_step = 1

dim = {
    "w1",
    "w2",
    "d1",
    "d2",
    "t1",
    "t2",
    "h",
    "L"
}

mats = [
    {"name" : "Al_2014_T6", "alpha" : 123, "rho" : 123, "sigma_y" : 123, "E" : 123},
    {"name" : "Al_2024_T3", "alpha" : 123, "rho" : 123, "sigma_y" : 123, "E" : 123},
    {"name" : "Al_7075_T6", "alpha" : 123, "rho" : 123, "sigma_y" : 123, "E" : 123}
]


totF = np.maximum(loads.F_tot_launch, loads.F_tot_launch)
totM = np.maximum(loads.totMomentsLaunch, loads.totMomentsOrbit)

for lug in range(0, 1):
    
    if lug:
        # Get loads from first lug
        F  = loads.wallForcesLug1(totF, totM)
        M  = loads.wallMomentsLug1(totF, totM)
        
    else:
        # Get loads from second lug
        F  = loads.wallForcesLug2(totF, totM)
        M  = loads.wallMomentsLug2(totF, totM)

    loads = {"Fx": F[0], "Fy": F[1], "Fz": F[2], "Mx" : M[0], "My" : M[1], "Mz" : M[2]}

    for mat in mats:
        for w1 in np.arange(w1_start, w1_end, w1_step):
            for d1 in np.arange(d1_start, d1_end, d1_step):
                for t1 in np.arange(t1_start, t1_end, t1_step):
                    for t2 in np.arange(t2_start, t2_end, t2_step):
                        for h in np.arange(h_start, h_end, h_step):
                            dim = {
                                    "w1" : w1,
                                    "w2" : w2,
                                    "d1" : d1,
                                    "d2" : d2,
                                    "t1" : t1,
                                    "t2" : t2,
                                    "h" : h,
                                    "L" : L,
                                    "d" : d
                                }

                            """Example"""
                            ms = []
                            ms.list(aaa.lug_get_MS(dim, mat, loads))
                            # call all the checks from here, using F, M, dim and mat
                            # F is a dictionary, forces at the wall, center of lug, with components Fx, Fy, Fz
                            # M is a dictionary, moments at the wall, center of lug, with components Mx, My, Mz
                            # dim is a dictionary with the above components