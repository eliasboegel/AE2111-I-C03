import constants as const
import dimensions as dim

import numpy as np

# Launch accelerations in g: x, y, z
launch_acc = np.array([2, 2, 6])

# Resultant forces of panel on lugs
def totForces():
    F = np.zeros(3)

    # Static loads on ground
    F += np.array([
        0,
        0,
        - const.g * const.m_sarray
    ])

    # Dynamic launch loads
    F -= launch_acc * const.g * const.m_sarray

    return F

# Resultant moments of panel on lugs
def totMoments():
    M = np.zeros(3)
    
    # unfinished

    return M


def totForcesLugUpper():
    # Each lug carries half the applied forces
    F = totForces() / 2

    # Total moments are balanced by additional forces at lugs
    M = totMoments()

    # Add force components based on applied moments, as well as distance between lugs
    F += np.array([
        M[1] / dim.d / 2, 
        - M[0] / dim.d / 2,
        0
        ])

    return F

def totMomentsLugUpper():
    Mtot = totMoments()

    F_lugU = totForcesLugUpper()
    r_lugU = np.array([0, dim.l, 0])

    M = np.array([0, 0, Mtot[2] / 2])

    M += np.cross(r_lugU, F_lugU)

    return M

def totForcesLugLower():
    # Each lug carries half the applied forces
    F = totForces() / 2

    # Total moments are balanced by additional forces at lugs
    M = totMoments()

    # Add force components based on applied moments, as well as distance between lugs
    F += np.array([
        - M[1] / dim.d / 2, 
        M[0] / dim.d / 2,
        0
        ])

    return F

def totMomentsLugLower():
    Mtot = totMoments()

    F_lugL = totForcesLugLower()
    r_lugL = np.array([0, dim.l, 0])

    # For moments around Z applied at the end of the adapter, this cannot be split up into a force couple for the two lugs
    # This means that both lugs need to provide for half of the applied Z moment at the end of the adapter
    M = np.array([0, 0, Mtot[2] / 2])

    M += np.cross(r_lugL, F_lugL)

    return M