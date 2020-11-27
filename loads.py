import constants as const
import dimensions as dim

import numpy as np

# Accelerations: x, y, z
launch_acc = np.array([6, 2, 2]) # in g
engine_fire_acc = np.array([0, 0, -const.t_engine / const.m_sc]) # in m/s^2

# Resultant forces of panel on lugs during launch
def totForcesLaunch():
    F = np.zeros(3)

    # Static forces on ground due to weight, applied directly at pin, added to dynamic launch loads
    F = np.array([0, 0, - const.g * const.m_sa / 2]) - launch_acc * const.g * const.m_sa / 2

    return F * const.safety_factor

# Resultant forces of panel on lugs during launch
def totForcesOrbit():
    F = np.zeros(3)

    # Dynamic main engine firing forces, applied at CG of solar array
    F = engine_fire_acc * const.m_sa / 2
    
    return F * const.safety_factor

# Resultant moments of panel on lugs during launch
def totMomentsLaunch():
    M = np.zeros(3)

    # No moments on pin during launch since panel is held in place by fairing, but forces are still carried pin, but moments are relieved by fairing

    return M * const.safety_factor

# Resultant moments of panel on lugs during orbit
def totMomentsOrbit(dims):
    r_sa_from_pin = np.array([0, dim.sc_panel_cg_from_center - dims["L"] - dim.sc_short_sides / 2, 0]) # Distance of the solar array CG from the pin

    # Dynamic main engine firing moments since array CG has moment arm
    M = np.cross(r_sa_from_pin, engine_fire_acc * const.m_sa / 2)

    return M * const.safety_factor



# Forces that Lug 1 creates on the wall, acts at center of Lug 1
def wallForcesLug1(totForces, totMoments, dims):
    # Each lug carries half the applied forces
    F = totForces / 2

    # Add force components based on applied moments, as well as distance between lugs
    F += np.array([
        totMoments[1] / dims["d"] / 2, 
        - totMoments[0] / dims["d"] / 2,
        0
        ])

    return F

# Moments that Lug 1 creates on the wall
def wallMomentsLug1(totForces, totMoments, dims):
    r_pin_1 = np.array([0, dims["L"], dims["d"]/2]) # Location of the force application point of the lug loads with respect to wall coordinate system


    F_lugU = wallForcesLug1(totForces, totMoments, dims)
    r_lugU = np.array([0, r_pin_1[1], 0])

    M = np.array([0, 0, totMoments[2] / 2])

    M += np.cross(r_lugU, F_lugU)

    return M

# Forces that Lug 2 creates on the wall, acts at center of Lug 2
def wallForcesLug2(totForces, totMoments, dims):
    # Each lug carries half the applied forces
    F = totForces / 2

    # Add force components based on applied moments, as well as distance between lugs
    F += np.array([
        - totMoments[1] / dims["d"] / 2, 
        totMoments[0] / dims["d"] / 2,
        0
        ])

    return F

# Moments that Lug 2 creates on the wall
def wallMomentsLug2(totForces, totMoments, dims):
    F_lugL = wallForcesLug2(totForces, totMoments, dims)

    r_pin_2 = np.array([0, dims["L"], -dims["d"]/2]) # Location of the force application point of the lug loads with respect to wall coordinate system
    r_lugL = np.array([0, dim.r_pin_2[1], 0])

    # For moments around Z applied at the end of the adapter, this cannot be split up into a force couple for the two lugs
    # This means that both lugs need to provide for half of the applied Z moment at the end of the adapter
    M = np.array([0, 0, totMoments[2] / 2])

    M += np.cross(r_lugL, F_lugL)

    return M


"""
# Testing
F_tot_launch = totForcesLaunch()
M_tot_launch = totMomentsLaunch()
F_tot_orbit = totForcesOrbit()
M_tot_orbit = totMomentsOrbit()

print("Total forces and moments for launch situation")
print(F_tot_launch)
print(M_tot_launch)
print()
print("Total forces and moments on lug 1 for launch situation")
print(wallForcesLug1(F_tot_launch, M_tot_launch, 1))
print(wallMomentsLug1(F_tot_launch, M_tot_launch))
print()
print("Total forces and moments on lug 2 for launch situation")
print(wallForcesLug2(F_tot_launch, M_tot_launch, 1))
print(wallMomentsLug2(F_tot_launch, M_tot_launch))
print()
print()
print()
print("Total forces and moments for orbit situation")
print(F_tot_orbit)
print(M_tot_orbit)
print()
print("Total forces and moments on lug 1 for orbit situation")
print(wallForcesLug1(F_tot_orbit, M_tot_orbit, 1))
print(wallMomentsLug1(F_tot_orbit, M_tot_orbit))
print()
print("Total forces and moments on lug 2 for orbit situation")
print(wallForcesLug2(F_tot_orbit, M_tot_orbit, 1))
print(wallMomentsLug2(F_tot_orbit, M_tot_orbit))
"""