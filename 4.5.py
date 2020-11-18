
def read_excel(excel): #Working on this one -Saviër

    # Read csv file for coordinates
    df = pd.read_csv(excel, delimiter=',')

    # Convert to seperate lists for X, Z, D
    lists = [[row[col] for col in df.columns] for row in df.to_dict('records')]
    



# For this function, I would like the forces F_x and F_z to have coordinates that I can use
# CG should be coordinates as (x, z)
def calculate_equivalent_FM(forces_and_moments_dictionary, CG_coordinates): # Working on this one -Kristian
    #The forces in the x- and z-directions will just be the forces
    return { "F_cgx": forces_and_moments_dictionary["F_x"], "F_cgz": forces_and_moments_dictionary["F_z"], "M_cgy": forces_and_moments_dictionary["F_x"] * (forces_and_moments_dictionary["coord_z"] - CG_coordinates(1))  - forces_and_moments_dictionary["F_z"] * (forces_and_moments_dictionary["coord_x"] - CG_coordinates(0))}


def in_plane_force(cg_forces_and_moments_dictionary, fastener_details_dictionary, number_of_fasteners): # Working on this one -Kristian
    return { "F_in_plane_x": cg_forces_and_moments_dictionary["F_x"] / number_of_fasteners, "F_in_plane_z": cg_forces_and_moments_dictionary["F_z"] / number_of_fasteners}


def in_plane_moment():# Working on this one -Kristian