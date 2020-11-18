import numpy as np
from math import sin, cos, atan2, pi


TESTING_forces_and_moments_temporary_dictionary = {"F_x": 5, "M_y": 5, "F_z": 5, "coord_z": 0, "coord_x": 0}
TESTING_fasteners_list = [{"coord_x": 0, "coord_z": 0, "diameter": 1}, {"coord_x": 2, "coord_z": 2, "diameter": 2}, {"coord_x": 4, "coord_z": 2, "diameter": 1}, {"coord_x": 5, "coord_z": 4, "diameter": 4}, {"coord_x": 0, "coord_z": 1, "diameter": 6}, {"coord_x": 2, "coord_z": 3, "diameter": 4}]
TESTING_stress_allowable = 20
TESTING_t2 = 2


def CG_calculator(fastener_details_list): # I changed it slightly to take in the data in another form, and into a function
    """Calculate area of each fastener"""
    #get area for each fastener this is now correct
    A_list = []
    for i in fastener_details_list:  #goes through every item in list 
        r_fastener = i["diameter"]/2 #Changed this slightly. You can do this instead of range(len(d_list)) etc
        A_fastener = pi*(r_fastener**2)   #until here correct
        A_list.append(A_fastener)

    A_array = np.array(A_list)

    """Convert coordinates to float numbers"""
    #convert xi_list to float and put in array
    xi_listfloat = []
    for i in fastener_details_list:
        xi = float(i["coord_x"]) # Made similar change here
        xi_listfloat.append(xi)

    xi_array = np.array(xi_listfloat)

    #convert zi_list to float and put in array
    zi_listfloat = []
    for i in fastener_details_list:
        zi = float(i["coord_z"])
        zi_listfloat.append(zi)

    zi_array = np.array(zi_listfloat)

    """Multiply the area by each coordinate"""
    #get area times xi for each fastener
    Axi_array = xi_array * A_array

    #get area times xi for each fastener
    Azi_array = zi_array * A_array

    """Sum the values of each Axi, Azi and A"""
    #sum all values Axi
    Axi_sum = sum(Axi_array)

    #sum all values Azi and sum of all areas
    Azi_sum = sum(Azi_array)


    A_sum = sum(A_array)


    """Calculate cg location"""
    #get xcg value
    xcg = Axi_sum/A_sum

    zcg = Azi_sum/A_sum

    return (xcg, zcg)

"""until here correct""" # Looks correct and makes sense to me -Kristian


def calculate_equivalent_FM(forces_and_moments_dictionary, CG_coordinates): # Working on this one -Kristian
    return { "F_cgx": forces_and_moments_dictionary["F_x"], "F_cgz": forces_and_moments_dictionary["F_z"], "M_cgy": forces_and_moments_dictionary["M_y"] + forces_and_moments_dictionary["F_x"] * (forces_and_moments_dictionary["coord_z"] - CG_coordinates[1])  - forces_and_moments_dictionary["F_z"] * (forces_and_moments_dictionary["coord_x"] - CG_coordinates[0])}


def in_plane_force(cg_forces_and_moments_dictionary, number_of_fasteners): # Working on this one -Kristian
    return { "F_in_plane_x": cg_forces_and_moments_dictionary["F_cgx"] / number_of_fasteners, "F_in_plane_z": cg_forces_and_moments_dictionary["F_cgz"] / number_of_fasteners}


def in_plane_moment(M_cgy, all_fastener_details_list, CG_coordinates, current_fastener_number): # Working on this one -Kristian
    sum_fastener_area_times_r_squared = 0
    for i in all_fastener_details_list:
        denominator_fastener_radius_squared = (i["coord_x"] - CG_coordinates[0]) ** 2 + (i["coord_z"] - CG_coordinates[1]) ** 2
        sum_fastener_area_times_r_squared += denominator_fastener_radius_squared * i["diameter"] ** 2 * pi / 4
    current_fastener_radius = ((all_fastener_details_list[current_fastener_number]["coord_x"] - CG_coordinates[0]) ** 2 + (all_fastener_details_list[current_fastener_number]["coord_z"] - CG_coordinates[1]) ** 2) ** 0.5
    F_in_plane_my = M_cgy * all_fastener_details_list[current_fastener_number]["diameter"] ** 2 * pi / 4 * current_fastener_radius / sum_fastener_area_times_r_squared
    phi = atan2((all_fastener_details_list[current_fastener_number]["coord_x"] - CG_coordinates[0]) , (all_fastener_details_list[current_fastener_number]["coord_z"] - CG_coordinates[1]))
    return { "F_in_plane_x": F_in_plane_my * cos(phi), "F_in_plane_z": - F_in_plane_my * sin(phi)}


"""Bearing stress calculator"""


def bearing_stress_calculator(in_plane_forces_dictionary, current_fastener_details_dictionary, t2):
    Pi = (in_plane_forces_dictionary["F_in_plane_x"]**2+in_plane_forces_dictionary["F_in_plane_z"]**2)**(1/2)
    B_stress = Pi/(current_fastener_details_dictionary["diameter"]*t2)
    return B_stress


TESTING_CG = CG_calculator(TESTING_fasteners_list)
TESTING_equivalent_CG_FM = calculate_equivalent_FM(TESTING_forces_and_moments_temporary_dictionary, TESTING_CG)
TESTING_common_in_plane_forces = in_plane_force(TESTING_equivalent_CG_FM, len(TESTING_fasteners_list))
TESTING_fastener_counter = 0
for i in TESTING_fasteners_list:
    current_fastener_in_plane_moment = in_plane_moment(TESTING_equivalent_CG_FM["M_cgy"], TESTING_fasteners_list, TESTING_CG, TESTING_fastener_counter)
    current_fastener__total_in_plane_forces = {"F_in_plane_x": TESTING_common_in_plane_forces["F_in_plane_x"] + current_fastener_in_plane_moment["F_in_plane_x"], "F_in_plane_z": TESTING_common_in_plane_forces["F_in_plane_z"] + current_fastener_in_plane_moment["F_in_plane_z"]}
    bearing_stress = bearing_stress_calculator(current_fastener__total_in_plane_forces, i, TESTING_t2)

    print("The bearing stress for fastener number", TESTING_fastener_counter+1, "is:", bearing_stress, "\nThe max allowable stress is:", TESTING_stress_allowable, "\n")
    #Check if bearing stress does not exceed allowable stress
    if bearing_stress < TESTING_stress_allowable:
        print("No failure due to bearing stress\nTry to save weight by reducing t2 or removing fasteners\n\n")

    elif bearing_stress == TESTING_stress_allowable:
        print("Bearing stress is equal to allowable stress\n\n")

    elif bearing_stress > TESTING_stress_allowable:
        print("Failure occurs due to bearing stress. Please change one of the following geometries:")
        print("D2\nt2\nnumber of fasteners\nNote, w might change due to this\n\n")

    else:
        print("Failed to compute")

    TESTING_fastener_counter += 1


# Disclaimer: I am absolutely horrible at coming up with variable names. Please feel free to change any of them to whatever actually makes sense... -Kristian