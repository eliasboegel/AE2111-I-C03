
def read_excel(): #Working on this one -Saviër


# For this function, I would like the forces F_x and F_z to have coordinates that I can use
# CG should be coordinates as (x, z)
def calculate_equivalent_FM(forces_and_moments_dictionary, CG_coordinates): # Working on this one -Kristian
    #The forces in the x- and z-directions will just be the forces
    return { "F_cgx": forces_and_moments_dictionary["F_x"], "F_cgz": forces_and_moments_dictionary["F_z"], "M_cgy": forces_and_moments_dictionary["F_x"] * (forces_and_moments_dictionary["coord_z"] - CG_coordinates(1))  - forces_and_moments_dictionary["F_z"] * (forces_and_moments_dictionary["coord_x"] - CG_coordinates(0))}


def in_plane_force(forces_and_moments_dictionary, fastener_list): # Working on this one -Kristian
    