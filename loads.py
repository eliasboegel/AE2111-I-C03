import constants as const
import dimensions as dim

import numpy as np

def totForces():
    F = np.zeros(3)

    # Static on ground
    F += np.array([
        0,
        0,
        - const.g * const.m_sarray
    ])

    # Dynamic launch loads
    F += no.array([
        2 * const.g * const.m_sarray,
        2 * const.g * const.m_sarray,
        - 6 * const.g * const.m_sarray
    ])

    return F

def totMoments():
    M = np.zeros
    
    

    



    return M