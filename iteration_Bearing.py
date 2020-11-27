import numpy as np
from math import sin, cos, atan2, pi


def bearingstress_everything(dims, lug_material):

    """ Fastener coordinates"""
    e1 = 1.5*dims["w1"] / 5
    e2 = e1

    #take bottom right as 0 point
    #fasteners x z coordinates on righthandside of the lug
    fastcordx_1 = e2
    fastcordz_1 = e1

    fastcordx_2 = e2
    fastcordz_2 = dims["w1"]-e1

    fastcordx_3 = dims["w1"]-e2
    fastcordz_3 = e1

    fastcordx_4 = dims["w1"]-e2
    fastcordz_4 = dims["w1"]-e1

    #fasteners x z location on left handside of the lug
    fastcordx_5 = dims["w1"]+dims["h"]+2*dims["t1"]+e2
    fastcordz_5 = e1

    fastcordx_6 = dims["w1"]+dims["h"]+2*dims["t1"]+e2
    fastcordz_6 = dims["w1"]-e1

    fastcordx_7 = 2*dims["w1"]+dims["h"]+2*dims["t1"]-e2
    fastcordz_7 = e1

    fastcordx_8 = 2*dims["w1"]+dims["h"]+2*dims["t1"]-e2
    fastcordz_8 = dims["w1"]-e1


    TESTING_forces_and_moments_temporary_dictionary = {"F_x": -16523, "M_y": 0, "F_z": 4721, "coord_z": w/2, "coord_x": w+t1+(h/2)}
    TESTING_fasteners_list = [{"coord_x": fastcordx_1, "coord_z": fastcordz_1, "diameter": dims["d2"]}, {"coord_x": fastcordx_2, "coord_z": fastcordz_2, "diameter": dims["d2"]}, {"coord_x": fastcordx_3, "coord_z": fastcordz_3, "diameter": dims["d2"]}, {"coord_x": fastcordx_4, "coord_z": fastcordz_4, "diameter": dims["d2"]}, {"coord_x": fastcordx_5, "coord_z": fastcordz_5, "diameter": dims["d2"]}, {"coord_x": fastcordx_6, "coord_z": fastcordz_6, "diameter": dims["d2"]}, {"coord_x": fastcordx_7, "coord_z": fastcordz_7, "diameter": dims["d2"]}, {"coord_x": fastcordx_8, "coord_z": fastcordz_8, "diameter": dims["d2"]}]
    TESTING_stress_allowable = matstress_allowable
    print("matstress", matstress_allowable)
    spacecraft_wall_thickness = 4E-3

    info_fastener = {"E": 113.8E9, "diameter": dims["d2"], "alpha": 8.6E-6, "Dfo": 0.00678, "Dfi": 0.004} # Fill in with actual values
    lug_E = lug_material["E"]
    alpha_clamped_part = lug_material


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
        #The forces in the x- and z-directions will just be the forces
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
        psi = atan2((all_fastener_details_list[current_fastener_number]["coord_x"] - CG_coordinates[0]) , (all_fastener_details_list[current_fastener_number]["coord_z"] - CG_coordinates[1]))
        return { "F_in_plane_x": F_in_plane_my * cos(psi), "F_in_plane_z": - F_in_plane_my * sin(psi)}


    """Bearing stress calculator"""


    def bearing_stress_calculator(in_plane_forces_dictionary, current_fastener_details_dictionary, t2, F_T):
        Pi = (in_plane_forces_dictionary["F_in_plane_x"]**2+in_plane_forces_dictionary["F_in_plane_z"]**2)**(1/2) + F_T
        B_stress = Pi/(current_fastener_details_dictionary["diameter"]*t2)
        return B_stress


    def calculate_phi(t2, lugbackup_E, Dfo, Dfi, fastener_E, Lhsub, fastenerNomDiameter, Lengsub, t3, nut_E, Lnsub):
        delta_A = 4 * t2 / (lugbackup_E * pi * (Dfo **2 - Dfi ** 2))
        fastener_A = fastenerNomDiameter ** 2 * pi / 4
        delta_B = 1 / fastener_E * (Lhsub + Lengsub + t2 + t3) / fastener_A + Lnsub / (nut_E * fastenerNomDiameter)
        return delta_A / (delta_A + delta_B)


    """ Thermal intensity values """

    #Earth
    J_searth = 1371.3
    J_aearth = 307.4
    J_irearth  = 239.7

    #Jupiter
    J_sjupiter = 52.7
    J_ajupiter = 21.1
    J_irjupiter = 8.2


    """ absorptivity and emissivity values dependent on material """
    absorb_alpha = 0.15 #absorptivity
    epsilon = 0.05 #emmisvity
    sigma = 5.67*10**(-8)


    """ emitting and projected area of lug """
    #calculations of the area
    A_front = 2 * (w * t1) + 3* (h * w) - 4 * pi * (0.5*dims["d2"])**2

    A_sunlitside = t2 * w + L * w + 0.5 * pi * (0.5*w)**2 - pi * (0.5*D1)**2

    A_top = h * t2 * 3 + (L + 0.5 * w) * t1

    A_inside = L*w+0.5*pi*(0.5*w)**2 - pi*(0.5*D1)**2

    A_back = w * (3*h+2*t1)

    A_total = A_sunlitside*2 + A_top *2 + A_inside * 2 + A_back + A_front
    A_i = A_sunlitside  #projected area
    A_e = A_total  #emitting area
    if (A_e < 0):
        return -1

    """" Calculations of Q_absorbed """

    #Q_absorbed = alpha * J_s * A_i + alpha * J_a * A_i + epsilon * J_ir * A_i

    #for earth
    Q_absorbed_earth = absorb_alpha * J_searth * A_i + alpha * J_aearth * A_i + epsilon * J_irearth * A_i

    #for Jupiter
    Q_absorbed_jupiter = absorb_alpha*J_sjupiter*A_i + alpha*J_ajupiter*A_i + epsilon*J_irjupiter*A_i

    if Q_absorbed_earth > Q_absorbed_jupiter:
        Q_absorbed_max = Q_absorbed_earth
        Q_absorbed_min = Q_absorbed_jupiter

    elif Q_absorbed_earth < Q_absorbed_jupiter:
        Q_absorbed_max = Q_absorbed_jupiter
        Q_absorbed_min = Q_absorbed_earth

    """ Calculations for min and max equilibrium temperature"""
    #T = (Q_absorbed/(epsilon*sigma*A_e))^(1/4)
    #min equilibrium temperature
    T_eqmin = (Q_absorbed_min/(epsilon*sigma*A_e))**(1/4)
    #max equilibrium temperature
    T_eqmax = (Q_absorbed_max/ (epsilon*sigma*A_e))**(1/4)


    # print(T_eqmin, "[K]" , T_eqmax, "[K]")


    temperatures = {"reference": 288.15, "min": T_eqmin, "max": T_eqmax} 

    phi = calculate_phi(dims["t2"], lug_E, info_fastener["Dfo"], info_fastener["Dfi"], info_fastener["E"], 0.4 * info_fastener["diameter"], info_fastener["diameter"], 0.33 * info_fastener["diameter"], spacecraft_wall_thickness, info_fastener["E"], 0.4 * info_fastener["diameter"])

    F_T_max = (alpha_clamped_part - info_fastener["alpha"]) * (temperatures["max"] - temperatures["reference"]) * info_fastener["E"] * info_fastener["diameter"] ** 2 / 4 * (1 - phi)
    F_T_min = (alpha_clamped_part - info_fastener["alpha"]) * (temperatures["min"] - temperatures["reference"]) * info_fastener["E"] * info_fastener["diameter"] ** 2 / 4 * (1 - phi)


    TESTING_CG = CG_calculator(TESTING_fasteners_list)
    TESTING_equivalent_CG_FM = calculate_equivalent_FM(TESTING_forces_and_moments_temporary_dictionary, TESTING_CG)
    TESTING_common_in_plane_forces = in_plane_force(TESTING_equivalent_CG_FM, len(TESTING_fasteners_list))
    TESTING_fastener_counter = 0
    fastener_max_stress_list = []
    for i in TESTING_fasteners_list:
        current_fastener_in_plane_moment = in_plane_moment(TESTING_equivalent_CG_FM["M_cgy"], TESTING_fasteners_list, TESTING_CG, TESTING_fastener_counter)
        current_fastener__total_in_plane_forces = {"F_in_plane_x": TESTING_common_in_plane_forces["F_in_plane_x"] + current_fastener_in_plane_moment["F_in_plane_x"], "F_in_plane_z": TESTING_common_in_plane_forces["F_in_plane_z"] + current_fastener_in_plane_moment["F_in_plane_z"]}
        bearing_stress_Tref = bearing_stress_calculator(current_fastener__total_in_plane_forces, i, dims["t2"], 0)
        bearing_stress_Tmin = bearing_stress_calculator(current_fastener__total_in_plane_forces, i, dims["t2"], F_T_min)
        bearing_stress_Tmax = bearing_stress_calculator(current_fastener__total_in_plane_forces, i, dims["t2"], F_T_max) 

        print("The bearing stress for fastener number", TESTING_fastener_counter+1, "is:", bearing_stress_Tmin, "-", bearing_stress_Tmax, "\nThe max allowable stress is:", TESTING_stress_allowable, "\n")
        #Check if bearing stress does not exceed allowable stress
        if bearing_stress_Tmax < TESTING_stress_allowable:
            print("No failure due to bearing stress at any temperature.\nTry to save weight by reducing t2 or removing fasteners\n\n")

        elif bearing_stress_Tmax == TESTING_stress_allowable:
            print("Bearing stress is equal to allowable stress\n\n")

        elif bearing_stress_Tmax > TESTING_stress_allowable:
            print("Failure occurs due to bearing stress. Please change one of the following geometries:")
            print("D2\nt2\nnumber of fasteners\nNote, w might change due to this\n\n")

        else:
            print("Failed to compute")

        print("The MS for fastener number", TESTING_fastener_counter+1, "is:", (TESTING_stress_allowable/bearing_stress_Tmax)-1)
        fastener_max_stress_list.append((TESTING_stress_allowable/bearing_stress_Tmax)-1)

        TESTING_fastener_counter += 1

    return fastener_max_stress_list
    # Disclaimer: I am absolutely horrible at coming up with variable names. Please feel free to change any of them to whatever actually makes sense... -Kristian
